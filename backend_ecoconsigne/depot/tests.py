from django.test import TestCase, Client
from .models import Ecocitoyen, Depot
from django.utils import timezone

class ApiTests(TestCase):
    def setUp(self):
        # Créer un éco-citoyen pour les tests
        self.eco = Ecocitoyen.objects.create(
            nom="Dupont",
            prenom="Jean",
            date_naissance="1990-01-01",
            email="dupont@example.com",
            telephone="12345678",
            commune="Nouméa",
            rfid="RFID123"
        )
        # Créer un dépôt pour ce citoyen
        self.depot = Depot.objects.create(
            ecocitoyen=self.eco,
            date=timezone.now(),
            nb_plastique=2,
            nb_verre=3,
            nb_metal=1
        )
        self.client = Client()

    def test_get_info_rfid_existant(self):
        response = self.client.get(f'/api/getinfo/{self.eco.rfid}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["rfid"], self.eco.rfid)
        self.assertEqual(data["nom"], f"{self.eco.nom} {self.eco.prenom}")
        self.assertTrue(data["valid"])

    def test_get_info_rfid_inexistant(self):
        response = self.client.get('/api/getinfo/INCONNU')
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertFalse(data["valid"])

    def test_get_last_depot_existant(self):
        response = self.client.get(f'/api/getdata/{self.eco.rfid}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["rfid"], self.eco.rfid)
        self.assertEqual(data["contenants"]["M"], self.depot.nb_metal)
        self.assertEqual(data["contenants"]["P"], self.depot.nb_plastique)
        self.assertEqual(data["contenants"]["V"], self.depot.nb_verre)

    def test_get_last_depot_aucun(self):
        # Créer un citoyen sans dépôt
        eco2 = Ecocitoyen.objects.create(
            nom="Durand",
            prenom="Alice",
            date_naissance="1992-05-05",
            email="durand@example.com",
            telephone="87654321",
            commune="Mont-Dore",
            rfid="RFID456"
        )
        response = self.client.get(f'/api/getdata/{eco2.rfid}')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["rfid"], eco2.rfid)
        self.assertEqual(data["contenants"]["M"], 0)
        self.assertEqual(data["contenants"]["P"], 0)
        self.assertEqual(data["contenants"]["V"], 0)
