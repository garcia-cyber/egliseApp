from django.urls import path 
from  .views import * 


urlpatterns = [
    path('', login , name = 'login') , 
    path('deco/', deco , name = 'deco') , 
    path('panel/', panel , name = 'panel') , 
]
