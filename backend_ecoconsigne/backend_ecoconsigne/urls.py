from django.contrib import admin
from django.urls import path, include  # 👈 ajoute "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('depot.urls')),  # 👈 ajoute cette ligne pour brancher les URL de l’app "depot"
]
