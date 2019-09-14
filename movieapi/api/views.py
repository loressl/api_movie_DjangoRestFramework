from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from . models import movie, actor
from .serializers import movieSerializer, actorSerializer
 
# Just wraps a simple HTTP Response to a JSON Response
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)
 
def index(request):
    return HttpResponse("&lt;h3&gt;Welcome to Movie API v1.0&lt;/h3&gt;")
 
@api_view(['GET'])
def movies(request):
    movies = movie.objects.all()
    serializer = movieSerializer(movies, many=True)
    return JSONResponse(serializer.data)
 
@api_view(['GET'])
def actors(request):
    actors = actor.objects.all()
    serializer = actorSerializer(actors, many=True)
    return JSONResponse(serializer.data)