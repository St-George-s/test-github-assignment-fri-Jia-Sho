class Washing_machine:
    def __init__(self, name, load, spin, price):
        self.name = name
        self.load = load
        self.spin = spin
        self.price = price
    

def read_data():
    return washing_machines

def getiing_load_and_speed():
    return smallest_load , slowest_spin

def find_cheapest(Washing_machines, smallest_load , slowest_spin):
    return cheapest_options

def display_cheapest(cheapest_options):
    pass


#main py
washing_machines = read_data()
smallest_load , slowest_spin = getiing_load_and_speed()
cheapest_options = find_cheapest(Washing_machines,smallest_load , slowest_spin)
display_cheapest(cheapest_options)
