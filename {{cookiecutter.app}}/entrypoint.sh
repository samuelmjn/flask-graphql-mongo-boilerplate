#!/bin/sh

echo "Waiting for Mongo..."

while ! nc -z mongo 27017; do
  sleep 0.1
done

echo "Mongo Started"

python3 manage.py runserver
