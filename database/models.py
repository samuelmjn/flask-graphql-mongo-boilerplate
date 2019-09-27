from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField, EmailField


class Profile(Document):
    meta = {'collection': 'profiles'}
    username = StringField()
    name = StringField()
    email = EmailField()
    password = StringField()
    created_on = DateTimeField(default=datetime.now)
