from rest_framework import serializers
from publicaciones.models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Publicacion
        fields=('autor', 'fecha_publicacion', 'contenido', 'tags', 'created')