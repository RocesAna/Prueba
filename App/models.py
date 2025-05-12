# contacts/models.py
from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    correo_electronico = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas Adicionales")
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se añade automáticamente al crear
    fecha_actualizacion = models.DateTimeField(auto_now=True) # Se actualiza automáticamente al guardar

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['apellido', 'nombre'] # Ordenar por defecto