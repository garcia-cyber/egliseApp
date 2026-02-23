from django.contrib import admin
from .models import * 

# Register your models here.


# ====================================
# fonction 
# ====================================

@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
	list_display = ['nomFonction']

# ======================================
# cellule 
# ======================================

@admin.register(Cellule)
class CelluleAdmin(admin.ModelAdmin):
	list_display = ['nomCellule', 'province'] 

# ======================================
# profile 
# ======================================

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
	list_display = ['user','user__email','fonction','phone','sexeUser','cellule','cellule__province'] 

# =======================================
#  departement
# =======================================
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
	list_display = ['nomDepartement']


# =======================================
#  membre 
# =======================================
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
	list_display = ['noms','sexe','etatCivil','phone','adresse','province','departement','typeM','deces','userMembre']

# =======================================
#  type de cotisation  
# =======================================
@admin.register(TypeCotisation)
class TypeCotisationAdmin(admin.ModelAdmin):
	list_display = ['typeCotisation'] 


# =======================================
#  cotisations 
# =======================================
@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
	list_display = ['cotisation','montant','dateCotisation','userCotisation','membreCotisation'] 

# =======================================
#  evenement 
# =======================================
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
	list_display = ['nomEvenement','dateEvenement','userEvenement']

# =======================================
# type de permission
# =======================================
@admin.register(TypePermission)
class TypePermissionAdmin(admin.ModelAdmin):
	list_display = ['typePermission']

# ======================================
# permission 
# ======================================
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = ['permission','userPermission','datePermission']

# =====================================
# materiel
# =====================================
@admin.register(Materiel)
class MaterielAdmin(admin.ModelAdmin):
	list_display = ['nomMateriel','etatMateriel','quantiteMateriel','userMateriel','dateRegister']

# ====================================
#  
# ====================================

