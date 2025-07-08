from django.contrib import admin
from .models import Depot  # importe ton modèle Depot

admin.site.register(Depot)  # enregistre le modèle Depot dans l'admin
