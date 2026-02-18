from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Fonction(models.Model):
    nomFonction = models.CharField(max_length=30) 

    def __str__(self):
        return self.nomFonction 
    
# =================================
# profile 
# =================================

