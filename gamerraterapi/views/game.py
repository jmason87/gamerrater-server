# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
# from django.core.exceptions import ValidationError
from gamerraterapi.models import Game, Player
from django.db.models import Q




class GameView(ViewSet):
    def list(self, request):
        """SEE CHAPTER 6 IN BOOK 2 LEVEL UP
        Handles GET requests for all games
        Returns:
            Response -- JSON serialized list of games
        """
        search_text = self.request.query_params.get('q', None)      
        games = Game.objects.all()
        # .all() method of the ORM is the same as:
        # SELECT *
        # FROM gamerrater_game
        # games is now a list of games objects
    
        if search_text is not None:
            games=Game.objects.filter(
                Q(title__contains=search_text) |
                Q(description__contains=search_text) |
                Q(designer__contains=search_text)
            )
            
            
        category = request.query_params.get('cat', None)
        # this is saying to look for a query string parameter. In this case the 'cat' specifies what we'll use in the url
        # if 'cat' is not present in the url, it will return None. ex url: http://localhost:8000/games?cat=1
        if category is not None:
                games = games.filter(category_id = category)
        # Here we are saying that if 'cat' is present, or not None, then overwrite games.all from 
        # above to to games.filter. Now it knows to return any game object with the category id = the number we use in the url   
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
        try:
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
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            # if the code inside the try block returns a DoesNotExist, then the server will respond with a 404 message
            # See chapter 6 in book 2 for reference
    def create(self, request):
        """SEE CHAPTER 8 IN BOOK 2 LEVEL UP
        Handles POST operations
        Returns
            Response -- JSON serialized game instance
        """

        player = Player.objects.get(user=request.auth.user)
        # here we are just getting the user that is logged in. we use request.auth.user to get the
        # Player object based on the user.
        serializer = CreateGameSerializer(data=request.data)
        #the data that is held in the request.data is passed to the create serializer
        serializer.is_valid(raise_exception=True)
        # is_valid is called to make sure the client sends valid data, aka making sure what we send from the client matches what
        # we ask for from the serializer
        serializer.save(player=player)
        # if validation is passed, .save will add the game to the database with a new id. Player?
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if everything works as it should a 201 status code is given
    
    def update(self, request, pk):
        """Handles PUT requests"""
        game = Game.objects.get(pk=pk)
        # PUT requests expect the entire object to be sent to the server regardless if a field has been updated.
        # Game.objects.get(pk=pk) is how we grab the object
        serializer = CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        # The rest of the code is the same as the create except we aren't passing anything in the response body (the None) 
        # to Response and a successfull PUT will display a 204 HTTP code
        
    def destroy(self, request, pk):
        """doin the deletes"""
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
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
                  'number_of_players', 'est_time_to_play', 'age_recomendation', 'category', 'player', 'average_rating')
        depth = 1
        # depth allows us to expand foreign key objects similar to a expand query string parameter.
        
class CreateGameSerializer(serializers.ModelSerializer):
    """SEE CHAPTER 8 IN BOOK 2 LEVEL UP"""
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released',
                  'number_of_players', 'est_time_to_play', 'age_recomendation', 'category']
        # On the CreateGameSerializer we do not need to add Player since its coming from the Auth header,
        # it will not be in the request body
    
