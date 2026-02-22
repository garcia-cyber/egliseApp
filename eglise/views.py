from django.shortcuts import render  , redirect 
from django.contrib.auth import authenticate , login as auth , logout 
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.contrib.auth.models import User
from .models import * 

# Create your views here.

#==============================================================
# home
# =============================================================
def home(request):
    return render(request , 'front/index.html')

#==============================================================
# login 
# =============================================================
def login(request):
    msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password'] 

            user = authenticate(username = username , password = password) 
            if user :
                auth(request,user) 
                return redirect('panel') 
            else:
                msg = "mot de passe erronne !!!:🤞"
    form = LoginForm()
    return render(request, 'back/auth-login.html', {'form':form , 'msg':msg})  

# =============================================================
# deconnexion 
# ============================================================
def deco(request):
    logout(request)
    return redirect('home')

# ============================================================
# panel controle 
# =============================================================
@login_required()
def panel(request):

    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 
    # =============================
    # nombre user systeme
    # ============================
    userCount = User.objects.count()

    # ==================================
    # nombre de membre chez admin central 
    # ===================================
    membreCount = Membre.objects.count()

    # =============================
    #  NOMBRE DES HOMMES
    # =============================

    homme = Membre.objects.filter( sexe = 'Masculin', typeM = 'membre').count()

    # =============================
    #  NOMBRE DES FEMMES
    # =============================
    femme = Membre.objects.filter( sexe = 'Feminin', typeM = 'membre').count()

    # =============================
    #  NOMBRE DES MARIES
    # ============================= 
    marie = Membre.objects.filter(etatCivil = 'marie' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES CELIBATEURS
    # ============================= 
    celibateur =  Membre.objects.filter(etatCivil = 'celibateur' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES VEUVES
    # ============================= 
    veuve = Membre.objects.filter(etatCivil = 'veuve' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES VEUF
    # ============================= 
    veuf = Membre.objects.filter(etatCivil = 'veuf' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES EVENEMENT
    # ============================= 
    evenement = Evenement.objects.count()


    # =================== CELLULE NOMBRES ======================

    # =============================
    # NOMBRE MEMBRE PAR CELLULE 
    # =============================
    cellule = Membre.objects.filter(userMembre = request.user).count()

    # =============================
    #  NOMBRE DES HOMMES
    # =============================

    hommeC = Membre.objects.filter(userMembre = request.user , sexe = 'Masculin', typeM = 'membre').count()

    # =============================
    #  NOMBRE DES FEMMES
    # =============================
    femmeC = Membre.objects.filter(userMembre = request.user , sexe = 'Feminin', typeM = 'membre').count()

    # =============================
    #  NOMBRE DES MARIES
    # ============================= 
    marieC = Membre.objects.filter(userMembre = request.user , etatCivil = 'marie' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES CELIBATEURS
    # ============================= 
    celibateurC =  Membre.objects.filter(userMembre = request.user , etatCivil = 'celibateur' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES VEUVES
    # ============================= 
    veuveC = Membre.objects.filter(userMembre = request.user , etatCivil = 'veuve' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES VEUF
    # ============================= 
    veufC = Membre.objects.filter(userMembre = request.user , etatCivil = 'veuf' , typeM = 'membre').count()

    # =============================
    #  NOMBRE DES EVENEMENT C
    # ============================= 
    evenementC = Evenement.objects.filter(userEvenement = request.user).count()


    context = {
        'userCount': userCount ,
        'fonction':fonction , 
        'membre' : membreCount , 
        'cellule' : cellule , 
        'hommeC'  : hommeC ,
        'femmeC' : femmeC , 
        'celibateurC' : celibateurC ,
        'marieC' : marieC,
        'veuveC'   : veuveC ,
        'veufC' : veufC ,
        'homme'  : homme ,
        'femme' : femme , 
        'celibateur' : celibateur ,
        'marie' : marie,
        'veuve'   : veuve ,
        'veuf' : veuf ,
        'evenement':evenement , 
        'evenementC' : evenementC
        }
    return render(request, 'back/index.html', context) 

# ============================================================
# add employe 
# =============================================================
@login_required()
def utilisateurAdd(request):
    msg = None 
    if request.method == 'POST':
        form = UtilisateurForm(request.POST) 
        if form.is_valid():
            user = form.save(commit= False) 
            user.set_password(form.cleaned_data['password']) 
            user.save()
            
            msg = "information enregistre"
            form = UtilisateurForm(request.POST) 
    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    form = UtilisateurForm()
    return render(request, 'back/employeAdd.html', {'form':form, 'msg': msg, 'fonction':fonction})  

# =================================================================
# liste des utilisateurs 
# =================================================================
@login_required()
def utilisateurRead(request):
    lst = User.objects.all()
    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    return render(request , 'back/employeRead.html', {'lst': lst, 'fonction':fonction})

# =================================================================
# attribue profil  
# =================================================================
@login_required()
def profilAdd(request):
  
    msg = None 
    if request.method == 'POST':
        form = ProfilForm(request.POST) 

        if form.is_valid():
            form.save()
            
            
            msg = "profil ajouter"


    form = ProfilForm() 
    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    return render(request , 'back/employeUpdate.html',{'fonction':fonction,'form':form, 'msg':msg}) 

# ==================================================================
#  enregistrement des membres
# ==================================================================
@login_required()
def membreAdd(request):
    msg = None 
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            membre = form.save(commit = False) 
            if request.user.is_authenticated:
                membre.userMembre = request.user
                membre.save()
                msg = 'membre enregistre '
                form = MembreForm(request.POST)
            else:
                msg = "erreur" 
    form = MembreForm()

    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    return render(request, 'back/membreAdd.html',{'fonction':fonction , 'msg':msg , 'form': form}) 


# ==================================================================
#  liste des membres
# ==================================================================
@login_required()
def membreRead(request):

    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    lst = Membre.objects.filter(userMembre = request.user).all()

    return render(request , 'back/membreRead.html',{'fonction':fonction , 'lst': lst})  

# ==================================================================
#  add evenement 
# ==================================================================
@login_required()
def evenementAdd(request):
    msg = None
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            use = form.save(commit = False)

            if request.user.is_authenticated :
                use.userEvenement = request.user 
                use.save()
                msg = "evenement enregistre"



    form = EvenementForm()

    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    return render(request , 'back/evenementAdd.html',{'fonction':fonction, 'form':form , 'msg':msg})  

# ==================================================================
#  read evenement 
# ==================================================================
login_required()
def evenementRead(request):

    profil = Profil.objects.filter(user = request.user).first()
    fonction = profil.fonction.nomFonction if profil else None 

    lst = Evenement.objects.filter(userEvenement = request.user).all()

    return render(request , 'back/evenementRead.html' , {'fonction':fonction, 'lst':lst})