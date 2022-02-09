from django.db import models

class Review(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    