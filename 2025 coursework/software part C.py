import csv

#defining the record- Order
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
    orders = []
    with open("2025 coursework/orders.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            order = Order(row[0], row[1], row[2], row[3], (row[4]), (row[5]))
            orders.append(order)
    return orders

# function to find the position of the customer who gave the first 5-star rating in the month entered by the user
def position_winnner_customer(orders):
    position = -1
    index = 0
    month_search = input("Enter the first three letters of a month to search ")
    while position == -1 and index < len(orders):
        if orders[index].date[3:6] == month_search and int(orders[index].rating) == 5:
            position = index
        index = index + 1
    return position

# procedure to write winner details to a text file
def winning_customers(orders, position):
    with open ("winningCustomer.txt", "w") as file:
        if position >= 0:
            file.write( orders[position].orderNum + ", " + orders[position].email + ", " + orders[position].cost)
        else:
            file.write("No Winner")
    file.close()

# a single function to find and return the total number of orders delivered and collected
def countOption(orders):
    total_delivered = 0
    total_collected = 0
    for i in range(0, len(orders)):
        if orders[i].option == "Delivery":
            total_delivered = total_delivered + 1
        else:
            total_collected = total_collected + 1
    return total_delivered, total_collected

# procedure to display the total number of orders delivered and collected to date
def display_total_order_option(orders):
    total_delivered, total_collected = countOption(orders)
    print("Total number of orders delivered to date: ", total_delivered)
    print("Total number of orders collected to date: ", total_collected)


#main py
orders = read_orders_data()
position = position_winnner_customer(orders)
winning_customers(orders, position)
display_total_order_option(orders)
 
