# Welcome to Big Blue Parking Genie

## Description
Big Blue Parking Genie is a web application that allows parking space owner to coordinate with a university employed supervisor to provide and rent out parking spaces during events and games. The application will also allow users to find and purchase the parking space provided by the owners. 
 
### Team members:

-	Andrew Jouffray - (Back-end development)
-	Kevin Thomas - (Front-end development)
-	Sarah Jones - (Back-end development)
-	Spencer Hanson - (Scrum master & Front-end development)

### Ogranisation of the repo:

__directory organization__

	__README.md
	|__docs/
	|  |_usecases/
	|__front/        <--------- Front End
	|  |_README.md   <--------- Front End instructions
	|__parking/      <--------- Back end
	   |__db.sqlite3
	   |__genie/     <--------- App Directory
	   |  |_admin.py
	   |  |_apps.py
	   |  |_ __init__.py
	   |  |_migrations/
	   |  |_models.py
	   |  |_tests.py
	   |  |_urls.py
	   |  |_views.py
	   |  |_templates/
	   |__parking/     <-------- Website configuration
	      |_asgi.py
	      |_ __init__.py
	      |_settings.py
	      |_urls.py
	      |_wsgi.py

__Description__

The Directory structure follows the basic template of a django project with the  `parking/` directory being the parent of the application directory `genie/`. The majority of the backend development will take place in the `genie/` directory and the front end development will de saved in the `genie/templates/genie/` directory.

The `parking/parking/` directory is where the configuration files and primary router files for the website will be saved.

## Version control procedures:

__General procedure__
- clone the repo `git clone git@github.com:andrewjouffray/group9-project.git`
- Always `git pull` before working
- Avoid working on the same file at the same time
- Avoid commiting broken code
- good english grammar is completely optional

__Commit & push procedure__
- In the proper directory `git add .`
- Write meaningful commit message `git commit -m "<message>"`
- `git push`

## Tool stack description and setup procedure

__Front end:__

