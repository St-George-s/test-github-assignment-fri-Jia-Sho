
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
    def __init__(self, brand, animalType, weight, price, stock):
        self.brand = brand
        self.animalType = animalType
        self.weight = weight
        self.price = price
        self.stock = stock

petFoodStock = [
    PetFood("Purina", "cat", 1.5 , 24.99 , 10),
    PetFood("Pedigree", "Dog", 2.0 , 18.99 , 20)
]

for i in range(len(petFoodStock)):
    print(petFoodStock[i].weight)
    print("The brand", petFoodStock[i].brand , "is for", petFoodStock[i].animalType, "weighing", petFoodStock[i].weight )

for pet in petFoodStock:
    print(pet.price)