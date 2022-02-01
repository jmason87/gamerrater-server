from unicodedata import category
from django.db import models

class Game_Category(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)