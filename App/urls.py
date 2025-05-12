# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Read (List)
    path('', views.contact_list, name='contact_list'),
    # Create
    path('nuevo/', views.contact_create, name='contact_create'),
    # Update
    path('editar/<int:pk>/', views.contact_update, name='contact_update'),
    # Delete
    path('eliminar/<int:pk>/', views.contact_delete, name='contact_delete'),
    # Read (Detail - Opcional)
    path('detalle/<int:pk>/', views.contact_detail, name='contact_detail'),
]