# Users Posts API
API for consulting a user's posts

---
## REQUIREMENTS
- [docker-compose](https://docs.docker.com/compose/install/)

---

## USAGE
### Run the project
```
$ git clone git@github.com:lsantosdemoura/users_posts-API.git users_posts
$ cd users_posts
# You can build and start docker at once
$ docker-compose up --build
```
#### You can access the image bash:
``` $ docker-compose exec web bash ```
### Run tests
```
$ cd users_posts
$ docker-compose -f test.yml build
$ docker-compose -f test.yml run test_api
```
### For consulting an existing e-mail with [httpie](https://httpie.org/)
```
$ http http://localhost:8000/?email=Sincere@april.biz

HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 2725
Content-Type: application/json
Date: Thu, 19 Sep 2019 04:16:27 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "address": {
        "city": "Gwenborough",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        },
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "zipcode": "92998-3874"
    },
    "company": {
        "bs": "harness real-time e-markets",
        "catchPhrase": "Multi-layered client-server neural-net",
        "name": "Romaguera-Crona"
    },
    "email": "Sincere@april.biz",
    "id": 1,
    "name": "Leanne Graham",
    "phone": "1-770-736-8031 x56442",
    "posts": [
        {
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        },
        {
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
            "id": 2,
            "title": "qui est esse"
        },
        {
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut"
        },
        {
            "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit",
            "id": 4,
            "title": "eum et est occaecati"
        },
        {
            "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque",
            "id": 5,
            "title": "nesciunt quas odio"
        },
        {
            "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae",
            "id": 6,
            "title": "dolorem eum magni eos aperiam quia"
        },
        {
            "body": "dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas",
            "id": 7,
            "title": "magnam facilis autem"
        },
        {
            "body": "dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae",
            "id": 8,
            "title": "dolorem dolore est ipsam"
        },
        {
            "body": "consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas",
            "id": 9,
            "title": "nesciunt iure omnis dolorem tempora et accusantium"
        },
        {
            "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error",
            "id": 10,
            "title": "optio molestias id quia eum"
        }
    ],
    "username": "Bret",
    "website": "hildegard.org"
}
```

### And for an unexisting e-mail
```
$ http localhost:8000/\?email\=test@test.com

HTTP/1.1 400 Bad Request
Allow: GET, HEAD, OPTIONS
Content-Length: 39
Content-Type: application/json
Date: Thu, 19 Sep 2019 04:18:40 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "email": "This e-mail does not exist."
}
```
