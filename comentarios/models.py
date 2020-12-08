from django.db import models

# Create your models here.
from publicaciones.models import Publicacion
# Create your models here.
class Comentario(models.Model):
    autor=models.CharField(max_length=200)
    fecha_comentario=models.DateField()
    contenido=models.CharField(max_length=2000)
    publicacion=models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.contenido