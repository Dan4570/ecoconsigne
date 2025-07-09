import os
import django
import random
from datetime import datetime, timedelta
from faker import Faker  # Librairie pour générer des données réalistes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_ecoconsigne.settings')
django.setup()

from depot.models import Ecocitoyen, Depot

fake = Faker('fr_FR')  # Utilise une locale française pour les noms, dates, etc.

# Nettoyage (si tu veux repartir de zéro)
Depot.objects.all().delete()
Ecocitoyen.objects.all().delete()

communes = ["Mont-Dore", "Dumbéa", "Nouméa", "Païta"]

NOMBRE_ECOCITOYENS = 100  # Nombre d'écocitoyens à créer

for i in range(NOMBRE_ECOCITOYENS):
    prenom = fake.first_name()
    nom = fake.last_name()
    date_naissance = fake.date_of_birth(minimum_age=18, maximum_age=80)
    email = f"{prenom.lower()}.{nom.lower()}@mail.com"
    telephone = fake.phone_number()
    commune = random.choice(communes)
    rfid = str(10000 + i)

    eco = Ecocitoyen.objects.create(
        nom=nom,
        prenom=prenom,
        date_naissance=date_naissance,
        email=email,
        telephone=telephone,
        commune=commune,
        rfid=rfid,
    )

    # Ajoute entre 2 et 10 dépôts par personne
    nombre_depots = random.randint(2, 10)
    for _ in range(nombre_depots):
        Depot.objects.create(
            ecocitoyen=eco,
            date=datetime.now() - timedelta(days=random.randint(1, 180)),
            nb_plastique=random.randint(0, 20),
            nb_verre=random.randint(0, 20),
            nb_metal=random.randint(0, 20),
        )

print(f"✅ {NOMBRE_ECOCITOYENS} écocitoyens et leurs dépôts ajoutés avec succès !")
