import webapp2
import os
import jinja2
from google.appengine.ext import ndb

ROOT_PATH = os.path.dirname(__file__)
GMAILYTICS_TEMPLATE_PATH = os.path.join(ROOT_PATH,"templates") 
JINJA_ENV = jinja2.Environment(
                               loader=jinja2.FileSystemLoader(GMAILYTICS_TEMPLATE_PATH),
                                extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class Quiz(ndb.Model):
    name = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        quizes = Quiz.query().fetch()
        values = { 
            'quizes': quizes
        }
        template = JINJA_ENV.get_template("index.html")
        self.response.write(template.render(values))

    def post(self):
        quiz = Quiz(name=self.request.get('message'))
        quiz.put()
        self.redirect('/')

class QuizPage(webapp2.RequestHandler):
    def get(self):
        pass

class QuestionPage(webapp2.RequestHandler):
    def get(self):
        pass

class AnswerPage(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/api/quiz/', QuizPage),
    (r'/api/question/', QuestionPage),
    (r'/api/answer/', AnswerPage)
], debug=True)
