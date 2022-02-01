from django.db import models

class Rating(models.Model):
    rating = models.IntegerField()
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    
