from django.db import models

class Ecocitoyen(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    commune = models.CharField(max_length=100)
    rfid = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Depot(models.Model):
    ecocitoyen = models.ForeignKey(Ecocitoyen, on_delete=models.CASCADE)
    date = models.DateTimeField()
    nb_plastique = models.IntegerField(default=0)
    nb_verre = models.IntegerField(default=0)
    nb_metal = models.IntegerField(default=0)

    montant = models.FloatField(null=True, blank=True)
    regle = models.BooleanField(default=False)

    def __str__(self):
        return f"Depot {self.date} - {self.ecocitoyen.nom}"
