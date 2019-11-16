FROM python:{{ cookiecutter.python_version }}

# Label
LABEL maintainer="Sal Anvarov <msalanvarov@gmail.com>"

# App directory
WORKDIR /app

# Copy source files
COPY .. .

# Download dependencies
RUN python3 -m pip install -r requirements.txt

# Expose port
EXPOSE 5000

ENTRYPOINT "entrypoint.sh"
