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
    TYPEETAT = [
                ('marie','Marie') ,
                ('celibateur' , 'Celibateur') , 
                ('veuve' , 'Veuve') ,
                ('divorce' , 'Divorce') , 
                ('veuf' , 'Veuf') 
            ]
    etatCivil   = models.CharField(max_length = 30 , choices = TYPEETAT , null = True)  
    deces = models.CharField(max_length = 30 , default = 'non', null = True)
    typeM = models.CharField(max_length = 30 , default = 'membre', null = True) 



    def __str__(self):
        return self.noms

# ================================
# models cotication type
# ================================
class TypeCotisation(models.Model):
    typeCotisation = models.CharField(max_length= 40 )


    def __str__(self):
        return self.typeCotisation 
# ================================
# models cotication
# ================================
class Cotisation(models.Model):
    cotisation = models.ForeignKey(TypeCotisation, on_delete = models.CASCADE , null = True) 
    montant  = models.DecimalField(max_digits=10 ,decimal_places= 2) 
    statut   = models.CharField(default = 'oui')
    dateCotisation = models.DateField(null = True) 
    userCotisation = models.ForeignKey(User , on_delete = models.CASCADE , null = True) 
    TYPEDEVISE = [
        ('cdf','Cdf') ,
        ('usd' , 'Usd')
    ]
    devise = models.CharField(max_length = 10 , null = True , choices = TYPEDEVISE , default = 'cdf') 
    membreCotisation = models.ForeignKey(Membre , on_delete = models.CASCADE, null = True ) 


    def __str__(self):
        return self.statut 

# ===============================
#  evenement 
# ===============================
class Evenement(models.Model):
    nomEvenement = models.CharField(max_length = 50)
    dateEvenement = models.DateField()
    userEvenement = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.nomEvenement 

# ===============================
# permission 
# ================================
class TypePermission(models.Model):
    typePermission = models.CharField(max_length = 40 , null = True)

    def __str__(self):
        return self.typePermission 
# ================================
#  permission 
# ================================
class Permission(models.Model):
    permission = models.ForeignKey(TypePermission , on_delete = models.CASCADE) 
    userPermission = models.ForeignKey(User , on_delete = models.CASCADE) 
    statutP = models.CharField(max_length = 3 , null = True , default = 'oui')
    datePermission = models.DateField()

    def __str__(self):
        return self.statutP

# =================================
# bloquer user
# =================================
class Bloque(models.Model):
    CHOIXB = [
    ('active', 'Active') , 
    ('bloque','Bloque')]
    statutB = models.CharField(max_length = 15 , choices = CHOIXB) 
    userBloque = models.ForeignKey(User , on_delete = models.CASCADE) 

    def __str__(self):
        return self.statutB 

# ===================================
# materiels
# ===================================
class Materiel(models.Model):
    nomMateriel = models.CharField(max_length = 50 , null = True) 
    ETATCHOIX = [
        ('tres bon','Tres Bon') , 
        ('bon' , 'Bon') , 
        ('panne' , 'Panne')

    ]
    etatMateriel = models.CharField(max_length = 30 , choices = ETATCHOIX, null = True)
    dateRegister = models.DateField(auto_now_add = True)  
    quantiteMateriel = models.IntegerField()
    userMateriel = models.ForeignKey(User , on_delete = models.CASCADE , null = True) 


    def __str__(self):
        return self.nomMateriel
 
