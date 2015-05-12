import webapp2
import pdb
import os
import jinja2
from google.appengine.ext import ndb

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

class NewQuizPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('new.html')
        self.response.write(template.render())

class MainPage(webapp2.RequestHandler):
    def get(self):
        quizes = Quiz.query().fetch()
        if quizes:
        	questions = Question.query(ancestor=quizes[0].key).fetch()
        	print questions
        	for question in questions:
        	    answers = Answer.query(ancestor=question.key).fetch()
        	    print answers
        values = { 
            'quizes': quizes,
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

class QuizAPIPage(webapp2.RequestHandler):
    def get(self):
        pass

class QuizPage(webapp2.RequestHandler):
    def get(self, quiz_id):
        print quiz_id
        pass

class QuestionPage(webapp2.RequestHandler):
    def get(self):
        pass

class AnswerPage(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/new', NewQuizPage),
    (r'/api/quiz/', QuizAPIPage),
    (r'/quiz/(\d+)', QuizPage),
    (r'/api/question/', QuestionPage),
    (r'/api/answer/', AnswerPage)
], debug=True)
