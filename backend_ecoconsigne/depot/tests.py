from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Ecocitoyen, Depot

class DepotAPITestCase(TestCase):
    def setUp(self):
        self.eco = Ecocitoyen.objects.create(
            nom="Doe",
            prenom="John",
            date_naissance="1990-01-01",
            email="john@example.com",
            telephone="123456789",
            commune="Nouméa",
            rfid="123456"
        )

        self.depot1 = Depot.objects.create(
            ecocitoyen=self.eco,
            date=timezone.now() - timezone.timedelta(days=1),
            nb_plastique=5,
            nb_verre=0,
            nb_metal=0,
            montant=50.0,
            regle=False
        )

        self.depot2 = Depot.objects.create(
            ecocitoyen=self.eco,
            date=timezone.now(),
            nb_plastique=2,
            nb_verre=1,
            nb_metal=3,
            montant=30.0,
            regle=True
        )

    def test_get_last_depot_model(self):
        last_depot = Depot.objects.filter(ecocitoyen=self.eco).latest('date')
        self.assertEqual(last_depot, self.depot2)

    def test_get_last_depot_api(self):
        url = reverse('get_last_depot', args=[self.eco.rfid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['contenants']['P'], self.depot2.nb_plastique)
        self.assertEqual(data['contenants']['V'], self.depot2.nb_verre)
        self.assertEqual(data['contenants']['M'], self.depot2.nb_metal)
