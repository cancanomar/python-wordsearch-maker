import random
import string

from pprint import pprint #creates a visual interface for application

handle = open("wordlist.txt") #Linux dictionary of words. included in text file
words = handle.readLines():

handle.close()


words = [
    random.choice(words).replace("'",'').strip() \
    for _ in range(5)
] #takes 5 random words and removes single quotes in the wordlist

gridSize = 20

grid = [
    [ '_' for _ in range(gridSize) ]
    for _ in range(gridSize)
] #underscore grid

def printGrid():
    for x in range(gridSize):
        print '\t' * 8 + ' '.join( grid[x] )
printGrid()

orientations = [ 'horizontal', 'vertical', 'diagup', 'diagdown' ]
for word in words:
    wordLength = len(word)


    placed = False #boolean to track on word was able to be placed
    while not placed:
        orientation = random.choice(orientations) #direction choices

        if orientation == 'horizontal':
            stepX = 1
            stepY = 0
        if orientation == 'vertical':
            stepX = 0
            stepY = 1
        if orientation == 'diagup':
            stepX = 1
            stepY = -1
        if orientation == 'diagdown':
            stepX = 1
            stepY = 1

        xPosition = random.randint(0, gridSize) #starting point for word
        yPosition = random.randint(0, gridSize)

        endingX = xPosition + wordLength * stepX
        endingY = yPosition + wordLength * stepY

        if endingX < 0 or endingX >= gridSize:
            continue
        if endingY < 0 or endingY >= gridSize:
            continue
        failed = False #determines if word can be placed on the grid to begin with

        for i in range(wordLength)
            character = word[i]
            newPositionX = xPosition + i*stepX
            newPositionY = yPosition + i*stepY

            characterAtNewPosition = grid[newPositionX][newPositionY]
            if characterAtNewPosition != '_':
                continue
            else:
                failed = True
                break

            if failed:
                continue
            else:
                for i in range(wordLength):
                    character = word[i]

                    newPositionX = xPosition + i*stepX
                    newPositionY = yPosition + i*stepY

                    grid[newPositionX][newPositionY] = character

                placed = True

for x in range(gridSize):
    for y in range(gridSize):
        if  (grid[x][y] == '_'):
            grid[x][y] = random.choice(string)

printGrid()
print "Word Bank:"
pprint (words)
