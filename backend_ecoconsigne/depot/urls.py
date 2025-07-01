from django.urls import path
from . import views

urlpatterns = [
    # API GET n°1 : identification d’un écocitoyen via RFID
    path('getinfo/<str:rfid>', views.get_info_rfid, name='get_info_rfid'),

    # API GET n°2 : dernier dépôt d’un écocitoyen via RFID
    path('getdata/<str:rfid>', views.get_last_depot, name='get_last_depot'),
]
