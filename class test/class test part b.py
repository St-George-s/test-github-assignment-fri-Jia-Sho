import csv
gameTitles= []
genres = []
ageRatings = []

#reads the data into parallel arrays
def readGameDataFromCSV():
    with open("class test/game_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        #loops over each row and append to corresponding arrays
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(int(row[2]))
    return gameTitles, genres, ageRatings

# finds how many games are in a genre that are under 18
def countSuitableGames(genre_to_check, gameTitles, genres, ageRatings):
    count = 0
    for i in range(0, len(gameTitles)):
        if genres[i] == genre_to_check : 
            if ageRatings[i] < 18:
                print(gameTitles[i])
                count = count +1
    print("Total number of games in", genre_to_check," that were under 18 were",count)

#main program
readGameDataFromCSV()
genre_to_check= input("Enter the genre to check ")
countSuitableGames(genre_to_check, gameTitles, genres, ageRatings)