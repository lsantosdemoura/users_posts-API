import json

from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
import pytest


@pytest.fixture
def user_data():
    user_data = {
        "address": {
            "city": "McKenziehaven",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            },
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "zipcode": "59590-4157"
        },
        "company": {
            "bs": "e-enable strategic applications",
            "catchPhrase": "Face to face bifurcated interface",
            "name": "Romaguera-Jacobson"
        },
        "email": "Nathan@yesenia.net",
        "id": 3,
        "name": "Clementine Bauch",
        "phone": "1-463-123-4447",
        "posts": [
            {
                "body": "repellat aliquid praesentium dolorem quo\nsed totam minus non itaque\nnihil labore molestiae sunt dolor eveniet hic recusandae veniam\ntempora et tenetur expedita sunt",
                "id": 21,
                "title": "asperiores ea ipsam voluptatibus modi minima quia sint"
            },
            {
                "body": "eos qui et ipsum ipsam suscipit aut\nsed omnis non odio\nexpedita earum mollitia molestiae aut atque rem suscipit\nnam impedit esse",
                "id": 22,
                "title": "dolor sint quo a velit explicabo quia nam"
            },
            {
                "body": "veritatis unde neque eligendi\nquae quod architecto quo neque vitae\nest illo sit tempora doloremque fugit quod\net et vel beatae sequi ullam sed tenetur perspiciatis",
                "id": 23,
                "title": "maxime id vitae nihil numquam"
            },
            {
                "body": "enim et ex nulla\nomnis voluptas quia qui\nvoluptatem consequatur numquam aliquam sunt\ntotam recusandae id dignissimos aut sed asperiores deserunt",
                "id": 24,
                "title": "autem hic labore sunt dolores incidunt"
            },
            {
                "body": "ullam consequatur ut\nomnis quis sit vel consequuntur\nipsa eligendi ipsum molestiae et omnis error nostrum\nmolestiae illo tempore quia et distinctio",
                "id": 25,
                "title": "rem alias distinctio quo quis"
            },
            {
                "body": "similique esse doloribus nihil accusamus\nomnis dolorem fuga consequuntur reprehenderit fugit recusandae temporibus\nperspiciatis cum ut laudantium\nomnis aut molestiae vel vero",
                "id": 26,
                "title": "est et quae odit qui non"
            },
            {
                "body": "eum sed dolores ipsam sint possimus debitis occaecati\ndebitis qui qui et\nut placeat enim earum aut odit facilis\nconsequatur suscipit necessitatibus rerum sed inventore temporibus consequatur",
                "id": 27,
                "title": "quasi id et eos tenetur aut quo autem"
            },
            {
                "body": "non et quaerat ex quae ad maiores\nmaiores recusandae totam aut blanditiis mollitia quas illo\nut voluptatibus voluptatem\nsimilique nostrum eum",
                "id": 28,
                "title": "delectus ullam et corporis nulla voluptas sequi"
            },
            {
                "body": "odit magnam ut saepe sed non qui\ntempora atque nihil\naccusamus illum doloribus illo dolor\neligendi repudiandae odit magni similique sed cum maiores",
                "id": 29,
                "title": "iusto eius quod necessitatibus culpa ea"
            },
            {
                "body": "alias dolor cumque\nimpedit blanditiis non eveniet odio maxime\nblanditiis amet eius quis tempora quia autem rem\na provident perspiciatis quia",
                "id": 30,
                "title": "a quo magni similique perferendis"
            }
        ],
        "username": "Samantha",
        "website": "ramiro.info"
    }

    return user_data


@pytest.fixture
def invalid_email_response():
    return {"email": "This e-mail does not exist."}


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def valid_email():
    return "Nathan@yesenia.net"


@pytest.fixture
def invalid_email():
    return "test@test.test"


def test_get_valid_email_posts(valid_email, client, user_data):
    response = client.get(reverse('get-posts'), {"email": valid_email})
    assert response.data == user_data
    assert response.status_code == status.HTTP_200_OK


def test_get_invalid_email_posts(invalid_email, client, invalid_email_response):
    response = client.get(reverse('get-posts'), data={"email": invalid_email}, content_type='application/json')
    assert response.data == invalid_email_response
    assert response.status_code == status.HTTP_400_BAD_REQUEST
