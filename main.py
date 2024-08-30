def get_destination():
    destination = input("enter the travel destination ")
    return destination

def get_number_of_people():
    people_number = input("Enter the number of people going ")
    return people_number

def get_travel_method():
    travel_method = input("Enter your mode of transport ")
    return travel_method

def print_travel_details(destination, people_count, travel_method):
    print("Your are going to", destination,"with", people_count,"people by",travel_method)

#main

destination = get_destination()
people_count = get_number_of_people()
if destination == "edinburgh" or "glasgow" or "dundee" or "aberdeen":
    travel_method = "local transport"
else:
    travel_method = get_travel_method()
print_travel_details(destination,people_count,travel_method)