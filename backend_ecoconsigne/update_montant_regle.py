import os
import django

# Préparation de l'environnement Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_ecoconsigne.settings")
django.setup()

from depot.models import Depot

def update_montant_and_regle():
    depots = Depot.objects.all()
    for depot in depots:
        montant_calcule = (
            depot.nb_plastique * 10 +   # 10 FCFP par plastique
            depot.nb_verre * 12 +       # 12 FCFP par verre
            depot.nb_metal * 15         # 15 FCFP par métal
        )

        depot.montant = round(montant_calcule, 2)
        depot.regle = montant_calcule > 0
        depot.save()

        print(f"Depot {depot.id} mis à jour : montant={depot.montant}, regle={depot.regle}")

if __name__ == "__main__":
    update_montant_and_regle()
