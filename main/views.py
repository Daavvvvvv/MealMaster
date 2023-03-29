from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from main.models import dieta
from main.models import comidas
from main.models import comidaDieta
from .forms import idForm

def index(request):
    return render(request, 'index.html', {})


def listarDietas(request):
    dietas = dieta.objects.all()
    return render(request, 'ListarDietas.html', {'dietas': dietas})


def listarAlimentos(request, idDieta):
    comida = mostrarComidas()
    dietas = mostrarDietas()
    nombre = ""
    for i in dietas:
        texto = str(i.nombre)
        if texto == idDieta:
            nombre = texto
            break
    idComidas = []

    dietacomidaquery = comidaDieta.objects.all()

    for i in dietacomidaquery:
        texto = str(i.dieta)
        if texto == idDieta:
            idComidas.append(i.comida)
        else:
            pass

    return render(request, 'DescripcionComidas.html', {'alimentos': idComidas, 'comidas': comida, 'dieta': nombre})


def agregarADieta(request, idDieta):
    idComidas = []
    comidasNoDieta = []
    comida = mostrarComidas()
    dietacomidaquery = comidaDieta.objects.all()
    for i in dietacomidaquery:
        texto = str(i.dieta)
        if texto == idDieta:
            idComidas.append(i.comida)
        else:
            pass

    cont = 0
    for i in comida:
        texto = str(i.nombre)
        for j in idComidas:
            texto1 = str(j.nombre)
            if texto == texto1:
                cont = cont + 1
                break
            else:
                pass
        if cont == 0:
            comidasNoDieta.append(i)
            cont = 0
        else:
            cont = 0

    return render(request, 'agregarComida.html', {'alimentos': comidasNoDieta, 'dieta': idDieta})


def agregarComida(request, idComida, idDieta):
    dietas = mostrarDietas()
    listaComidas = mostrarComidas()
    hola = None
    for i in dietas:
        texto = str(i.nombre)
        if texto == idDieta:
            hola = i.id
            break
    objDieta = dieta.objects.get(id=hola)
    objComida = comidas.objects.get(id=idComida)
    CDInstance = comidaDieta.objects.create(comida=objComida,dieta=objDieta)
    CDInstance.save()
    return render(request, 'comidaAgregada.html', {})


def eliminarAdieta(request, idDieta):
    idComidas = []
    dietacomidaquery = mostrarComidaDieta()

    for i in dietacomidaquery:
        texto = str(i.dieta)
        if texto == idDieta:
            idComidas.append(i.comida)
        else:
            pass

    return render(request, 'eliminarComida.html', {'alimentos': idComidas,'dieta': idDieta})

def eliminarComida(request, idComida, idDieta):
    dietas = mostrarDietas()
    hola = None
    for i in dietas:
        texto = str(i.nombre)
        if texto == idDieta:
            hola = i.id
            break
    CDInstance = comidaDieta.objects.get(comida=idComida,dieta=hola)
    CDInstance.delete()
    print(CDInstance)
    return render(request, 'comidaEliminada.html', {})














def mostrarComidas():
    comida = comidas.objects.all()
    return comida

def mostrarDietas():
    dietas = dieta.objects.all()
    return dietas

def mostrarComidaDieta():
    CD = comidaDieta.objects.all()
    return CD