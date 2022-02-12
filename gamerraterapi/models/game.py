from django.db import models
from .rating import Rating

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time_to_play = models.IntegerField()
    age_recomendation = models.IntegerField()
    category = models.ManyToManyField("Category", through="Game_Category", related_name="categories")
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

    @property
    # the @property decorator declares that whatever method is defined below, in this case, average_rating. and it
    # can be called as if it is a key on the above Game class. ex: in the front end you could access this by 
    # calling game.average_rating
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        if (len(ratings) > 0):
            total_rating = 0
            for rating in ratings:
                total_rating += rating.rating
            ratings_length = len(ratings)
            return total_rating / ratings_length
        return 0
