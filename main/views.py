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

def listarAlimentos(response):
    idComidas = []
    alimentos = comidas.objects.all()
    form = idForm()
    if response.method == 'POST':
        form = idForm(response.POST)
        if form.is_valid():
            x = form.cleaned_data['idDieta']  
            dietacomidaquery = comidaDieta.objects.all()
            #idComidas = []
            for idDieta in dietacomidaquery:
                texto = str(idDieta.dieta)
                if texto == x:
                    idComidas.append(idDieta.comida)
                else:
                    pass
    
            


    return render(response, 'DescripcionComidas.html', {'alimentos': idComidas, 'form': form})

#def verDieta(request, dieta_id):
    #verDieta= get_object_or_404(dieta, id= dieta_id)
    #context = {'verDieta': verDieta}
    #return render(request, 'DescripcionComidas.html', context)


'''
form = idForm()
    if response.method == 'POST':
        form = idForm(response.POST)
        if form.is_valid():
            pass
, 'form': form
'''