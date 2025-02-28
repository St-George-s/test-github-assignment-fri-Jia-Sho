import csv

# record to store olympics data
class Country:
    def __init__(self, rank, country_name, country_code, gold, silver, bronze, total):
        self.rank = rank
        self.country_name = country_name
        self.country_code = country_code
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = total

# storing the data in csv file as array of records
def data_loading():
    countries = []
    with open("Olympics starter/olympics2024.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            country = Country(row[0], row[1], row[2], int(row[3]),int(row[4]), int(row[5]), int(row[6]))
            countries.append(country)
    return countries

# finds total medals across all countries
def medal_calculation(countries):
    total_medal = 0
    for i in range(len(countries)):
        total_medal = total_medal + countries[i].total
    print(total_medal)
    pass

# finds the country with maximum gold medals
def top_country_identification(countries):
    #find max in total medals
    maximum = countries[0].total
    index = 0
    for i in range(1, len(countries)):
        if maximum < countries[i].total:
            maximum = countries[i].total
            index = i
    print("The country with highest number of medals is", countries[index].country_name, "with", maximum , "medals.")
    pass

# makes a text file of countries with more than 30 gold medals
def gold_medal_report(countries):
    with open("topCountries.txt", "w") as file:
        for i in range(0, len(countries)):
            if countries[i].gold > 30:
                file.write(str(countries[i].country_name) + " has " + str(countries[i].gold) + " golds\n")
    pass

# main program
countries = data_loading()
medal_calculation(countries)
top_country_identification(countries)
gold_medal_report(countries)
