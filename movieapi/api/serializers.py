from rest_framework import serializers
from . models import actor, movie
 
class actorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = actor
        fields = ('__all__')
 
class movieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
 
    class Meta:
        model = movie
        fields = ('__all__')