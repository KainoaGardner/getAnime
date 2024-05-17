def displayWatchlist():
    print("---Watchlist---")
    with open("watchingFile.txt", "r") as file:
        for i,title in enumerate(file):
            print(f"{i + 1}: {title}",end="")
    file.close()
    
def removeAllWatchlist():
    print("removed all titles from watchlist")
    with open("watchingFile.txt","w") as file:
        file.write("")
    file.close()

def addWatchList(titles):
    alreadyAdded = []
    with open("watchingFile.txt","r") as inputFile:
        for line in inputFile:
            if line.strip("\n") in titles:
                alreadyAdded.append(line.strip("\n"))
                titles.remove(line.strip("\n"))
        with open("watchingFile.txt","a") as outputFile:
            for title in titles:
                outputFile.write(title + "\n")

        outputFile.close()   
    inputFile.close()

    for title in alreadyAdded:
        print(f"{title} is already in Watchlist")
    print("---ADDED---") 
    for i,title in enumerate(titles):
        print(f"{i + 1}: {title}")
    print()


def deleteWatchlist(titles):
    foundTitles = []
    with open("watchingFile.txt","r") as file:
        lines = file.readlines()
    file.close()
    with open("watchingFile.txt","w") as file:
        for line in lines:
            if not checkInList(line.strip("\n"),titles):
                file.write(line)
            else:
                foundTitles.append(line.strip("\n"))
    file.close()

    print("---DELETED---") 
    for i,title in enumerate(foundTitles):
        print(f"{i + 1}: {title}")
    print()

def checkInList(target,titles):
    print(target)
    for title in titles:
        if target == title:     
            return True
    return False

def listAiring(airingToday):
    airing = []
    with open("watchingFile.txt","r") as file:
        for line in file:
            if line.strip("\n") in airingToday:
                airing.append([line.strip("\n"),airingToday[line.strip("\n")]["ep"]])
    file.close()

    print("---AiringToday---")
    for i,element in enumerate(airing):
        print(f"{i + 1}: {element[0]} {element[1]}")
        


    


