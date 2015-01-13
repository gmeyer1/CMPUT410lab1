# CMPUT 410 Winter 2015
# Lab 1
# Glenn Meyer
# gmeyer1

class Student:
	courseMarks={}
	name=""
	family=""
	def __init__(self, name, family):
		self.name = name
		self.family = family

	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark

	def average(self):
		total = 0.0
		for course, mark in self.courseMarks.items():
			total += mark
			
		return total/len(self.courseMarks)
	
a = Student("Bob","Bobbington")
a.addCourseMark("CMPUT 401",2.0)
a.addCourseMark("CMPUT 410",3.0)
a.addCourseMark("CMPUT 415",4.0)

print("Name: %s %s\nAverage Grade: %.1f" %(a.name, a.family, a.average()))
