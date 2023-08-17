from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from .forms import *

# Create your views here.

def pintores(request):
    contexto = {"pintores": Pintor.objects.all()}
    return render(request, "salute_artist/pintores.html", contexto)

def escritores(request):
    contexto = {"escritores": Escritor.objects.all()}
    return render(request, "salute_artist/escritor.html", contexto)

def musicos(request):
    contexto = {"musicos": Musico.objects.all()}
    return render(request, "salute_artist/musico.html", contexto)




#formularios

def pintorForm(request):
    if request.method == "POST":
        miForm = PintorForm(request.POST)
        if miForm.is_valid():
            pintor_nombre = miForm.cleaned_data.get("nombre")
            pintor_edad = miForm.cleaned_data.get("edad")
            pintor_gmail = miForm.cleaned_data.get("gmail")
            pintor_portfolio = miForm.cleaned_data.get("portfolio")
            pintor = Pintor(nombre=pintor_nombre,
                            edad = pintor_edad,
                            gmail = pintor_gmail,
                            portfolio = pintor_portfolio)
            pintor.save()
            return render(request, "salute_artist/base.html")
    else:
        miForm = PintorForm()

    return render(request, "salute_artist/pintorForm.html", {"form": miForm})

#_____

def musicoForm(request):
    if request.method == "POST":
        miForm = MusicoForm(request.POST)
        if miForm.is_valid():
            musico_nombre = miForm.cleaned_data.get("nombre")
            musico_edad = miForm.cleaned_data.get("edad")
            musico_gmail = miForm.cleaned_data.get("gmail")
            musico_portfolio = miForm.cleaned_data.get("portfolio")
            musico = Musico(nombre=musico_nombre,
                            edad = musico_edad,
                            gmail = musico_gmail,
                            portfolio = musico_portfolio)
            musico.save()
            return render(request, "salute_artist/base.html")
    else:
        miForm = MusicoForm()

    return render(request, "salute_artist/musicoForm.html", {"form": miForm})

#_____

def escritorForm(request):
    if request.method == "POST":
        miForm = EscritorForm(request.POST)
        if miForm.is_valid():
            escritor_nombre = miForm.cleaned_data.get("nombre")
            escritor_edad = miForm.cleaned_data.get("edad")
            escritor_gmail = miForm.cleaned_data.get("gmail")
            escritor_portfolio = miForm.cleaned_data.get("portfolio")
            escritor = Escritor(nombre=escritor_nombre,
                            edad = escritor_edad,
                            gmail = escritor_gmail,
                            portfolio = escritor_portfolio)
            escritor.save()
            return render(request, "salute_artist/base.html")
    else:
        miForm = EscritorForm()

    return render(request, "salute_artist/escritorForm.html", {"form": miForm})




#buscador de BD

def buscarMusico(request):
    return render(request, "salute_artist/buscarMusico.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        musicos = Musico.objects.filter(nombre__icontains=patron)
        contexto = {"musicos": musicos}
        return render(request, "salute_artist/musico.html", contexto)
    return HttpResponse("No se ingreso nada para buscar")

#_____

def buscarEscritor(request):
    return render(request, "salute_artist/buscarEscritor.html")

def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        escritores = Escritor.objects.filter(nombre__icontains=patron)
        contexto = {"escritores": escritores}
        return render(request, "salute_artist/escritor.html", contexto)
    return HttpResponse("No se ingreso nada para buscar")

#_____

def buscarPintor(request):
    return render(request, "salute_artist/buscarPintor.html")

def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        pintores = Pintor.objects.filter(nombre__icontains=patron)
        contexto = {"pintores": pintores}
        return render(request, "salute_artist/pintores.html", contexto)
    return HttpResponse("No se ingreso nada para buscar") 