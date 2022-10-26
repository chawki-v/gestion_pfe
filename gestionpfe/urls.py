from django.urls import path
from . import views

app_name="gestionpfe"
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('DemandeStage/',views.demandeS,name='demandeS'),
    path('CahierCharge/',views.cahierC,name='demandeC'),

]
