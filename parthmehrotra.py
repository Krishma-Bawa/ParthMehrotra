import webapp2
import jinja2
from Models import TimelineObject

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
	)

timeline = [
	TimelineObject("Drive Ai", "Project Manager", "November 2014 - Present", "Work", "http://google.com", ["Hi", "Bye"])
]

class Timeline(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'

application = webapp2.WSGIApplication([
	('/', Timeline),
], debug=True)
