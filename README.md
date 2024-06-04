
# FastAPI JWT Authentication 

This is an example of a FastAPI application that uses JSON Web Tokens (JWT) for authentication. The application includes user registration, login, and data retrieval functionality.

## Directory Structure

JWT:
- init.py
- jwt_bearer.py
- jwt_handler.py
models:
- model.py
Database/
- database.py
main.py
docker-compose.yaml
Dockerfile
requirements.txt

## Features

* User registration and login functionality
* JWT-based authentication
* Data retrieval using a PostgreSQL database

## Technologies used

* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL

## How to use

1. Clone the repository: `git clone https://github.com/Panchagnulakrishnacharan2703/FastAPI-JWT-Authentication.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Start the application: `docker-compose up`
4. Register a new user: `curl -X POST -H "Content-Type: application/json" -d '{"firstname": "krishna", "lastname": "charan", "email": "charan@example.com", "password": "password"}' http://localhost:8000/user/register`
5. Login and retrieve data: `curl -X POST -H "Content-Type: application/json" -d '{"email": "charan@example.com", "password": "password"}' http://localhost:8000/user/login`

## Docker Compose

The application uses Docker Compose to manage the PostgreSQL database and the FastAPI application. To start the application, run `docker-compose up`.

## Dockerfile

The Dockerfile is used to build the FastAPI application. It installs the required dependencies and sets the environment variables.

## .gitignore

The `.gitignore` file is used to ignore certain files and directories in the repository.

## Note:
 This is just an example and should not be used in production without proper security measures.
