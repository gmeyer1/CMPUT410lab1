class Student:
	courseMarks={}
	name=""
	def __init__(self, name, family):
		self.name = name

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark

	def average(self):
		total = 0.0
		for course, mark in self.courseMarks.items():
			total += mark
			
		return total/len(self.courseMarks)
	
a = Student("bob","bobbington")
a.addCourseMark("CMPUT 401",2.0)
a.addCourseMark("CMPUT 410",3.0)
a.addCourseMark("CMPUT 415",4.0)

print("Name: %s\nAverage Grade: %.1f" %(a.name, a.average()))