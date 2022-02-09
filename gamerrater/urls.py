"""gamerrater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from gamerraterapi.views import register_user, login_user
from rest_framework import routers
from gamerraterapi.views import GameView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
# DefaultRouter is a built in class in Django Rest, it sets up the resource
# for each method this is present on the view
# trailing_slash tells the router to accept /games instead of /games/
# SEE CHAPTER 6 IN BOOK 2 LEVEL UP
router.register(r'games', GameView, 'game')
# the first pararmeter r'games' sets up the url
# the second parameter GameView tells the server which view to use when it sees /games
# The third parameter 'game' is called the base name. It acts as a nickname and
# you'll really only see it in errors. Typically the singular of the plural r'url'
# SEE CHAPTER 6 IN BOOK 2 LEVEL UP
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] 