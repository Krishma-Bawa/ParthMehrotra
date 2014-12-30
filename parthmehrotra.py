import webapp2

class Timeline(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('TIMELINE')

application = webapp2.WSGIApplication([
	('/', Timeline),
], debug=True)
