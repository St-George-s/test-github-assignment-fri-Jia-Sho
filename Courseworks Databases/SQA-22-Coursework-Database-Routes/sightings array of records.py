import csv

# declaring the record
class Sighting:
    def __init__(self,town,mammal,date,age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age

#procedure to reading the txt file data into array of records
def read_sighting_data(sightings):
    with open("Courseworks Databases/SQA-22-Coursework-Database-Routes/mammals.txt", "r") as file:
        reader= csv.reader(file)
        for row in reader:
            sighting= Sighting(row[0], row[1], row[2], int(row[3]))
            sightings.append(sighting)

# procedure to find the age of the oldest walker
def oldest_walker(sightings):
    max_age = 0
    for i in range(0, len(sightings)):
        if sightings[i].age > max_age:
            max_age = sightings[i].age
    print("The oldest walker's age is ", max_age)

# function to return a variable capitalised
def capitalisation(variable):
    firstChar = variable[0]
    Ascii_firstChar = ord(firstChar)
    if Ascii_firstChar >= 97 and Ascii_firstChar <= 122:
        Ascii_firstChar = Ascii_firstChar - 32
        firstChar = chr(Ascii_firstChar)
        capitalised = firstChar + variable[1:]
        return capitalised

# procedure to find sighting dates for a particular mammal in a particular town
def sighting_dates(sightings):
    town = input("Enter the town ")
    town_capitalised = capitalisation(town)
    mammal = input("Enter the mammal ")
    mammal_capitalised = capitalisation(mammal)

    # loop over array of records to find the date where conditions are met 
    print("Dates of sightings were ")
    for i in range(0, len(sightings)):
        if sightings[i].town == town_capitalised and sightings[i].mammal == mammal_capitalised:
            print(sightings[i].date)

#procedure to count and display the number of sightings on each date
def sightings_count(sightings):
    date_to_count = sightings[0].date
    count = 1

    for i in range(1, len(sightings)):
        if sightings[i].date == date_to_count:
            count = count+1
        else:
            print("On ", date_to_count,"there were ", count,"sightings.")
            date_to_count = sightings[i].date 
            count = 1
    print("On ", date_to_count,"there were ", count,"sightings.")



#main py
sightings = []
read_sighting_data(sightings)
oldest_walker(sightings)
sighting_dates(sightings)
sightings_count(sightings)
