from django.shortcuts import render  , redirect 
from django.contrib.auth import authenticate , login as auth , logout 
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.contrib.auth.models import User

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

    userCount = User.objects.count()

    return render(request, 'back/index.html', {'userCount': userCount}) 

# ============================================================
# add employe 
# =============================================================
@login_required()
def utilisateurAdd(request):
    msg = None 
    if request.method == 'POST':
        form = UtilisateurForm(request.POST) 
        if form.is_valid():
            form.save() 
            msg = "information enregistre"
    
    form = UtilisateurForm()
    return render(request, 'back/employeAdd.html', {'form':form, 'msg': msg}) 