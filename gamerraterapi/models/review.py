from django.db import models

class Review(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    