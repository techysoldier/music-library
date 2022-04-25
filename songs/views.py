from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Songs
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def song_list(request):
      if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
      product = get_object_or_404(Songs, pk =pk)
      if request.method == 'GET':
        serializer = SongSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
      elif request.method == 'PUT':
        serializer = SongSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      elif request.method =='DELETE':
        song_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)         
