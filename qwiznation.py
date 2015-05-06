import webapp2
import os
import jinja2

ROOT_PATH = os.path.dirname(__file__)
GMAILYTICS_TEMPLATE_PATH = os.path.join(ROOT_PATH,"templates") 
JINJA_ENV = jinja2.Environment(
                               loader=jinja2.FileSystemLoader(GMAILYTICS_TEMPLATE_PATH),
                                extensions=['jinja2.ext.autoescape'],
                                autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template("index.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
