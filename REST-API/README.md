## Running the app locally

install django rest framework and django rest JWT.

`➜  REST-API git:(master) ✗ pip3 install djangorestframework markdown django-filter djangorestframework_simplejwt`

After installation


`➜  REST-API git:(master) ✗ python3 manage.py migrate`

`➜  REST-API git:(master) ✗ python3 manage.py runserver`


Example
-------

open your postman and make a post request to http://localhost:8000/account/ootsuk/register

```json
{
    "first_name":"Abdessamad",
    "last_name":"Bensaad",
    "username":"B3ns44d3",
    "password":"1234B3ns44d",
    "email":"b3ns44d@email.com"
}
```
You will get something like this 
```json
{
    "user": {
        "id": 10,
        "password": "pbkdf2_sha256$216000$nkTeP66vbhww$XcXGQxrvUQYrr8ehF4kHoxzGCoMkSqUDfHKq5zox2ac=",
        "last_login": null,
        "is_superuser": false,
        "username": "B3ns44d3",
        "first_name": "Abdessamad",
        "last_name": "Bensaad",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-02-02T08:57:54.950479Z",
        "groups": [],
        "user_permissions": []
    },
    "message": "User Created Successfully.  Now perform Login to get your token"
}
```

Now after registration, Just login to get the JWT token. Now you can make request to the server with that token. To login, make a post request to http://localhost:8000/ootsuk/token/

```json
{
    "username":"B3ns44d3",
    "password":"1234B3ns44d"
}
```