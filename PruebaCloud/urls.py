# myproject/urls.py
from django.contrib import admin
from django.urls import path, include # Asegúrate de importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')), # Incluye las URLs de la app contacts bajo el prefijo /contactos/
    # Puedes añadir una ruta raíz si quieres
    # path('', include('contacts.urls')), # Si quieres que la lista sea la página principal
]