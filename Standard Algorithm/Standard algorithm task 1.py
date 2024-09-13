times_spent = [5, 3, 4, 6, 5]

# Find Maximim
def find_max(array):
    maximum = array[0]
    for i in range(1, len(array)):
        if maximum < array[i]:
            maximum = array[i]
    print(maximum)

#Find Minimum
def find_min(array):
    minimum = array[0]
    for i in range(1,len(array)):
        if minimum > array[i]:
            minimum = array[i]
    print(minimum)

#Linear Search
def linear_search(array):
    item_searching = int(input("Enter the value to find "))
    for i in range(0, len(array)):
        if item_searching == array[i]:
            print("the item", item_searching,"is found")
            break

#count occourances
def count_occourances(array):
    item_counting = int(input("Enter the item to count "))
    count = 0
    for i in range(0, len(array)):
        if item_counting == array[i]:
            count = count +1
    print("The total number of times", item_counting,"occours is", count)

# main program
find_max(times_spent)
find_min(times_spent)
linear_search(times_spent)
count_occourances(times_spent)