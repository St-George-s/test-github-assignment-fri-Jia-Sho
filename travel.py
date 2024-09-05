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

def print_all_trips(destination,people_count,travel_method):
    for i in range(len(destination)):
        print("Your ",i+1," trip is to",destination[i],"with",people_count[i],"people by",travel_method[i])

#main
destination_array = []
people_count_array = []
travel_method_array = []
destination = get_destination()
while destination != "END":
    destination_array.append(destination)
    people_count = get_number_of_people()
    people_count_array.append(people_count)
    if destination in [ "edinburgh" , "glasgow" , "dundee" , "aberdeen"]:
        travel_method = "local transport"
    else:
        travel_method = get_travel_method()
    travel_method_array.append(travel_method)
    print_travel_details(destination,people_count,travel_method)
    destination = get_destination()
print_all_trips(destination_array,people_count_array,travel_method_array)
