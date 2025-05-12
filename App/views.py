# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy # Usado para redirects después de operaciones

# READ - Listar todos los contactos
def contact_list(request):
    contacts = Contact.objects.all() # Obtiene todos los objetos Contact
    context = {'contacts': contacts}
    return render(request, 'contact_list.html', context)

# CREATE - Añadir un nuevo contacto
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el nuevo contacto en la BD
            return redirect('contact_list') # Redirige a la lista de contactos
    else: # Si es método GET (primera visita a la página)
        form = ContactForm() # Crea un formulario vacío
    context = {'form': form}
    return render(request, 'contact_form.html', context)

# UPDATE - Editar un contacto existente
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk) # Obtiene el contacto o error 404
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact) # Carga datos del POST en el form asociado al contacto
        if form.is_valid():
            form.save() # Guarda los cambios en la BD
            return redirect('contact_list') # Redirige a la lista
    else: # Si es método GET
        form = ContactForm(instance=contact) # Crea form pre-llenado con datos del contacto
    context = {'form': form, 'contact': contact} # Pasamos el contacto para saber si estamos editando
    return render(request, 'contact_form.html', context)

# DELETE - Eliminar un contacto
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST': # Solo permite borrar vía POST por seguridad
        contact.delete()
        return redirect('contact_list')
    # Si es GET, mostramos una confirmación (opcional pero recomendado)
    context = {'contact': contact}
    return render(request, 'contact_confirm_delete.html', context)

# READ (Detail) - Opcional: Ver detalles de un solo contacto
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    context = {'contact': contact}
    return render(request, 'contact_detail.html', context) # Necesitarás crear este template