from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import GamePicture, Player
from gamerraterapi.models.game import Game
from django.core.files.base import ContentFile
import uuid
import base64

class ImageView(ViewSet):
    def list (self, request):
        """handes GET all"""
        game_pictures = GamePicture.objects.all()
        serializer = GamePictureSerializer(game_pictures, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """handles GET single"""
        game_picture = GamePicture.objects.get(pk=pk)
        serializer = GamePictureSerializer(game_picture)
        return Response(serializer.data)

    def create(self, request):
        """handles POST"""
        game = Game.objects.get(pk=request.data['gameId'])
        # player = Player.objects.get(user=request.auth.user)


        format, imgstr = request.data["image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), 
                           name=f'{request.data["gameId"]}-{uuid.uuid4()}.{ext}')

        
        image = GamePicture.objects.create(
            game = game,
            pic = data
        )
        serializer = CreateGamePictureSerializer(image)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        """doin the deletes"""
        img = GamePicture.objects.get(pk=pk)
        img.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class GamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ('id', 'game', 'pic')
        
class CreateGamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ('id', 'game', 'pic')

