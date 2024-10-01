import csv
# defining class order
class Order():
    def __init__(self, customer_name, product_purchased, amount_spent, customerID , category_product):
        self.customer_name = customer_name
        self.product_purchased = product_purchased
        self.amount_spent = amount_spent
        self.customerID = customerID
        self.category_product = category_product

#read csv file in arrays of record
def readOrdersFromCSV():
    orders = []
    with open("Mock test/orders.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            customer_orders = Order(row[0],row[1], float(row[2]))
            orders.append(customer_orders)
    return orders

def findMaxOrderWithTv(orders):
    maxOrder = 0.00
    maxIndex = 0
    for i in range(0,len(orders)):
        if "TV" in orders[i].product_purchased :
            if maxOrder < orders[i].amount_spent:
                maxOrder = orders[i].amount_spent
                maxIndex = i
    print("Maximum spent on TV is", maxOrder,"by", orders[maxIndex].customer_name)

def discount(orders):
    with open("discount.txt","a") as file:
    for i in range(0, len(orders)):
        if orders[i].customerID % 5 == 0:
            product = orders[i].category_product[:3]
            file.write(orders[i].customerID, product, "Discount code assigned")
            

# main program
orders = readOrdersFromCSV()
findMaxOrderWithTv(orders)