For the front end we will use the [Vue](https://vuejs.org/) framework on javascript.

__Back end:__

For the back end we will use [Djando](https://www.djangoproject.com/) framework for python. We will be using python3.6 or above.

__Database:__

Django uses [SQLite](https://www.sqlite.org/index.html) by default and we will be using it on this project.

__Setup:__

This project is quite simple to run in the linux terminal:

`$ cd <project root directory>/`

`$ python manage.py runserver`

The server should be up and running at:

`http://localhost:8000/genie`

To login as an admin:

`http://localhost:8000/admin/`

## Build instructions

make sure you have python 3.6 or higher

`$ pip install -r requirements.txt`

`$ git clone git@github.com:andrewjouffray/group9-project.git`

__Note: When making changes to the models, update the database by:__

	$ cd <project root directory>/
	$ python manage.py makemigartions
	$ python manage.py migrate

## Unit testing instruction:

Each endpoint of the apis in the back end must be individually tested using the [Postman](https://www.postman.com/) app.

### User Login

Make a `POST` request to `localhost:8000/genie/login`

	header = {
		Content-Type: application/json
	}

	body ={

		"username": "john", 
		"password":"secret"
	}
	
Answer should look like this if auth successful:

	code 200
	{
		token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im90aGVyIiwicGFzc3dvcmQiOiIxMjM0NSJ9.V0BXwNldF53fI8peQE_vkyK5kH44V5tCuzs557SfPp4"
	}

Temporary secret: `"secret"`

algorithm: `"HS256"`

If not successful:

	code 401
	Unauthorized

### User registration

Make a `POST` request to `localhost:8000/genie/register`

	header = {
		Content-Type: application/json
	}

	body ={

		"firstname": "name",
		"lastname": "lastname",
		"email": "email",
		"username": "john", 
		"password":"secret",
		"renter": True / False,
		"owner": True / False
	}
	
Answer should look like this if registration successful:

	code 200 OK

If not successful:

	code 409 Conflict

### Get all events

Make a `GET` request to `localhost:8000/genie/allevents`

	header = {
		Content-Type: application/json,
		Authorization: <token from login answer here> 
	}

Answer should look like this if auth successful:

	code 200

`pk` is the id

```
{
    "events": [
        {
            "model": "genie.event",
            "pk": 1,
            "fields": {
                "title": "Fun Party at billy's",
                "date": "2021-03-26",
                "time": "18:00:00",
                "streetAddress": "123 W 342 S",
                "city": "Logan",
                "zip": "84321"
            }
        },
        {
            "model": "genie.event",
            "pk": 3,
            "fields": {
                "title": "organic food market",
                "date": "2021-04-05",
                "time": "18:00:00",
                "streetAddress": "231 W 423 N",
                "city": "Logan",
                "zip": "84321"
            }
        },
        {
            "model": "genie.event",
            "pk": 2,
            "fields": {
                "title": "Charity activity 1",
                "date": "2021-04-21",
                "time": "12:00:00",
                "streetAddress": "old main room 342",
                "city": "Logan",
                "zip": "84321"
            }
        }
    ],
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJwZXJtaXNzaW9ucyI6MSwiZXhwIjoxNjE3OTIyOTc1fQ.xf6WSVlODnB7D0eQbllCsn9gvOZ0pQJbrbur2qWaDaY"
}

```

Temporary secret: `"secret"`

algorithm: `"HS256"`

If not successful:

	code 401
	Unauthorized


### Get all parking spots purchased by a user (OUTDATED use the endpoint below it)

Make a `GET` request to `localhost:8000/genie/rentals`

	header = {
		Content-Type: application/json,
		Authorization: <token from login answer here> 
	}

Answer should look like this if auth successful:

	code 200
	{
    	"spots": [
        	{
            		"streetAddress": "3432 East",
            		"city": "logan",
            		"zip": "84321",
            		"price": 4,
            		"distance": 3,
            		"available": false,
            		"owner": [
                		5
            		],
            		"renter": [
                		6
            		]
        	},
        	{
            		"streetAddress": "423 yeet street",
            		"city": "logan",
            		"zip": "84321",
            		"price": 5,
            		"distance": 2,
            		"available": false,
            		"owner": [
                		2
            		],
            		"renter": [
                		6
            		]
        	}
    	],
    	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJwZXJtaXNzaW9ucyI6MSwiZXhwIjoxNjE2NzA1NTk0fQ.8WAqWW0x0tONsF8jIVhmEtvWkqE81k26K7d7TGOWcyI"
	}
If not successful:

	code 401
	Unauthorized

### Get user details

Make a `GET` request to `http://localhost:8000/genie/getUserDetail`

header:


        header = {
                Content-Type: application/json,
                Authorization: <token from login answer here> 
        }


Answer:

```
{
    "user": {
        "username": "Rich",
        "firstName": "Mr owner",
        "lastName": "Rich",
        "email": "ok@email.com",
        "money": 95
    },
    "rentals": [
        {
            "streetAddress": "423 yeet street",
            "city": "logan",
            "zip": "84321",
            "date": "2021-06-21"
        }
    ],
    "owner": true,
    "owned": [
        {
            "streetAddress": "3432 East",
            "city": "logan",
            "zip": "84321",
            "price": 4
        }
    ]
}
```

### Get details of an event and available parking spots 

Make a `GET` request to `http://localhost:8000/genie/event/<event id>`

	header = {
		Content-Type: application/json,
		Authorization: <token from login answer here> 
	}

Answer should look like this if auth successful:

	code 200
	{
    	"event_details": {
        	"title": "FootballGame",
        	"date": "2021-05-19",
        	"time": "16:14:20",
        	"streetAddress": "Stadium",
        	"city": "Logan",
        	"zip": "84321",
        	"id": 5
    	},
    	"available_spots": [
        	{
            	"address": "next to dennys",
            	"city": "logan",
            	"zip": "84321",
            	"price": 5,
            	"id": 5
        },
        {
            	"address": "4563 blvd",
            	"city": "logan",
            	"zip": "84321",
            	"price": 6,
            	"id": 3
        	},
        	{
            	"address": "3432 East",
            	"city": "logan",
            	"zip": "84321",
            	"price": 4,
            	"id": 6
        },
        {
            	"address": "123 E 456 N",
            	"city": "logan",
            	"zip": "84321",
            	"price": 6,
            	"id": 1
        },
        {
            	"address": "423 yeet street",
            	"city": "logan",
            	"zip": "84321",
            	"price": 5,
            	"id": 7
        }
    	],
    		"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJwZXJtaXNzaW9ucyI6MSwiZXhwIjoxNjE3OTIyOTc1fQ.xf6WSVlODnB7D0eQbllCsn9gvOZ0pQJbrbur2qWaDaY"
	}
If not successful:

	code 401
	Unauthorized

### Rent a spot:

Make a `POST` request to `http://localhost:8000/genie/makeRental`

	header = {
		Content-Type: application/json,
		Authorization: <token from login answer here> 
	}

	body = {
    		eventId": "id",
    		"spotId": "id",
    		"userId": "id"
	}

Answer should look like this if auth successful:

	code 200
	{
		"message": "success",
		"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvaG4iLCJwZXJtaXNzaW9ucyI6MSwiZXhwIjoxNjE3OTIyOTc1fQ.xf6WSVlODnB7D0eQbllCsn9gvOZ0pQJbrbur2qWaDaY"

	}

If not successful:

	code 401
	Unauthorized

If not enough money:

	code 409
	{
    		"message": "not enough money"
	}

### create parking request

Make a `POST` to `http://localhost:8000/genie/createParking`

	header= {
     		"Content-Type": "application/json",
     		"Authorization": <insert token from login answer here>,
	}

	body= {
     		"streetAddress": "a street",
    		"city": "Logan",
    		"zip": 84341,
    		"price": 10
	}

## System testing instructions:

The whole components that make up the system include:

- Python Server Backend 
- Javascript and HTML / CSS front end
- The SQLite database
- Web Browser

In order to test the whole system, we must run all implemented requirements test in several browsers, in different screen sizes, as well as on the `http://locahost:8000` and using the local IP address of the server.

## Other development notes, as needed:

None so far
