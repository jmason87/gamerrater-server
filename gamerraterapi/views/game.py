from unicodedata import category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from gamerraterapi.models import Game, Player


class GameView(ViewSet):
    def list(self, request):
        """SEE CHAPTER 6 IN BOOK 2 LEVEL UP
        Handles GET requests for all games
        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        # .all() method of the ORM is the same as:
        # SELECT *
        # FROM gamerrater_game
        # games is now a list of games objects
        serializer = GameSerializer(games, many=True)
        # passing games to the serializer, many=Trues lets serializer
        # know that this is a list vs. a single object
        return Response(serializer.data)
        # see comment below for return Response

    def retrieve(self, request, pk):
        """SEE CHAPTER 6 IN BOOK 2 LEVEL UP
        Handles GET requests for a single game
        Returns:
            Response -- JSON serialized single game
        """
        game = Game.objects.get(pk=pk)
        # .get() method of the ORM is the same as:
        #     SELECT id, label
        #     FROM gamerraterapi_game
        #     WHERE id = ?
        serializer = GameSerializer(game)
        # passing game to the GameSerializer
        return Response(serializer.data)
        # serializer.data is passed to Response as the Response body
        # Response combines _set_headers and wfile.write functions from book 1.

    def create(self, request):
        """SEE CHAPTER 8 IN BOOK 2 LEVEL UP
        Handles POST operations
        Returns
            Response -- JSON serialized game instance
        """

        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GameSerializer(serializers.ModelSerializer):
    """SEE CHAPTER 6 IN BOOK 2 LEVEL UP
    The serializer class determines how the python data should be
    serialized and sent back to the client"""
    class Meta:
        """Meta holds the configuration for the serializer.
        model is telling it which model to reference, in this case, Game
        and fields are the keys from the model"""
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released',
                  'number_of_players', 'est_time_to_play', 'age_recomendation', 'category')
        depth = 1
        
class CreateGameSerializer(serializers.ModelSerializer):
    """SEE CHAPTER 8 IN BOOK 2 LEVEL UP"""
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released',
                  'number_of_players', 'est_time_to_play', 'age_recomendation', 'category']
    
