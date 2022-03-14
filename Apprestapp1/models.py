from distutils.command.upload import upload
from ssl import Options
from django.db import models 
from django.contrib.auth.models import User

class Restaurant(models.Model):
    nombre= models.CharField('nombre',max_length=40) #titulo
    categoria = models.CharField('categoria',max_length=50) #subtitulo
    informacion = models.CharField('informacion',max_length=1000) #cuerpop
    propietario = models.CharField('propietario',max_length=40)#autor
    fecha = models.DateField('fecha',auto_now_add=True,auto_now=False,blank=True)#fecha
    imagen = models.ImageField(null=True, blank=True,upload_to='imagenes', default="placeholder.png")#imagen

    def __str__(self):
        return f'{self.nombre} {self.categoria} - {self.informacion} - {self.propietario} - {self.fecha}'

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
    ]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models. EmailField ()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def _str_(self):
        return self. nombre
