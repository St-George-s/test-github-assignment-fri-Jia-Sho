import csv
attractions = []
category = []
visitors = []
daysOpen = []
height = []
# reading data from csv file to parallel arrays
def attractions_data():
    with open("Coursework/attractions.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            attractions.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])
    return attractions, category, visitors, daysOpen , height


# finding and display least visited attraction
def least_visited_attraction(attraction , visitor):
    minimum = visitor[0]
    minIndex = 0
    for i in range(1, len(visitor)):
        if minimum > visitor[i]:
            minimum = visitor[i]
            minIndex = i
    print("The least visited attraction is", attraction[minIndex], "with", minimum,"visitors.")
    pass

#finding and display most visited attraction
def most_visited_attraction(attraction, visitor):
    maximum = visitor[0]
    maxIndex = 0
    for i in range(1, len(visitor)):
        if maximum < visitor[i]:
            maximum = visitor[i]
            maxIndex = i
    print("The most visited attraction is", attraction[maxIndex],"With", maximum,"visitors.")


# find names of roller costers that need service in 7 days and write to text file
def service_roller_coster(attraction, category, daysOpen):
    with open("service.csv","w") as file:
        for i in range (0,len(attraction)):
            if category[i] == "Roller Coaster":
                days = daysOpen[i] % 90
                if 90-days <= 7:
 
                    file.write(attraction[i] )
                    

#main program
attractions_data()
least_visited_attraction(attractions, visitors)
most_visited_attraction(attractions, visitors)
service_roller_coster(attractions, category, daysOpen)
