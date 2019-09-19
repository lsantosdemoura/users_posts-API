import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UsersPosts(APIView):
    # TODO: fazer deploy no heroku
    # TODO: adicionar swagger
    def get(self, request, format=None):
        email = request.GET.get('email')
        response_user = requests.get(f'https://jsonplaceholder.typicode.com/users?email={email}')
        response_user_json = response_user.json()
        if response_user_json:
            response_user_json = response_user_json[0]
            user_id = response_user_json.get('id')
            response_posts = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}')
            response_posts_json = response_posts.json()
            [r.pop('userId') for r in response_posts_json]
            response_user_json.update({'posts': response_posts_json})

            return Response(response_user_json)
        else:
            return Response({"email": "This e-mail does not exist."}, status.HTTP_400_BAD_REQUEST)
