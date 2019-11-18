#!/usr/bin/env bash

if [[ "{{cookiecutter.open_source_license}}" = "No License" ]]
then
    rm LICENSE
fi

echo "Preparing web application..."
python3 -m pip install pipenv

echo "Fetching dependencies"
pipenv install

echo
echo "Docker has composed the application and is executing at http://localhost:5000."

