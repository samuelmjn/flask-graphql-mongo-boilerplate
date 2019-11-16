import os
from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='{{cookiecutter.app}}',
    author='msanvarov',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'graphene',
        'python-dotenv',
        'bcrypt',
        'pymongo',
        'pytest',
        'flask_graphql',
        'python-dotenv',
        'faker',
        'flask-script',
        'flask-cors',
        'PyJWT',
        'pymongo',
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.app}} = {{cookiecutter.app}}.manage:runserver'
        ]
    }
)
