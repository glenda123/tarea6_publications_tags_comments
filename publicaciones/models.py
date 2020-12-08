from django.db import models

# Create your models here.
from tags.models import Tag

# Create your models here.
class Publicacion(models.Model):
    autor=models.CharField(max_length=200)
    fecha_publicacion=models.DateField()
    contenido=models.CharField(max_length=8000)
    tags=models.ManyToManyField(Tag, related_name='publicaciones')
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.contenido