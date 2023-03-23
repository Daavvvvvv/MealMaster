from django.db import models

class comidas(models.Model):
    nombre = models.TextField(max_length=50)
    calorias= models.IntegerField()
    descripcion= models.TextField(max_length=100000)
    
    def __str__(self):
        return self.nombre


class dieta(models.Model):
    nombre= models.TextField(max_length=1000)
    descripcion= models.TextField(default=0)
    
    
    def __str__(self):
        return self.nombre
    

class comidaDieta(models.Model):
    comida = models.ForeignKey(comidas, on_delete=models.CASCADE)
    dieta = models.ForeignKey(dieta, on_delete=models.CASCADE)
