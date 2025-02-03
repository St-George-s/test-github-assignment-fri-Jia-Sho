import csv
gameTitles= []
genres = []
ageRatings = []
platform = []

#reads the data into parallel arrays
def readGameDataFromCSV():
    #opening csv file in read mode
    with open("class test/game_platform_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        #loops over each row and append to corresponding arrays
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(int(row[2]))
            platform.append(row[3])
    #returning the appended lists
    return gameTitles, genres, ageRatings, platform

# finds how many games are in a genre that are under 18 and are on what platform
# writes the information to a text file
def countSuitableGames(genre_to_check, gameTitles, genres, ageRatings, platform):
    #open text file in write mode
    with open("platform_suitable_games.txt", "w") as file:
        for i in range(0, len(gameTitles)):
            if genres[i] == genre_to_check : 
                #check if age rating is under 18
                if ageRatings[i] < 18:
                    #write to the file 
                    file.write(gameTitles[i])
                    file.write(" -")
                    file.write(platform[i])
                    file.write("\n")
                    
   
#main program
readGameDataFromCSV()
genre_to_check= input("Enter the genre to check ")
countSuitableGames(genre_to_check, gameTitles, genres, ageRatings, platform)