FROM python:{{cookiecutter.python_version}}

# Label
LABEL maintainer="Sal Anvarov <msalanvarov@gmail.com>"

# App directory
WORKDIR /app

# Copy source files
COPY . .

# Download dependencies
RUN python3 -m pip install pipenv

# Setup pipenv
RUN pipenv install

# Expose port
EXPOSE 5000

# Starting web app
CMD pipenv run python manage.py runserver
