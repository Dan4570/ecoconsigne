import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_ecoconsigne.settings')
django.setup()

from depot.models import Ecocitoyen, Depot

# Nettoyage (si tu veux repartir de zéro)
Depot.objects.all().delete()
Ecocitoyen.objects.all().delete()

noms = [
    ("Jean", "TOTO"), ("Hina", "NOA"), ("Léo", "MARTIN"), ("Sophie", "DURAND"),
    ("Lucas", "MOREAU"), ("Emma", "ROUX"), ("Manu", "FELIX"), ("Clara", "LOPEZ"),
    ("Nico", "RAMOS"), ("Jade", "TAUI")
]

communes = ["Mont-Dore", "Dumbéa", "Nouméa", "Païta"]

for i, (prenom, nom) in enumerate(noms):
    eco = Ecocitoyen.objects.create(
        nom=nom,
        prenom=prenom,
        date_naissance="2000-01-01",
        email=f"{prenom.lower()}.{nom.lower()}@mail.com",
        telephone=f"75{random.randint(100000,999999)}",
        commune=random.choice(communes),
        rfid=str(10000 + i)
    )

    # Ajoute entre 2 et 5 dépôts par personne
    for j in range(random.randint(2, 5)):
        Depot.objects.create(
            ecocitoyen=eco,
            date=datetime.now() - timedelta(days=random.randint(1, 60)),
            nb_plastique=random.randint(0, 10),
            nb_verre=random.randint(0, 10),
            nb_metal=random.randint(0, 10),
        )

print("✅ Données de test ajoutées avec succès !")
