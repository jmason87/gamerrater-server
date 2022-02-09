from django.db import models

class Game_Category(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
# foreign keys on models need to have the model they're coming from referenced,
# thats whats in quotes in what looks like the first parament position. It's the Game class
# on_delete=models.CASCADE will delete the object if the foreign key object is
# deleted somewhere else. 
# example: if a game_category object has a game foreign key and that game object gets
# deleted or removed, and game_category object that uses that foreign key will also be deleted.

