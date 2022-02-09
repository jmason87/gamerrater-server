from django.db import models

class Image(models.Model):
    image_url = models.CharField(max_length=100)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    