from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'register/login.html')

def signup(request):
    return render(request,'register/signup.html')

def demandeS(request):
    return render(request,'parts/demandeStage.html')

def cahierC(request):
    return render(request,'parts/CahierCharge.html')
