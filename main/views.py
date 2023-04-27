from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from main.models import comidas, dieta, comidaDieta, rutina, ejercicio, rutinaEjercicio
from .forms import idForm

def index(request):
    return render(request, 'index.html', {})

def listarDietas(request):
    dietas = dieta.objects.all()
    return render(request, 'ListarDietas.html', {'dietas': dietas})

def registro(request):
    return render(request, 'registration/registro')

def listarAlimentos(request, idDieta):
    comida = mostrarComidas()
    dietas = mostrarDietas()
    nombre = ""
    for i in dietas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idDieta:
            nombre = nombreDieta
            break
    idComidas = []

    dietacomidaquery = comidaDieta.objects.all()

    for i in dietacomidaquery:
        nombreDieta = str(i.dieta)
        if nombreDieta == idDieta:
            idComidas.append(i.comida)
        else:
            pass

    return render(request, 'DescripcionComidas.html', {'alimentos': idComidas, 'comidas': comida, 'dieta': nombre})


def agregarADieta(request, idRutina):
    idComidas = []
    comidasNoDieta = []
    comida = mostrarComidas()
    dietacomidaquery = comidaDieta.objects.all()
    for i in dietacomidaquery:
        nombreDieta = str(i.dieta)
        if nombreDieta == idRutina:
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

    return render(request, 'agregarComida.html', {'alimentos': comidasNoDieta, 'dieta': idRutina})


def agregarComida(request, idComida, idDieta):
    dietas = mostrarDietas()
    listaComidas = mostrarComidas()
    dietaID = None
    for i in dietas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idDieta:
            dietaID = i.id
            break
    objDieta = dieta.objects.get(id=dietaID)
    objComida = comidas.objects.get(id=idComida)
    CDInstance = comidaDieta.objects.create(comida=objComida,dieta=objDieta)
    CDInstance.save()
    return render(request, 'comidaAgregada.html', {})


def eliminarAdieta(request, idDieta):
    idComidas = []
    dietacomidaquery = mostrarComidaDieta()

    for i in dietacomidaquery:
        nombreDieta = str(i.dieta)
        if nombreDieta == idDieta:
            idComidas.append(i.comida)
        else:
            pass

    return render(request, 'eliminarComida.html', {'alimentos': idComidas,'dieta': idDieta})

def eliminarComida(request, idComida, idDieta):
    dietas = mostrarDietas()
    dietaID = None
    for i in dietas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idDieta:
            dietaID = i.id
            break
    CDInstance = comidaDieta.objects.get(comida=idComida,dieta=dietaID)
    CDInstance.delete()
    print(CDInstance)
    return render(request, 'comidaEliminada.html', {})


def listarRutinas(request):
    rutinas = mostrarRutinas()
    return render(request, 'ListarRutinas.html', {'rutinas': rutinas})

def listarEjercicios(request, idRutina):
    ejercicios = mostrarEjercicios()
    rutinas = mostrarRutinas()
    nombre = ""
    for i in rutinas:
        nombreRutina = str(i.nombre)
        if nombreRutina == idRutina:
            nombre = nombreRutina
            break
    idEjercicio = []

    RD = mostrarEjercicioRutina()

    for i in RD:
        objectRutina = i.rutina
        nombreRutina = objectRutina.nombre
        if nombreRutina == idRutina:
            
            idEjercicio.append(i.ejercicio)
        else:
            pass

    return render(request, 'DescripcionEjercicios.html', {'ejercicios': idEjercicio, 'ejercicioNombre': ejercicios, 'rutina': nombre})

def agregarARutina(request, idRutina):
    idEjercicios = []
    ejerciciosNoRutina = []
    ejercicios = mostrarEjercicios()
    RD = mostrarEjercicioRutina()
    for i in RD:
        objectRutina = i.rutina
        nombreRutina = objectRutina.nombre
        if nombreRutina == idRutina:
            idEjercicios.append(i.ejercicio)
        else:
            pass
    cont = 0
    for i in ejercicios:
        texto = str(i.nombre)
        for j in idEjercicios:
            texto1 = str(j.nombre)
            if texto == texto1:
                cont = cont + 1
                break
            else:
                pass
            if cont == 0:
                ejerciciosNoRutina.append(i)
                cont = 0
            else:
                cont = 0
    

    return render(request, 'agregarEjercicio.html', {'ejercicios': ejerciciosNoRutina, 'rutina': idRutina})

def agregarEjercicio(request, idEjercicio, idRutina):
    rutinas = mostrarRutinas()
    rutinaID = None
    for i in rutinas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idRutina:
            rutinaID = i.id
            break
    objRutina = rutina.objects.get(id=rutinaID)
    objEjercicio = ejercicio.objects.get(id=idEjercicio)
    RDInstance = rutinaEjercicio.objects.create(ejercicio=objEjercicio,rutina=objRutina)
    RDInstance.save()
    return render(request, 'ejercicioAgregado.html', {})

def eliminarARutina(request, idRutina):
    idEjercicios = []
    RD = mostrarEjercicioRutina()

    for i in RD:
        objectRutina = i.rutina
        nombreRutina = objectRutina.nombre
        if nombreRutina== idRutina:
            idEjercicios.append(i.ejercicio)
        else:
            pass

    return render(request, 'eliminarEjercicio.html', {'ejercicios': idEjercicios,'rutina': idRutina})


def eliminarEjercicio(request, idEjercicio, idRutina):
    rutinas = mostrarRutinas()
    rutinaID = None
    for i in rutinas:
        nombreRutina = str(i.nombre)
        if nombreRutina == idRutina:
            rutinaID = i.id
            break
    RDInstance = rutinaEjercicio.objects.get(ejercicio=idEjercicio,rutina=rutinaID)
    RDInstance.delete()
    print(RDInstance)
    return render(request, 'ejercicioEliminado.html', {})



def mostrarComidas():
    comida = comidas.objects.all()
    return comida

def mostrarDietas():
    dietas = dieta.objects.all()
    return dietas

def mostrarComidaDieta():
    CD = comidaDieta.objects.all()
    return CD

def mostrarEjercicios():
    ejercicios = ejercicio.objects.all()
    return ejercicios

def mostrarRutinas():
    rutinas = rutina.objects.all()
    return rutinas

def mostrarEjercicioRutina():
    RD = rutinaEjercicio.objects.all()
    return RD