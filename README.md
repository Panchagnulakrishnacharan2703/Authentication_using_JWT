
# FastAPI JWT Authentication 

This is an example of a FastAPI application that uses JSON Web Tokens (JWT) for authentication. The application includes user registration, login, and data retrieval functionality.

## Directory Structure

Autehtication/
    JWT/
        ├── jwt_bearer.py        # Handles JWT token extraction and validation from requests.
        └── jwt_handler.py        # Contains logic for creating and manipulating JWT tokens.
    models/
        └── model.py              # Defines the structure of your database entities.
    Database/
        └── database.py             # Logic for connecting and interacting with the database.
    main.py                     # The main entry point for your application.
    docker-compose.yaml         # Configuration file for Docker Compose.
    Dockerfile                   # Defines how to build the Docker image.
    requirements.txt             # Text file listing project dependencies.


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
