
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs de profil si nécessaire
# models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    OFFRE = 0
    DEMANDE = 1
    TYPE_CHOICES = [
        (OFFRE, 'Offre'),
        (DEMANDE, 'Demande'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Stage(Post):
    OUVRIER = 1
    TECHNICIEN = 2
    PFE = 3
    TYPE_CHOICES = [
        (OUVRIER, 'Ouvrier'),
        (TECHNICIEN, 'Technicien'),
        (PFE, 'Projet de Fin dÉtudes'),
    ]
    stage_type = models.IntegerField(choices=TYPE_CHOICES)

class Logement(Post):
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Evenement(Post):
    description = models.TextField()
    event_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Transport(Post):
    destination = models.CharField(max_length=200)
