import csv

studentID = []
firstName = []
lastName = []
grade = []

def studentData():
    with open("File Handling/students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            studentID.append(row[0])
            firstName.append(row[1])
            lastName.append(row[2])
            grade.append(row[3])
    return studentID , firstName, lastName, grade

#studentID , firstName, lastName, grade = studentData()
#print(studentID , firstName, lastName, grade)

