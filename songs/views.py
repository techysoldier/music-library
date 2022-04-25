from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Songs

@api_view(['GET'])
def song_list(request):
      # if request.method == 'GET':
      #   songs = Songs.objects.all()
      #   serializer = SongSerializer(songs,many=True)
        return Response('ok')