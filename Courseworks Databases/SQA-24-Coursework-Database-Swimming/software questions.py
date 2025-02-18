import csv

company= []
numEmployees = []
ceoSalary = []

def reading_companies():
    with open("Courseworks Databases/SQA-24-Coursework-Database-Swimming/companies.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))

def find_max_salary_and_employee(ceoSalary , numEmployees):
    max_ceosalary = 0
    max_ceosalary_position = 0
    max_employees = 0 
    max_employees_position = 0 
    for i in range(0, len(ceoSalary)):
        if ceoSalary[i] > max_ceosalary:
            max_ceosalary = ceoSalary[i]
            max_ceosalary_position = i
        if numEmployees[i] > max_employees:
            max_employees = numEmployees[i]
            max_employees_position = i
    return max_employees_position, max_ceosalary_position

def salary_difference(company, ceoSalary):
    chosen_company = input("Enter the company name- ")
    found = False




#main.py
reading_companies()
max_emplyees_position, max_ceosalary_position = find_max_salary_and_employee(ceoSalary , numEmployees)

print(max_ceosalary_position)