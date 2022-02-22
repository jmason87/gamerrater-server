from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from gamerraterapi.models import Game

class GameTests(APITestCase):
    def setUp(self):
        """
        Create a new Gamer, collect the auth Token, and create a sample GameType
        """

        # Define the URL path for registering a Gamer
        url = '/register'

        # Define the Gamer properties
        gamer = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, gamer, format='json')
        
        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])

        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # SEED THE DATABASE WITH A GAMETYPE
        # This is necessary because the API does not
        # expose a /gametypes URL path for creating GameTypes

        # Create a new instance of GameType
            # game_type = Game_Type()
            # game_type.label = "Board game"

        # Save the GameType to the testing database
            # game_type.save()

    def test_create_game(self):
        """
        Ensure we can create (POST) a new Game.
        """

        # Define the URL path for creating a new Game
        url = "/games"

        # Define the Game properties
        game = {
            "title": "Clue",
            "description": "descripty",
            "designer": "designy",
            "year_released": 6,
            "number_of_players": 1,
            "est_time_to_play": 1,
            "age_recomendation": 1,
            "category": []
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, game, format='json')

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(response.data["title"], game['title'])
        self.assertEqual(response.data["description"], game['description'])
        self.assertEqual(response.data["designer"], game['designer'])
        self.assertEqual(response.data["year_released"], game['year_released'])
        self.assertEqual(response.data["number_of_players"], game['number_of_players'])
        self.assertEqual(response.data["est_time_to_play"], game['est_time_to_play'])
        self.assertEqual(response.data["age_recomendation"], game['age_recomendation'])
        self.assertEqual(response.data["category"], game['category'])

    def test_get_game(self):
        """
        Ensure we can GET an existing game.
        """

        # Create a new instance of Game
        game = Game()
        game.player_id = 1
        game.title = "Monopoly"
        game.description = "descripty"
        game.designer = "designey"
        game.year_released = 5
        game.number_of_players = 4
        game.est_time_to_play = 1
        game.age_recomendation = 2

        # Save the Game to the testing database
        game.save()
        game.category.set([])

        # Define the URL path for getting a single Game
        url = f'/games/{game.id}'

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(response.data["player"]['id'], game.player_id)
        self.assertEqual(response.data["title"], game.title)
        self.assertEqual(response.data["description"], game.description)
        self.assertEqual(response.data["designer"], game.designer)
        self.assertEqual(response.data["year_released"], game.year_released)
        self.assertEqual(response.data["number_of_players"], game.number_of_players)
        self.assertEqual(response.data["est_time_to_play"], game.est_time_to_play)
        self.assertEqual(response.data["age_recomendation"], game.age_recomendation)
        self.assertEqual(response.data["category"], [])

    def test_change_game(self):
        """
        Ensure we can change an existing game.
        """

        # Create a new instance of Game
        game = Game()
        # game.game_type_id = 1
        game.player_id = 1
        game.title = "Sorry"
        game.description = "edit descripty"
        game.designer = "edit designy"
        game.year_released = 4
        game.number_of_players = 1
        game.est_time_to_play = 3
        game.age_recomendation = 2

        # Save the Game to the testing database
        game.save()
        game.category.set([])

        # Define the URL path for updating an existing Game
        url = f'/games/{game.id}'

        # Define NEW Game properties
        new_game = {
            "title": "Sorry",
            "description": "descriptyy",
            "designer": "designyy",
            "year_released": 4,
            "number_of_players": 1,
            "est_time_to_play": 3,
            "age_recomendation": 2,
            "category": []
            
        }

        # Initiate PUT request and capture the response
        response = self.client.put(url, new_game, format="json")

        # Assert that the response status code is 204 (NO CONTENT)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(response.data["player"]['id'], self.token.user_id)
        self.assertEqual(response.data["description"], new_game['description'])
        self.assertEqual(response.data["designer"], new_game['designer'])
        self.assertEqual(
            response.data["year_released"], new_game['year_released'])
        self.assertEqual(
            response.data["number_of_players"], new_game['number_of_players'])
        self.assertEqual(response.data["est_time_to_play"], new_game['est_time_to_play'])
        self.assertEqual(response.data["age_recomendation"], new_game['age_recomendation'])
        self.assertEqual(response.data["category"], new_game['category'])
       
    def test_delete_game(self):
        """
        Ensure we can delete an existing game.
        """

        # Create a new instance of Game
        game = Game()
        game.player_id = 1
        game.description = "Sorry"
        game.designer = "Milton Bradley"
        game.year_released = 5
        game.number_of_players =3
        game.est_time_to_play = 4
        game.age_recomendation = 1

        # Save the Game to the testing database
        game.save()
        game.category.set([])
        
        # Define the URL path for deleting an existing Game
        url = f'/games/{game.id}'

        # Initiate DELETE request and capture the response
        response = self.client.delete(url)

        # Assert that the response status code is 204 (NO CONTENT)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 404 (NOT FOUND)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

