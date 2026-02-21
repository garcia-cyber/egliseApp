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
	list_display = ['user','user__email','fonction','phone','sexeUser'] 

# =======================================
#  departement
# =======================================
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
	list_display = ['nomDepartement']


