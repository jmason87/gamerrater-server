from django.db import models

class GamePicture(models.Model):
    game = models.ForeignKey("Game", on_delete=models.DO_NOTHING, related_name='images')
    pic = models.ImageField(
        upload_to='pictures', height_field=None,
        width_field=None, max_length=None, null=True)

    




    # image_url = models.CharField(max_length=100)
    # player = models.ForeignKey("Player", on_delete=models.CASCADE)
    