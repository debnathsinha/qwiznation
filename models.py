from google.appengine.ext import ndb

class Quiz(ndb.Model):
    """Models a single quiz"""
    org_id = ndb.StringProperty()
    name = ndb.StringProperty()
    questions = ndb.StringProperty(repeated=True)

class Question(ndb.Model):
    """Models a question"""
    org_id = ndb.StringProperty()
    text = ndb.StringProperty()
    answers = ndb.StringProperty(repeated=True)
    picture_url = ndb.StringProperty()

class Answer(ndb.Model):
    """Answers"""
    text = ndb.StringProperty()
    
