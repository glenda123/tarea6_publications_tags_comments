# Create your models here.
from django.db import models

# Create your models here.
class Tag(models.Model):
    nombre=models.CharField(max_length=250)
    created=models.DateTimeField(auto_created=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre