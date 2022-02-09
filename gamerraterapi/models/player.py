from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    
# user is a built in class from django that can be accessed. It inclused basic user keys
# like name, username, password, etc.
