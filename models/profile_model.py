from datetime import datetime
from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField, EmailField


class ProfileModel(Document):
    """
    Models a mongo document
    """
    meta = {'collection': 'profiles'}
    username = StringField()
    name = StringField()
    email = EmailField()
    password = StringField()
    created_on = DateTimeField(default=datetime.now)
