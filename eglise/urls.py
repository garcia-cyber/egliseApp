from django.urls import path 
from  .views import * 


urlpatterns = [
    path('login/', login , name = 'login') , 
    path('deco/', deco , name = 'deco') , 
    path('panel/', panel , name = 'panel') , 
    path('', home , name ='home') , 
    path('utilisateurAdd/', utilisateurAdd ,  name ='utilisateurAdd') , 
    path('utilisateurRead/', utilisateurRead ,  name ='utilisateurRead') , 
]
