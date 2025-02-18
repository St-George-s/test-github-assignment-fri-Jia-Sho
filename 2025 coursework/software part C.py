import csv

#defining the record Order
class Order:
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating

#procedure to read the data from file into array of records
def read_orders_data():
    with open("2025 coursework/orders.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            order = Order(row[0], row[1], row[2], row[3], float(row[4]), int(row[5]))
            orders.append(order)

# function to find the position of the customer who gave the first 5-star rating in the month entered by the user
def position_winnner_customer(orders):
    position = -1
    index = 0
    month_search = input("Enter the first three letters of a month to search for ")
    while position == -1:
         for index in range() < len(orders):
            if orders[index].date[3:5] == month_search and orders[index].rating == 5:
                    position= index
            index = index + 1
    return position














#main py
orders =  []
read_orders_data()
position = position_winnner_customer(orders)
print(position)
 
