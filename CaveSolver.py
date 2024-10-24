def loadCaveFromFile(cavefilename):
    cave = []
    cavefile = open(cavefilename, 'r', newline='', encoding='utf8')
    lines = cavefile.readlines()
    for line in lines:
        line = line.strip()
        cave.append(list(line))
    cavefile.close()
    return cave

def findEntance(cave):
    for row in range(len(cave)):
        for col in range(len(cave[0])):
            if cave[row][col] == 'A':
                return [row, col]
            
    
def findExit(cave):
    for row in range(len(cave)):
        for col in range(len(cave[0])):
            if cave[row][col] == 'Z':
                return [row, col]
            
#check if the current cave is marked
#true if marked, false if unmarked
def checkMarked(cave, markedCaves):
    if cave in markedCaves:
        return True
    else:
        return False

def checkUp(currentCave, cave, markedCaves):
    #check bounds
    #check if it's marked
    #check if it's a space
    #validCaves.append([currentCave[0] - 1, currentCave[1]])
    row, col = currentCave
    if row - 1 >= 0:
        if row - 1 < len(cave):
            #if cave[row - 1][col] not in markedCaves:
            if [row - 1, col] not in markedCaves:
                if cave[row - 1][col] != 'X':
                    return True
    return False

def checkDown(currentCave, cave, markedCaves):
    #check bounds
    #check if it's marked
    #check if it's a space
    row, col = currentCave
    if row + 1 > 0:
        if row + 1 < len(cave):
            #if cave[row + 1][col] not in markedCaves:
            if [row + 1, col] not in markedCaves:
                if cave[row + 1][col] != 'X':
                    return True
    return False
    
def checkRight(currentCave, cave, markedCaves):
    #check bounds
    #check if it's marked
    #check if it's a space
    row, col = currentCave
    if col + 1 > 0:
        if col + 1 < len(cave[0]):
            #if cave[row][col + 1] not in markedCaves:
            if [row, col + 1] not in markedCaves:
                if cave[row][col + 1] != 'X':
                    return True
    return False

def checkLeft(currentCave, cave, markedCaves):
    #check bounds
    #check if it's marked
    #check if it's a space
    row, col = currentCave
    if col - 1 >= 0:
        if col - 1 < len(cave[0]):
            #if cave[row][col - 1] not in markedCaves:
            if [row, col - 1] not in markedCaves:
                if cave[row][col - 1] != 'X':
                    return True
    return False

def check(currentCave, cave, markedCaves):

    validCaves = []

    # if checkUp(currentCave, cave, markedCaves) == True:
    #     validCaves.append(cave[currentCave[0] - 1][currentCave[1]])
    # if checkDown(currentCave, cave, markedCaves) == True:
    #     validCaves.append(cave[currentCave[0] + 1][currentCave[1]])
    # if checkRight(currentCave, cave, markedCaves) == True:
    #     validCaves.append(cave[currentCave[0]][currentCave[1] + 1])
    # if checkLeft(currentCave, cave, markedCaves) == True:
    #     validCaves.append(cave[currentCave[0]][currentCave[1] - 1])

    if checkUp(currentCave, cave, markedCaves) == True:
        validCaves.append([currentCave[0] - 1, currentCave[1]])
    if checkDown(currentCave, cave, markedCaves) == True:
        validCaves.append([currentCave[0] + 1, currentCave[1]])
    if checkRight(currentCave, cave, markedCaves) == True:
        validCaves.append([currentCave[0], currentCave[1] + 1])
    if checkLeft(currentCave, cave, markedCaves) == True:
        validCaves.append([currentCave[0], currentCave[1] - 1])

    
    return validCaves

#treat like main
def findPathFromEntranceToExit(cave):
    #treat like a stack
    path = []

    entrance = findEntance(cave)
    exit = findExit(cave)

    path.append(entrance)
    
    currentCave = entrance

    markedCaves = []
    # markedCaves.append(currentCave)
    # pathFound = False

    while path:
        print("Current path:", path)
        
        
        #check for surrounding caves
        #if yes move pick a cave and move to it
        #if no pop a cave off the stack
        #repeat until path is found


        #validCaves = check(currentCave, cave, markedCaves)
        #print(path)
        #if validCaves:
        #    nextCave = validCaves.pop()
        #    path.append(nextCave)
        #    markedCaves.append(currentCave)
        #    currentCave = nextCave
        #else:
        #    path.pop()

        #if currentCave == exit:
        #    pathFound = True
        #    break

        #check
        validCaves = check(currentCave, cave, markedCaves)

        #delete and path
        # IMPORTANT: Uncomment the 3 print statements to see extra information
        if validCaves:
            markedCaves.append(currentCave)
            # print("valid caves:", validCaves)
            # print("current cave:", currentCave)
            currentCave = validCaves.pop()
            # print("New current cave:", currentCave)
            path.append(currentCave)
        else:
            #if the cave is marked don't pop
            if currentCave not in markedCaves:
                markedCaves.append(currentCave)
            else:
                # markedCaves.append(currentCave)
                path.pop()
                #IF STATEMENT
                if path:
                    currentCave = path[-1]
                else:
                    print("No path found!")
                    break

        if currentCave == exit:
            print("Path Found!")
            break
    



    return path
    
    

    # Return a list of coordinate pairs [ [row, col], [row, col], ... ]
    # YOUR CODE HERE

    

#cave = loadCaveFromFile('alphacave.txt')
#cave = loadCaveFromFile('betacave.txt')
cave = loadCaveFromFile('gammacave.txt')
#cave = loadCaveFromFile('epsiloncave.txt')
print("Cave:", cave)
#entrance = []
#entrance.append(findEntance())
print("Entrance:", findEntance(cave))
path = findPathFromEntranceToExit(cave)
print(path)