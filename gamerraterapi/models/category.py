from django.db import models  ## models import from django

class Category(models.Model):
    title = models.CharField(max_length=50)
    
# your class will list the keys the each instance will have on it.
# Link to django models overview:
# https://docs.djangoproject.com/en/3.2/topics/db/models/
# Reference chapter 2 from book 2 (Level Up)

# once your models are ready, run the following command:
#   python3 manage.py makemigrations <api_name>
# the above command created the migrations, now run this to create the tables:
#   python3 manage.py migrate
# if everything worked properly, you should have tables in your sqlite explorer
