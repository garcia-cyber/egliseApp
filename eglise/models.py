from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Fonction(models.Model):
    nomFonction = models.CharField(max_length=30) 

    def __str__(self):
        return self.nomFonction 
# ===============================
# cellule 
# ===============================
class Cellule(models.Model):
    nomCellule = models.CharField(max_length=30) 
    province   = models.CharField(max_length=30) 

    def __str__(self):
        return self.nomCellule
    
    
# =================================
# profile 
# =================================
class Profil(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    fonction = models.ForeignKey(Fonction , on_delete=models.CASCADE ) 
    celluel  = models.ForeignKey(Cellule , on_delete= models.CASCADE) 
    phone = models.IntegerField()


    def __str__(self):
        return self.phone 
    
