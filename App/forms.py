# contacts/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = '__all__' # Incluye todos los campos del modelo
        # O especifica los campos que quieres en el formulario:
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'notas']

        # Opcional: Personalizar widgets o labels si es necesario
        # widgets = {
        #     'notas': forms.Textarea(attrs={'rows': 3}),
        # }
        # labels = {
        #     'correo_electronico': 'Email',
        # }