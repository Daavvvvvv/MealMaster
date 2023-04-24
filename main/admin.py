from django.contrib import admin
from .models import comidas, dieta, comidaDieta, rutina, ejercicio, rutinaEjercicio
# Register your models here.


admin.site.register(comidas)
admin.site.register(dieta)
admin.site.register(comidaDieta)
admin.site.register(rutina)
admin.site.register(ejercicio)
admin.site.register(rutinaEjercicio)