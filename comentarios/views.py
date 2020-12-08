from comentarios.models import Comentario
from publicaciones.models import Publicacion
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import PublicacionSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class=ComentarioSerializer
    
    @action(methods=['GET'], detail=True)
    def publicacion(self, request, pk=None):
        
        comentario= self.get_object()
        serialized= PublicacionSerializer(comentario.publicacion)
        return Response(status=status.HTTP_200_OK, data=serialized.data)


