import webapp2
import pdb
import os
import jinja2
import json
from google.appengine.ext import ndb
from google.appengine.api import images
from pprint import pprint
import urllib2

ROOT_PATH = os.path.dirname(__file__)
GMAILYTICS_TEMPLATE_PATH = os.path.join(ROOT_PATH,"templates") 
JINJA_ENV = jinja2.Environment(
                               loader=jinja2.FileSystemLoader(GMAILYTICS_TEMPLATE_PATH),
                                extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

QUESTIONS_PER_QUIZ = 5

class Quiz(ndb.Model):
    name = ndb.StringProperty()
    result = ndb.StringProperty()
    pic_url = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class Question(ndb.Model):
    text = ndb.StringProperty()
    pic_url = ndb.StringProperty()
    correct_answer = ndb.StringProperty()
    answers = ndb.StringProperty(repeated=True)

class Answer(ndb.Model):
    text = ndb.StringProperty()

class DashboardAdminPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template("dashboard.html")
        self.response.write(template.render())

class QuizListViewPage(webapp2.RequestHandler):
    def get(self):
        quizzes = Quiz.query().fetch()
        template_values = {
            'quizzes' : quizzes
        }
        template = JINJA_ENV.get_template("quiz.html")
        self.response.write(template.render(template_values))

class QuizDetailPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        template_values = {
            'quiz_id': quiz_id
        }
        template = JINJA_ENV.get_template("quiz-tile.html")
        self.response.write(template.render(template_values))

class QuizEditDetailPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        template = JINJA_ENV.get_template("newquiz.html")
        self.response.write(template.render())
        
class NewQuizPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('newquiz.html')
        self.response.write(template.render())

class EmbedPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        template_values = {
            'quiz_id': quiz_id
        }
        template = JINJA_ENV.get_template('embed.html')
        self.response.write(template.render(template_values))
        
class NewQuizTitlePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('newquiz-titlepage.html')
        self.response.write(template.render())
        
class QuizTilePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('quiz-tile.html')
        self.response.write(template.render())        
        
class AdminPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template("quiz.html")
        self.response.write(template.render())

class MainPage(webapp2.RequestHandler):
    def get(self):
        quizzes = Quiz.query().fetch()
        if quizzes:
        	questions = Question.query(ancestor=quizzes[0].key).fetch()
        	print questions
        	for question in questions:
        	    answers = Answer.query(ancestor=question.key).fetch()
        	    print answers
        values = { 
            'quizzes': quizzes,
            'questionsperquiz': range(QUESTIONS_PER_QUIZ)
        }
        template = JINJA_ENV.get_template("index.html")
        self.response.write(template.render(values))

class QuizAPIDetailPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        # Get a particular quiz
        print quiz_id
        quiz_id = int(quiz_id)
        quiz = Quiz.get_by_id(int(quiz_id))
        quiz_response = {}
        quiz_response['name'] = quiz.name
        quiz_response['result'] = quiz.result
        quiz_response['pic_url'] = quiz.pic_url
        questions = Question.query(ancestor=quiz.key).fetch()
        if questions:
            quiz_response['questions'] = []
        for question in questions:
            qn_resp = {}
            qn_resp['text'] = question.text
            qn_resp['pic_url'] = question.pic_url
            qn_resp['correct_answer'] = question.correct_answer
            qn_resp['answers'] = question.answers
            quiz_response['questions'].append(qn_resp)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(quiz_response))

    def post(self, quiz_id):
        # Edit/update an existing quiz
        quiz = json.loads(self.request.body)
        pdb.set_trace()
        print quiz
        qz = Quiz(name = quiz['name'], result = quiz['result'])
        qz.put()
        questions = quiz['questions']
        for question in questions:
            qn = Question(parent=qz.key, text=question['text'],
                          pic_url=question['pictureUrl'],
                          correct_answer=str(question['correctAnswer']))
            answers = question['answers']
            for answer in answers:
                qn.answers.append(answer)
            qn.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(qz.key.id())

class QuizAPIListPage(webapp2.RequestHandler):
    def get(self):
        # Get the previews of all the quizzes
        names = []
        quizzes = Quiz.query().fetch()
        for quiz in quizzes:
            names.append({
                'id': quiz.key.id(),
                'name': quiz.name
            })
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(names))

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        img_url = self.request.get("url")
        try:
            result = urllib2.urlopen(img_url)
            image = result.read()
            width = int(self.request.get("width")) or 320
            height = int(self.request.get("height")) or 320
            image = images.resize(image, width, height)
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(image)
            #pdb.set_trace()
            #print "Result: " + str(result.read())
        except urllib2.URLError, e:
            print e

app = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/admin', AdminPage),
    (r'/dashboard', DashboardAdminPage),
    (r'/quiz/new', NewQuizPage),
    (r'/quiz/title', NewQuizTitlePage),  
    (r'/quiztile', QuizTilePage),
    (r'/quiz/embed/([a-zA-Z0-9]+)', EmbedPage),
    (r'/quiz', QuizListViewPage),
    (r'/quiz/([a-zA-Z0-9]+)/edit$', QuizEditDetailPage),
    (r'/quiz/([a-zA-Z0-9]+)', QuizDetailPage),
    (r'/api/quiz', QuizAPIListPage),
    (r'/api/quiz/([a-zA-Z0-9]+)', QuizAPIDetailPage),
    (r'/img', ImageHandler)
], debug=True)
