import csv

#defining class Books
class Books():
    def __init__(self,title,author,genre,price,stock):
        self.title= title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

#read csv file in array of records
def readBooksFromCSV():
    books = []
    with open("random codes/books.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            shop_books= Books(row[0], row[1], row[2],float(row[3]), int(row[4]))
            books.append(shop_books)
    return books

def viewAllBooks(books):
    for i in range(0, len(books)):
        print(i+1,". ", books[i].title,",",books[i].author, ",", books[i].genre, books[i].price, ",", books[i].stock)
    print("")

def searchBook(books):
    search_book = input("Enter the title/author of the book you are finding ").lower()
    found = False
    for i in range(0, len(books)):
        if books[i].title.lower() == search_book or books[i].author.lower() == search_book:
            print(books[i].title,",",books[i].author, ",", books[i].genre,",", books[i].price, ",", books[i].stock)
            found = True
            break
    if found == False:
        print("This book is not available")

def updateStock(books):
    title = input("Enter the title of the book to update stock: ").lower()
    found = False
    for i in range(0, len(books)):
        if books[i].title.lower() == title:
            new_stock = input("Enter the new stock level ")
            books[i].stock = new_stock
            print("The stock level has been updated" )
            print(books[i].title,",",books[i].author, ",", books[i].genre, ",", books[i].price, ",", books[i].stock)
            found = True
            break
    if found == False:
        print("This book is not available")

    with open("random codes/books.csv", "r") as file:
        reader = csv.reader(file)
        lines = list(reader)  

    for line in lines:
        if line[0].lower() == title: 
            line[4] = str(new_stock)  
            break

    with open("random codes/books.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines) 


def calculate_total_inventory_value(books):
    total_value = 0
    for i in range(0, len(books)):
        cost_each_title =float(books[i].price) * float(books[i].stock)
        total_value = total_value + cost_each_title
    print("The total inventory value is £", total_value)

# main program
books = readBooksFromCSV()
viewAllBooks(books)
searchBook(books)
updateStock(books)
calculate_total_inventory_value(books)
