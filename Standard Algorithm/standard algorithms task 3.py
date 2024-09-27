# Standard algorithm with parallel arrays #
times_spent = [5, 3, 4, 6, 5]
student_name = ["Alice", "Ben", "Cara", "David", "Eva"]
activities = ["hillwalking", "canoeing", "climbing", "hillwalking", "canoeing"]

# defining the record
class Activities:
    def __init__(self, time, name, activity):
        self.time = time
        self.name = name
        self.activity = activity

# storing in form of arrays of records
def record_storing(time , name , activity):
    for i in range(0, len(time)):
        student_activities = [ Activities(time[i], name[i], activity[i]) ]
    return student_activities


# Find Maximum in arrays of records
def find_max(record):
    maximum = record[0].time
    maxIndex = 0
    for i in range(1, len(record)):
        if maximum < record[i].time:
            maximum = record[i].time
            maxIndex = i
    print("The maximum time spent was", maximum ,"hours by", record[maxIndex].name, "during", record[maxIndex].activity)

#Find Minimum in arrays of records
def find_min(record):
    minimum = record[0].time
    maxIndex = 0
    for i in range(1,len(record)):
        if minimum < record[i].time :
            minimum = record[i].time
            maxIndex = i
    print("The minimum time spent was", minimum ,"hours by", record[maxIndex].name, "during", record[maxIndex].activity )

#Linear Search in arrays of records
def linear_search(record):
    item_searching = int(input("Enter the value to find "))
    index = 0
    for i in range(0, len(record)):
        if item_searching == record[i].time:
            index = i
            print("Time", item_searching,"hours was spent by", record[index].name ,"during", record[index].activity  )
    
#count occourances in arrays of records
def count_occourances(record):
    item_counting = int(input("Enter the item to count "))
    count = 0
    name_count = []
    for i in range(0, len(record)):
        if item_counting == record[i].time :
            count = count +1
            name_count.append(record[i].name )
    print("Time", item_counting,"hours appeared", count,"times. Students", name_count)

# main program
record = record_storing(times_spent, student_name, activities)
find_max(record)
find_min(record)
#linear_search(record)
#count_occourances(record)