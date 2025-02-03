import csv

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
