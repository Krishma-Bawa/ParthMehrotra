class TimelineObject:
	heading = ""
	role = ""
	time = ""
	kind = ""
	link = ""
	skills = []

	def __init__(self, heading, role, time, kind, link, skills):
		self.heading = heading
		self.role = role
		self.time = time
		self.kind = kind
		self.link = link
		self.skills = skills
