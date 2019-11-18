# {{cookiecutter.app_name}}

<p align="center">
  <a href="https://palletsprojects.com/p/flask/" target="blank"><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1518503935975/S1_-_WePM.png" width="320" alt="Flask Logo" /></a>
</p>

<p align="center"><a href="https://palletsprojects.com/p/flask/">Flask</a> is a lightweight WSGI web application framework.</p>

[![Build Status](https://travis-ci.org/msanvarov/flask-graphql-mongo-boilerplate.svg?branch=master)](https://travis-ci.org/msanvarov/flask-graphql-mongo-boilerplate)
[![codebeat badge](https://codebeat.co/badges/f8a6a8af-4118-4bfb-b329-e76c1fe4a5a0)](https://codebeat.co/projects/github-com-msanvarov-flask-graphql-mongo-boilerplate-master)

### 📚 Description

This boilerplate leverages the Flask framework to quickly prototype backend applications. It comes with database, logging, security, and authentication features out of the box.

---

### 🍬 Features

- Based on [Flask](https://github.com/pallets/flask).

- GraphQL Framework for Python, [Graphene](https://github.com/graphql-python/graphene). With GraphQL support for Flask in the form of [Flask-GraphQL](https://github.com/graphql-python/flask-graphql).

- [PyJWT](https://github.com/jpadilla/pyjwt) library that allows encoding and decoding JSON Web Tokens (JWT).

- [PyMongo](https://github.com/mongodb/mongo-python-driver), the official Python driver for MongoDB.

- [Faker](https://github.com/joke2k/faker) for generating fake data in migrations.

---

### 🌱 Project Structure

A quick synopsis of the folder structure.

```text
.
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docker-compose.yml
├── manage.py               // flask scripts
├── renovate.json
├── requirements.txt
└── server
    ├── __init__.py
    ├── constants.py        // environment variables from .env file
    ├── resolvers
    │   ├── __init__.py
    │   └── auth.py         // authentication resolver
    ├── schemas
    │   ├── __init__.py
    │   └── profile.py      // profile schema
    ├── tests
    │   ├── __init__.py
    │   └── test_e2e.py     // e2e testing
    └── utils
        ├── __init__.py
        ├── database.py     // database utility functions
        ├── email.py        // email utility functions
        ├── passwords.py    // hashing passwords
        └── webtokens.py    // encrypting/decrypting web tokens
```

### 🛠️ Prerequisites

#### 💻 Non Docker

- Please make sure to have MongoDB locally, or utilize Mongo on the cloud by configuring a cluster in [atlas](https://www.mongodb.com/cloud/atlas). Then grab the connection string and modify the following [line](https://github.com/msanvarov/flask-graphql-mongo/blob/master/.env.example#L6) in the configuration file before copying to the `.env` file.

#### 🐳 Docker

- Please make sure to have docker desktop setup on any preferred operating system to quickly compose the required dependencies. Then follow the docker procedure outlined below.

**Note: Despite the fact that Docker Desktop comes free for both Mac and Windows, it only supports the Pro edition of Windows 10. A common workaround is to get Docker Toolbox which will bypass the Windows 10 Pro restriction by executing Docker in a VM.**

---

### 🚀 Deployment

#### Manual Deployment without Docker

- Create a `.env` file using the `cp .env.example .env` command and replace the existing env variables with preferred settings.

- Install dependencies either with pip or pipenv `pip install -r requirements.txt` or using `pipenv`: `pip install pipenv && pipenv install`

- Start the app in development mode by using `python manage.py runserver` or `pipenv run python manage.py runserver` (the app will be exposed on the port 5000; not to conflict with React, Angular, or Vue)

```bash
# copy .env.example files
$ cp .env.example .env
__
# download dependencies with pip
$ python3 -m pip install -r requirements.txt

# start web server
$ python manage.py runserver
```

#### 🐳 Deploying with Docker

- Execute the following command in-app directory:

```bash
# creates and loads the docker container with required configuration
$ docker-compose up -d
```

- Then the web application, and MongoDB will be available to [http://localhost:5000](http://localhost:5000/), [http://localhost:27017](http://localhost:27017/) respectively.

### 🔒 Environment Configuration

By default, the application comes with a configuration module that can read every environment variable from the `.env` file. The [constants.py file](https://github.com/msanvarov/flask-graphql-mongo/blob/master/constants.py) is responsible for mapping the environment variables to a python dictionary that can be accessed anywhere in the application.

**APP_URL** - the base URL for the application. Made mainly for E2E testing.

**MONGO_URL** - the URL to the MongoDB collection

**MONGO_DB** - the database to store data to

**WEBTOKEN_SECRET_KEY** - the secret key to encrypt/decrypt web tokens with. Make sure to generate a random alphanumeric string for this. Not

**WEBTOKEN_EXPIRATION_TIME** - **the time in seconds** indicating when the web token will expire; by default, it's 2400 seconds which is 40 mins.

**SMTP** - the simple mail transfer protocol url.

**SMTP_PORT** - usually the default standard ports: 25, 587, 465.

**EMAIL_USERNAME** - either username or email to authenticate smtp with.

**EMAIL_PASSWORD** - password to authenticate smtp with.

---

### ✅ Testing

#### 🐳 Docker

Tests can be performed inside the docker container that contains the web application.

```bash
# tests
$ docker exec -it pytest
```

#### Non-Docker

```bash
# e2e tests without pipenv
$ pytest

# e2e tests with pipenv
$ pipenv run pytest
```

---

### 📝 GraphiQL

Out of the box, the web app comes with a GraphiQL which includes a documentation explorer. With the GraphiQL IDE, querying because extremely easy and intuitive.

---

### ✨ PyMongo

PyMongo is a Python distribution containing tools for working with MongoDB. Please refer the [documentation](https://api.mongodb.com/python/current/) for further details.

The configuration for PyMongo can be found in the [model utils](https://github.com/msanvarov/flask-graphql-mongo/blob/master/utils/model.py#L7).

---

### 📃 Logs

This boilerplate comes with integrated logs by werkzeug, the configurations can be found in the [_init_ file](https://github.com/msanvarov/flask-graphql-mongo/blob/master/__init__.py#L8).

---

## License

Flask is [MIT licensed](../LICENSE).

[Author](https://msanvarov.github.io/personal-portfolio/)
