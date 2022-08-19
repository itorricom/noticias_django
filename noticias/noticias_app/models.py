from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    #activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=900)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="noticialist")
    def __str__(self):
        return self.titulo


