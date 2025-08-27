from django.http import JsonResponse
from .models import Ecocitoyen, Depot

# --- API 1 : Identification éco-citoyen ---
def get_info_rfid(request, rfid):
    try:
        eco = Ecocitoyen.objects.get(rfid=rfid)
        data = {
            "rfid": eco.rfid,
            "nom": f"{eco.nom} {eco.prenom}",
            "valid": True
        }
    except Ecocitoyen.DoesNotExist:
        data = {
            "rfid": rfid,
            "nom": "",
            "valid": False
        }
    return JsonResponse(data)

# --- API 2 : Dernier dépôt ---
def get_last_depot(request, rfid):
    try:
        eco = Ecocitoyen.objects.get(rfid=rfid)
        last_depot = Depot.objects.filter(ecocitoyen=eco).order_by('-date').first()
        if last_depot is None:
            data = {
                "rfid": rfid,
                "contenants": {"M": 0, "P": 0, "V": 0}
            }
        else:
            data = {
                "rfid": rfid,
                "contenants": {
                    "M": last_depot.nb_metal,
                    "P": last_depot.nb_plastique,
                    "V": last_depot.nb_verre
                }
            }
    except Ecocitoyen.DoesNotExist:
        data = {
            "rfid": rfid,
            "contenants": {"M": 0, "P": 0, "V": 0}
        }
    return JsonResponse(data)

# --- Liste complète des écocitoyens ---
def ecocitoyens_json(request):
    ecocitoyens = Ecocitoyen.objects.all().values(
        'id', 'nom', 'prenom', 'date_naissance', 'email', 'telephone', 'commune', 'rfid'
    )
    return JsonResponse(list(ecocitoyens), safe=False)

# --- Recherche par ID ---
from django.shortcuts import get_object_or_404
def get_ecocitoyen_by_id(request, id):
    eco = get_object_or_404(Ecocitoyen, pk=id)
    data = {
        "id": eco.id,
        "nom": eco.nom,
        "prenom": eco.prenom,
        "date_naissance": eco.date_naissance,
        "email": eco.email,
        "telephone": eco.telephone,
        "commune": eco.commune,
        "rfid": eco.rfid
    }
    return JsonResponse(data)
