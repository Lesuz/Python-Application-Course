# 8 Student - Course with assosiation class
class Course():

    def __init__(self, courseNumber,courseName):
        self.courseNumber = courseNumber
        self. courseName = courseName


    def getCourseNumber(self):
        return courseNumber
    
    def getCourseName(self):
        return courseName

class Student():

    def __init__(self, studentNumber,Fname,Lname):
        self.studentNumber = studentNumber
        self.Fname = Fname
        self.Lname = Lname

    def getStudentInfo(self):
        return "Studen number: " + str(studentNumber) + ", first name: " + str(Fname) + ", last name: " + str(Lname)

import datetime

class Enrollment():

    def __init__(self):
        self.courses = []
        self.students = []
        self.dates = []

    def addEnrollment(self, c,s,d):
        self.courses.append(c)
        self.students.append(s)
        self.dates.append(d)
        
    
    def getEnrollment(self, i):
        return self.courses[i],self.students[i],self.dates[i]

    
myEnrollment = Enrollment()

courseNumber = int(input("Course number: "))
courseName = input("Give name of the course: ")

myCourse = Course(courseNumber,courseName)

studentNumber = int(input("Give student number: "))
Fname = input("Give student's first name: ")
Lname = input("Give student's last name: ")

myStudent = Student(studentNumber,Fname,Lname)

myEnrollment.addEnrollment(myCourse,myStudent,datetime.datetime.now())

x = myEnrollment.getEnrollment(0)
print (x[0].getCourseNumber(),x[0].getCourseName(), x[1].getStudentInfo(),x[2].)
