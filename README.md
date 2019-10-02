<p align="center">
  <a href="https://palletsprojects.com/p/flask/" target="blank"><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1518503935975/S1_-_WePM.png" width="320" alt="Flask Logo" /></a>
</p>

<p align="center"><a href="https://palletsprojects.com/p/flask/">Flask</a> is a lightweight WSGI web application framework.</p>
<p align="center">
    <a href="https://travis-ci.org/msanvarov/flask-graphql-mongo"><img src="https://travis-ci.org/msanvarov/flask-graphql-mongo.svg?branch=master" alt="Travis" /></a>
</p>
  
### 📚 Description

This boilerplate is made to quickly prototype backend applications. It comes with database, logging, security, and authentication features out of the box.

---

### 🛠️ Prerequisites

#### Non Docker

- Please make sure to have MongoDB locally, or utilize Mongo on the cloud by configuration a cluster in [atlas](https://www.mongodb.com/cloud/atlas). Then grab the connection string and modify the following [line](https://github.com/msanvarov/flask-graphql-mongo/blob/master/.env.example#L5) in the `.env` file.

#### Docker 🐳

- Please make sure to have docker desktop setup on any preferred operating system to quickly compose both the MongoDB and web application. Then follow the steps outlined below.

---

### 🚀 Deployment

#### Manual Deployment without Docker

- Create a .env file using the `$ cp .env.example .env` command and replace the existing env variables with personal settings (MongoDB URL either srv or localhost)

- Install dependencies either with pip or pipenv `pip3 install -r requirements.txt ` or using `pipenv`: `pip install pipenv && pipenv install`

- Start the app in development mode by using `py -3 manage.py runserver` or `pipenv run python manage.py runserver` (the app will be exposed on the port 5000; not to conflict with React, Angular, or Vue)

#### Deploying with Docker 🐳

- Execute the following command in-app directory:

```bash
# creates and loads the docker container with required configuration
$ docker-compose up -d
```

- The following command will set up the project for you (building the Docker images, starting docker-compose stack). The Web application and mongo will be exposed to http://localhost:9000 and http://localhost:27017 respectively

### 🔒 Environment Configuration

By default, the application comes with a config module that can inject the ConfigService and read every environment variable from the .env. file.

**APP_URL** - the base URL for the application. Made mainly for e2e testing.

**MONGO_URL** - the URL to the MongoDB collection

**MOGNO_DB** - the database to store data to

**WEBTOKEN_SECRET_KEY** - the secret key to encrypt/decrypt web tokens with. Make sure to generate a random alphanumeric string for this. Not 

**WEBTOKEN_EXPIRATION_TIME** - **the time in seconds** indicating when the web token will expire; by default, it's 2400 seconds which is 40 mins.

**SMTP** - the simple mail transfer protocol url.

**SMTP_PORT** - usually the default standard ports: 25, 587, 465.

**EMAIL_USERNAME** - either username or email to authenticate smtp with.

**EMAIL_PASSWORD** - password to authenticate smtp with.

---

### ✅ Testing

#### Docker 🐳

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

Out of the box, the web app comes with a graphiQL which includes a documentation explorer.

---

### ✨ Mongoose

Mongoose provides a straight-forward, schema-based solution to model your application data. It includes built-in type casting, validation, query building, business logic hooks and more, out of the box.

---

### 🔊 Logs

This boilerplate comes with integrated logs by werkzeug, the configurations can be found in the [__init__ file](https://github.com/msanvarov/flask-graphql-mongo/blob/master/__init__.py#L8).

---

## License

Flask is [MIT licensed](LICENSE).

[Author](https://msanvarov.github.io/personal-portfolio/)
