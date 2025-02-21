#making the record
import csv

class Member:
    def __init__(self,forename,surname,distance):
        self.forename = forename
        self.surname = surname
        self.distance = distance

# reading txt file data into array of records
def reading_member_data():
    members = []
    with open ("Courseworks Databases/SQA-19-Coursework-Database-Flights/members.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            member = Member(row[0], row[1], float(row[2]))
            members.append(member)
    return members

# finding the furthest distance travelled
def furthest_distance(members):
    furthest = members[0].distance
    for i in range(1,len(members)):
        if members[i].distance > furthest:
            furthest = members[i].distance
    return furthest

#displaying furthest distance travelled
def display_furthest(furthest):
    print("The furthest distance travelled is", furthest, "miles")

# function to names of people who have walked more than 70% of furthest distance to a file
def club_prize_winners(members, furthest):
    with open("Results.txt", "w") as file:
        file.write('The prize members are:' + "\n" )
        for i in range(0, len(members)):
            if members[i].distance > 0.7*furthest:
                file.write(members[i].forename + " " + members[i].surname + "\n") 

        file.write("\n" + "The number of full marathons walked by each member are: " + "\n")
        for i in range(0, len(members)):
            full_marathons = int(members[i].distance/26.22)
            file.write( members[i].forename + " " + members[i].surname + str(full_marathons) + "\n")

#main python
members = reading_member_data()
furthest= furthest_distance(members)
display_furthest(furthest)
club_prize_winners(members, furthest)