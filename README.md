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
	|
	|__Client/
	|
	|__Server/

__Description__

The back-end development should be done in the Server directory, this is where the API will be developed along with the database management. All authorisation should also be processed in the backend for security purposes.

The Front end should be developed in the Client directory and provide all the forms and pages to be loaded by the client side browser.

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

For the front end we will use the [vue](https://vuejs.org/) framework on javascript.

__Back end:__

For the back end we will use [djando](https://www.djangoproject.com/) framework for python. We will be using python3.6 or above.

__Database:__

Django uses [SQLite](https://www.sqlite.org/index.html) by default and we will be using it on this project.

__Setup:__

This project is quite simple to run in the linux terminal:

`$ cd <project directory>/`
`$ python manage.py runserver`

The server should be up and running at:

`http://localhost:8000`

To login as an admin:

`http://localhost:8000/admin/`

## Build instructions

make sure you have python 3.5 or higher
`$ pip install django`
`$ git clone git@github.com:andrewjouffray/group9-project.git`

## Unit testing instruction:

Each endpoint of the apis in the back end must be individually tested using the [postman](https://www.postman.com/) app.

Functionality to test:

- 

## System testing instructions:

Not sure yet

## Other development notes, as needed:

None so far
