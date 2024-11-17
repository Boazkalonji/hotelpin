from django.db import models
from django.contrib.auth.models import User




class Categories(models.Model):
    liblle = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.description} {self.liblle}'




class Chambres(models.Model):
    id_categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='image_chambre' , blank = False , null = False)
    prix = models.IntegerField(null=False, blank = False)
    def __str__(self):
        return f'{self.description} {self.prix} {self.image}'




class Comptes(models.Model):
    liblle = models.CharField(max_length=30)

    def __str__(self):
        return self.liblle





class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compte = models.ForeignKey(Comptes, on_delete=models.CASCADE, null=False)
    chambre = models.ForeignKey(Chambres, on_delete=models.CASCADE, blank=True)

    date_debut = models.DateField(null=False)
    date_fin = models.DateField(null=False)
    num_compte = models.IntegerField()
    durer = models.IntegerField()
    code_reservation = models.IntegerField(unique=True)
    def __str__(self):
        
        return f'{self.date_debut} {self.date_fin} {self.num_compte}'




class Message(models.Model):
    sujet = models.TextField(null=False, blank=False, max_length=60)
    nom = models.CharField(max_length=60)
    postnom = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    message = models.TextField(max_length=200)