def entering_expenses():
    description= input("Enter description of the expense ")
    amount= int(input("Enter the amount spent "))
    category = input("Enter the category of the expense ")
    
    return description, amount, category

def putting_in_file(expenses):
    with open("expenses.txt", "w") as file:
        for i in range(3):
            file.write(expenses[i])

# main.py
expenses= [entering_expenses()]
putting_in_file(expenses)

