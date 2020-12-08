from rest_framework import serializers
from tags.models import Tag

class TagSerializer(serializers.ModelSerializer):
    created= serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        model=Tag
        fields=('nombre', 'created')