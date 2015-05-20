import webapp2
import pdb
import os
import jinja2
import json
from google.appengine.ext import ndb
from pprint import pprint

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
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class Question(ndb.Model):
    text = ndb.StringProperty()
    pic_url = ndb.StringProperty()
    correct_answer = ndb.StringProperty()

class Answer(ndb.Model):
    text = ndb.StringProperty()

class DashboardAdminPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template("dashboard.html")
        self.response.write(template.render())

class QuizListViewPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template("quiz.html")
        self.response.write(template.render())
    def post(self):
        pass

class QuizDetailPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        print quiz_id
        
    def post(self, quiz_id):
        print self.request.get("content")

class NewQuizPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('newquiz.html')
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

    def post(self):
        name = self.request.get('name')
        result = self.request.get('result')
        quiz = Quiz(name=name, result=result)
        quiz.put()

        for i in range(1,QUESTIONS_PER_QUIZ+1):
            question_text = self.request.get('question'+str(i)+'text')
            print question_text
            pic_url = self.request.get('question'+str(i)+'picurl')
            print pic_url
            correct_answer = self.request.get('question'+str(i)+'correctanswer')
            print correct_answer
            if not question_text or not pic_url or not correct_answer:
                break
            question = Question(parent=quiz.key,text=question_text,
                                pic_url=pic_url, correct_answer=correct_answer)
            question.put()
            for j in range(1,5):
                answer_text = self.request.get('answer'+str(i)+str(j)+'text')
                answer = Answer(parent=question.key, text=answer_text)
                if not answer_text:
                    break
                answer.put()
                print answer
        self.redirect('/')

class QuizAPIDetailPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        # Get a particular quiz
        quiz=open('samplequiz.json').read()
        quiz = json.loads(quiz)
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(quiz))

    def post(self, quiz_id):
        # Edit/update an existing quiz
        quiz = json.loads(self.request.body)
        print quiz

class QuizAPIListPage(webapp2.RequestHandler):
    def get(self):
        # Get the previews of all the quizzes
        names = []
        quizzes = Quiz.query().fetch()
        for quiz in quizzes:
            names.push(quiz.name)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(names))

    def post(self, quiz_id):
        # Create a new quiz
        pass        

class QuestionPage(webapp2.RequestHandler):
    def get(self):
        pass

class AnswerPage(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/admin', AdminPage),
    (r'/dashboard', DashboardAdminPage),
    (r'/quiz/new', NewQuizPage),
    (r'/quiz', QuizListViewPage),
    (r'/quiz/(\d+)', QuizDetailPage),
    (r'/api/quiz', QuizAPIListPage),
    (r'/api/quiz/(\d+)', QuizAPIDetailPage),
    (r'/api/question/', QuestionPage),
    (r'/api/answer/', AnswerPage)
], debug=True)
