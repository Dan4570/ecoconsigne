from django.http import JsonResponse
from .models import Ecocitoyen, Depot
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

def get_info_rfid(request, rfid):
    try:
        eco = Ecocitoyen.objects.get(rfid=rfid)
        total = sum([
            d.nb_plastique + d.nb_verre + d.nb_metal
            for d in eco.depot_set.all()
        ])
        data = {
            "rfid": eco.rfid,
            "nom": f"{eco.nom} {eco.prenom}",
            "compte": str(total)
        }
        return JsonResponse(data)
    except Ecocitoyen.DoesNotExist:
        return JsonResponse({"error": "Utilisateur non trouvé"}, status=404)

def get_last_depot(request, rfid):
    try:
        eco = Ecocitoyen.objects.get(rfid=rfid)
        last_depot = Depot.objects.filter(ecocitoyen=eco).order_by('-date').first()
        if last_depot is None:
            return JsonResponse({
                "rfid": rfid,
                "date": None,
                "contenants": "M:0,P:0,V:0"
            })
        data = {
            "rfid": rfid,
            "date": last_depot.date.strftime("%Y-%m-%d %H:%M:%S"),
            "contenants": f"M:{last_depot.nb_metal},P:{last_depot.nb_plastique},V:{last_depot.nb_verre}"
        }
        return JsonResponse(data)
    except Ecocitoyen.DoesNotExist:
        return JsonResponse({"error": "Utilisateur non trouvé"}, status=404)

# --- Nouvelle fonction à ajouter ---

def ecocitoyens_json(request):
    ecocitoyens = Ecocitoyen.objects.all().values(
        'id', 'nom', 'prenom', 'date_naissance', 'email', 'telephone', 'commune', 'rfid'
    )
    return JsonResponse(list(ecocitoyens), safe=False)
