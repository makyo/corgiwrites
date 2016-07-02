import datetime

from corgiwrites import db

class User(db.Document):
    # id = ObjectIDField()
    username = db.StringField(max_length=32)
    password = db.StringField(max_length=50)
    email = db.StringField(max_length=100)
    stories = db.ListField(db.ReferenceField('Story'))

class Story(db.Document):
    # id = ObjectIDField() asdf
    owner = db.ReferenceField('User')
    title = db.StringField(max_length=3000)
    genre = db.StringField(max_length=1000)
    summary = db.StringField(max_length=12000)
    wordcounts = db.ListField(db.EmbeddedDocumentField('WordCountEntry'))
    status = db.StringField(max_length=30)
    submissions = db.ListField(db.EmbeddedDocumentField('Submission'))

class Submission(db.EmbeddedDocument):
    market = db.ReferenceField('Market')
    status = db.StringField(max_length=30)
    date = db.DateTimeField(default=datetime.datetime.now, required=True)

class Market(db.Document):
    # id = ObjectIDField()
    name = db.StringField(max_length=3000)
    url = db.StringField(max_length=4096)
    genre = db.StringField(max_length=1000)
    wordcount = db.IntField()
    is_active = db.BooleanField(default=True)
    expires = db.DateField()

class WordCountEntry(db.EmbeddedDocument):
    wordcount = db.IntField()
    date = db.DateTimeField(default=datetime.datetime.now)
