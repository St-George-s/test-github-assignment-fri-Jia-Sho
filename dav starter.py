import random

def generate_username(first_name , last_name):
    first_part = first_name[0:3]
    second_part = last_name[0:3]
    last_part = str(random.randint(100,999))
    username = first_part + second_part + last_part
    print("Your username is ", username)


first_name = input("Enter your first name ")
last_name = input("Enter your last name ")
age = input("Enter your age ")
award_level = input("Enter your Award level ")

generate_username(first_name, last_name)