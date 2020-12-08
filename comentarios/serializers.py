from rest_framework import serializers
from comentarios.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Comentario
        fields=('autor', 'fecha_comentario', 'contenido', 'publicacion', 'created')