from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time_to_play = models.IntegerField()
    age_recomendation = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

