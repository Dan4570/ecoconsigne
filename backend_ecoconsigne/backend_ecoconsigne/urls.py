from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil !")

urlpatterns = [
    path('', home, name='home'),  # route pour /
    path('admin/', admin.site.urls),
    path('api/', include('depot.urls')),
]
