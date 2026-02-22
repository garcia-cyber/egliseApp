from django.contrib.auth.models import User
from django import forms 
from .models import Profil 
from .models import *


# creation du formulaire d'authentification 
# ==========================================
# ==========================================
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30 , widget = forms.TextInput(attrs={'class':'form-control'})) 
    password = forms.CharField(max_length = 200 , widget = forms.PasswordInput(attrs={'class':'form-control'})) 

# ===============================================
#  
# ===============================================

class UtilisateurForm(forms.ModelForm):
    password = forms.CharField(max_length=200 , widget= forms.PasswordInput(attrs={'class':'form-control'}), label='mot de passe utilisateur') 

    class  Meta:
        model = User 
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}) ,
            'email': forms.EmailInput(attrs={'class':'form-control'}) ,
            
        }      

        labels = {
            'username': 'nom utilisateur' , 
            'email': 'email utilisateur' , 
            'password': 'mot de passe utilisateur' , 

        }  

# =====================================================
#  form profile 
# =====================================================

class ProfilForm(forms.ModelForm):
    class Meta :
        model = Profil 
        fields = ['fonction','cellule','phone','sexeUser','user']
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}) ,
            'fonction': forms.Select(attrs={'class':'form-control'}) ,
            'cellule': forms.Select(attrs={'class':'form-control'}) ,
            'phone': forms.TextInput(attrs={'class':'form-control'}) ,
            'sexeUser': forms.Select(attrs={'class':'form-control'}) , 
            
        } 


# =====================================================
#  form membre
# =====================================================
class MembreForm(forms.ModelForm):
    class Meta :
        model = Membre 
        fields = ['noms','sexe','etatCivil','phone','adresse','province','departement' ]

        widgets = {
            'noms' : forms.TextInput(attrs={'class':'form-control'}) ,
            'sexe' : forms.Select(attrs={'class':'form-control'}) ,
            'etatCivil' : forms.Select(attrs={'class':'form-control'}) ,
            'phone' : forms.NumberInput(attrs={'class':'form-control'}) ,
            'adresse' : forms.TextInput(attrs={'class':'form-control'}) ,
            'province' : forms.TextInput(attrs={'class':'form-control'}) ,
            'departement' : forms.Select(attrs={'class':'form-control'}) ,
        }

# ====================================
# evenement form 
# ===================================
class EvenementForm(forms.ModelForm):
    class Meta :
        model   = Evenement 
        fields  = ['nomEvenement','dateEvenement']
        widgets = {
            'nomEvenement' : forms.TextInput(attrs={'class':'form-control'}) ,
            'dateEvenement' : forms.DateInput(attrs={'type' :'date','class':'form-control'}) 
        } 


    # def clean_nomEvenement(self):
    #     nomEvenement = self.cleaned_data.get("nomEvenement")

    #     if Evenement.objects.filter(nomEvenement = nomEvenement).exist():
    #         raise forms.ValidationError("le nom Evenement existe")

    #     return nomEvenement