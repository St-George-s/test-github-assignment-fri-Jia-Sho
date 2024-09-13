# Standard algorithm with parallel arrays #
times_spent = [5, 3, 4, 6, 5]
student_name = ["Alice", "Ben", "Cara", "David", "Eva"]
activities = ["hillwalking", "canoeing", "climbing", "hillwalking", "canoeing"]


class Activities:
    def __init__(self, time)








# Find Maximum in parallel arrays
def find_max(time, name, activity):
    maximum = time[0]
    maxIndex = 0
    for i in range(1, len(time)):
        if maximum < time[i]:
            maximum = time[i]
            maxIndex = i
    print("The maximum time spent was", maximum ,"hours by", name[maxIndex], "during", activity[maxIndex])

#Find Minimum in parallel arrays
def find_min(time, name, activity):
    minimum = time[0]
    maxIndex = 0
    for i in range(1,len(time)):
        if minimum > time[i]:
            minimum = time[i]
            maxIndex = i
    print("The minimum time spent was", minimum ,"hours by", name[maxIndex], "during", activity[maxIndex])

#Linear Search in parallel arrays
def linear_search(time, name , activity):
    item_searching = int(input("Enter the value to find "))
    index = 0
    for i in range(0, len(time)):
        if item_searching == time[i]:
            index = i
            print("Time", item_searching,"hours was spent by", name[index],"during", activity[index]  )
    
#count occourances in parallel arrays
def count_occourances(time, name , activity):
    item_counting = int(input("Enter the item to count "))
    count = 0
    name_count = []
    for i in range(0, len(time)):
        if item_counting == time[i]:
            count = count +1
            name_count.append(name[i])
    print("Time", item_counting,"hours appeared", count,"times. Students", name_count)

# main program
max_time = find_max(times_spent, student_name, activities)


find_min(times_spent, student_name, activities)
linear_search(times_spent, student_name, activities)
count_occourances(times_spent, student_name, activities )