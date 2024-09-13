import csv

#studentID = []
#firstName = []
#lastName = []
#grade = []

#def studentData():
#    with open("File Handling/students.csv", "r") as file:
#        reader = csv.reader(file)
#        header = next(reader)
#        for row in reader:
#            studentID.append(row[0])
#            firstName.append(row[1])
#            lastName.append(row[2])
#            grade.append(row[3])
#    return studentID , firstName, lastName, grade

#studentID , firstName, lastName, grade = studentData()
#print(studentID , firstName, lastName, grade)


# arrays of records
class Students:
    def __init__(self,studentID, firstName , lastName , grade):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade

def readStudentData():
    student = []
    with open("File Handling/students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            students = Students(row[0], row[1], row[2], row[3])
            student.append(students)

    return student

student = readStudentData()
for i in range(len(student)):
    print(student[i].studentID, student[i].firstName, student[i].lastName)
