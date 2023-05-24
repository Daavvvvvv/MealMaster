from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from main.models import comidas, dieta, comidaDieta, rutina, ejercicio, rutinaEjercicio
from .forms import preguntas, CustomUserCreationForm
import openai
openai.api_key = "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"

def index(request):
    return render(request, 'index.html', {})

def listarDietas(request):
    dietas = dieta.objects.all()
    return render(request, 'ListarDietas.html', {'dietas': dietas})

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }
    return render(request, 'registration/registro.html', data)

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


def agregarADieta(request, idDieta):
    idComidas = []
    comidasNoDieta = []
    comida = mostrarComidas()
    dietacomidaquery = comidaDieta.objects.all()
    for i in dietacomidaquery:
        nombreDieta = str(i.dieta)
        if nombreDieta == idDieta:
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
                if i in ejerciciosNoRutina:
                    cont = 0
                else:
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
        if nombreRutina == idRutina:
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


def preguntaChat(request, respuesta):
    texto = ''
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = preguntas(request.POST)
        # check whether it's valid:
        if form.is_valid():
            texto = form.cleaned_data
            respuesta1 = texto['pregunta']
            print(texto['pregunta'])
            messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
            message = respuesta1
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )

            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            messages.append({"role": "assistant", "content": reply})
            return render(request, "preguntaChat.html",{"form": form, "ejemplo": reply})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = preguntas()

    return render(request, "preguntaChat.html",{"form": form, "ejemplo": texto})

def chatGPT(request, pregunta):
    print(pregunta)
    return render(request, "chat.html", {"chat": pregunta})

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