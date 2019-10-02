FROM python:3.7
# App directory
ADD . /app
WORKDIR /app
# Environment setup
COPY .env.example .env
# App dependencies
RUN pip install -r requirements.txt
