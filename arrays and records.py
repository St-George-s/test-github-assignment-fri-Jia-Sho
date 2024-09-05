
brand = ["giant","trek"]
model = ["escape 2","Marlin 5"]
frame_size = [20,22]
type = ["Hybrid","Mountain"]
price = [450,370]
electric_assistant = [False, False]

class car:
    def __init__(self, make,year,price,colour):
        self.colour = colour
        self.price = price
        self.year = year
        self.make = make

cars = [
car("Mercedes", 2017, 3000, "Z black"),
car("BMW", 2020, 4000, "Matt Black")
]


# pet shop data
class PetFood:
    def __init__(self, brand, AnimalType, Weight, price, stock):
        self.brand = brand
        self.AnimalType = AnimalType
        self.Weight = Weight
        self.price = price
        self.stock = stock

PetFood_1 = PetFood