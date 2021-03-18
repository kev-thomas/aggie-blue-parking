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

### User Login Testing

Temporary secret: `"secret"`

algorithm: `"HS256"`

Payload should look like this:

	payload = {"username": "john", "password":"secret"}

using PyJWT you can encode it like this: (note: I added a user with those credentials so you can actually test it)

	encoded_jwt = jwt.encode({"username": "john", "password":"secret"}, "secret", algorithm="HS256")

To make a request (POST):

	header = {
		Content-Type: application/json
		Authentication: <JWT token here>
	}
	
Leave the body empty

Make a `POST` request to `localhost:8000/genie/login`

Answer should look like this if auth successful:

	code 200
	{
		token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im90aGVyIiwicGFzc3dvcmQiOiIxMjM0NSJ9.V0BXwNldF53fI8peQE_vkyK5kH44V5tCuzs557SfPp4"
	}

If not successful:

	code 401
	Unauthorized

## System testing instructions:

The whole components that make up the system include:

- Python Server Backend 
- Javascript and HTML / CSS front end
- The SQLite database
- Web Browser

In order to test the whole system, we must run all implemented requirements test in several browsers, in different screen sizes, as well as on the `http://locahost:8000` and using the local IP address of the server.

## Other development notes, as needed:

None so far
