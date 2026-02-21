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
# profil
# =================================
class Profil(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    fonction = models.ForeignKey(Fonction , on_delete=models.CASCADE ) 
    cellule  = models.ForeignKey(Cellule , on_delete= models.CASCADE) 
    phone = models.IntegerField()
    TYPESEXE = [
        ('masculin','Masculin') , 
        ('feminin' , 'Feminin')
    ]
    sexeUser = models.CharField(max_length =15 , choices  = TYPESEXE , null = True)



    def __str__(self):
        return self.sexeUser
    
# =================================
# departement 
# =================================
class Departement(models.Model):
    nomDepartement = models.CharField(max_length=30) 


    def __str__(self):
        return self.nomDepartement


# ================================
#  membres eglise 
# ================================
class Membre(models.Model):
    noms = models.CharField(max_length= 60)
    TYPESEXE = [
        ('Masculin', 'masculin') , 
        ('Feminin', 'feminin')
    ]
    sexe = models.CharField(max_length = 15 , choices = TYPESEXE) 
    phone = models.IntegerField()   
    adresse = models.CharField(max_length = 80 , null = True ) 
    province = models.CharField(max_length = 40 , null = True)
    userMembre = models.ForeignKey(User , on_delete = models.CASCADE , null = True)  
    departement = models.ForeignKey(Departement, on_delete = models.CASCADE , null = True) 



    def __str__(self):
        return self.noms


 
