from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import Rating, Player

class RatingView(ViewSet):
    def list (self, request):
        """handes GET all"""
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """handles GET single"""
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    def create(self, request):
        """handles POST"""
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'game', 'player')
        depth = 1
        
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'game')