import numpy as np
import math
import random
#Map of Europe
mapArray = [["-", "-", "-", "-", "-", "-", "O", "-", "-", "-", "-", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "O", "O", "-", "-", "-", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "O", "O", "O", "-", "-", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "-", "-", "-", "-", "-", "O", "O", "-",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "O", "-", "-", "-", "-", "O", "-", "-",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "O", "-", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "-", "O", "-", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "O", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "O", "-", "O", "O", "-", "-", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "-", "-", "-", "O", "O", "-", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "-", "-", "-", "-", "O", "O", "-", "-", "O", "O",],
            ["-", "-", "-", "O", "O", "-", "-", "-", "-", "O", "O", "-", "-", "-", "-", "O",],]

displayArray = [["-", "-", "-", "-", "-", "-", "O", "-", "-", "-", "-", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "O", "O", "-", "-", "-", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "O", "O", "O", "-", "-", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "-", "-", "-", "-", "-", "O", "O", "-",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "O", "-", "-", "-", "-", "O", "-", "-",],
            ["-", "-", "-", "-", "-", "O", "-", "O", "O", "-", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "-", "O", "-", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "-", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "-", "O", "-", "-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "-", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "O", "O", "O", "-", "-", "O", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "O", "-", "O", "O", "-", "-", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "O", "-", "-", "-", "O", "O", "-", "O", "O", "O",],
            ["-", "-", "O", "O", "O", "O", "-", "-", "-", "-", "O", "O", "-", "-", "O", "O",],
            ["-", "-", "-", "O", "O", "-", "-", "-", "-", "O", "O", "-", "-", "-", "-", "O",],]

#array of the "Resistance" of each country, based on medicine and how advanced or rich their economy is, higher numbers are weaker resistances while low numbers are high resistances, these are multiplyers, 1 is baseline
resistanceArray = [[0, 0, 0, 0, 0, 0, .9, 0, 0, 0, 0, 1, 1, 1, 1, 1,],
            [0, 0, 0, 0, 0, 0, .85, .9, 0, 0, 0, 1, 1, 1, 1, 1,],
            [0, 0, 0, 0, 0, .8, .9, .9, 0, 0, 0, 0, 1, 1, 1, 1,],
            [0, 0, 0, 0, 0, .9, 0, .8, 0, 0, 0, 0, 0, 1, 1, 0,],
            [0, 0, 0, 0, 0, .8, 0, .75, .76, 0, 0, 0, 0, .9, 0, 0,],
            [0, 0, 0, 0, 0, .8, 0, .7, .6, 0, 0, 0, 1, .95, 1, 1,],
            [0, 0, 0, 0, 0, 0, 0, 0, .7, 0, 1, 1, 1, 1, 1, 1.1,],
            [0, 0, 0, 0, 0, 0, 0, 0, .6, .95, .9, 1, 1, 1, 1, 1.1,],
            [0, 0, 0, 0, 0, 0, 0, .7, .6, .75, .8, 1, 1, 1, 1.1, 1.1,],
            [0, 0, 0, .9, 0, 0, 0, .8, .7, .75, .75, 1, 1, 1, 1.1, 1.1,],
            [0, 0, 1, .9, .95, 0, .8, .9, .8, .8, 1, 1, 1, 1, 1.1, 1.1,],
            [0, 0, 1, .9, .9, .9, .85, .8, 1, 1.1, 0, 0, 1.1, 1, 1, 1.1,],
            [0, 0, 1, .9, .9, .9, .9, .9, 0, 1.05, .95, 0, 0, 1, 1.1, 1.1,],
            [0, 0, 1, .9, .9, .9, .9, 0, 0, 0, .85, .9, 0, 1, 1.1, 1.1,],
            [0, 0, 1, .9, .9, .9, 0, 0, 0, 0, 1, 1.05, 0, 0, 1.1, 1.1,],
            [0, 0, 0, .9, .9, 0, 0, 0, 0, .95, .9, 0, 0, 0, 0, 1.2,],]

#Population Distribution for every square of land (Water is marked as Zero)
populationArray = [ [0, 0, 0, 0, 0, 0, 3805468, 0, 0, 0, 0, 1805468, 1805468, 1805468, 1805468, 1805468,],
                    [0, 0, 0, 0, 0, 0, 6805468, 6805468, 0, 0, 0, 3805468, 2805468, 1805468, 1805468, 1805468,],
                    [0, 0, 0, 0, 0, 4805468, 6805468, 6805468, 0, 0, 0, 0, 2805468, 1805468, 1805468, 1805468,],
                    [0, 0, 0, 0, 0, 3805468, 0, 6805468, 0, 0, 0, 0, 0, 2805468, 2805468, 0,],
                    [0, 0, 0, 0, 0, 6805468, 0, 12805468, 9805468, 0, 0, 0, 0, 1805468, 0, 0,],
                    [0, 0, 0, 0, 0, 3805468, 0, 30805468, 16805468, 0, 0, 0, 2805468, 2805468, 1805468, 805468,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 5805468, 0, 10805468, 5805468, 5805468, 1805468, 2805468, 3805468,],
                    [0, 0, 0, 0, 0, 0, 0, 0, 6805468, 17805468, 7805468, 7805468, 7805468, 4805468, 3805468, 1805468,],
                    [0, 0, 0, 0, 0, 0, 0, 5805468, 8805468, 7805468, 18805468, 16805468, 7805468, 3805468, 5805468, 1805468,],
                    [0, 0, 0, 5805468, 0, 0, 0, 5805468, 5805468, 6805468, 10805468, 9805468, 2805468, 2805468, 2805468, 1805468,],
                    [0, 0, 3805468, 5805468, 5805468, 0, 6805468, 5805468, 7805468, 11805468, 2805468, 3805468, 3805468, 2805468, 1805468, 1805468,],
                    [0, 0, 4805468, 1905468, 4805468, 6805468, 4805468, 5805468, 8805468, 9805468, 0, 0, 2805468, 805468, 1805468, 2805468,],
                    [0, 0, 5805468, 10805468, 5805468, 5805468, 5805468, 5805468, 0, 29805468, 9805468, 0, 0, 2805468, 1805468, 3805468,],
                    [0, 0, 5805468, 3805468, 3805468, 3805468, 9805468, 0, 0, 0, 5805468, 5805468, 0, 3805468, 2805468, 1805468,],
                    [0, 0, 5805468, 3805468, 6805468, 10805468, 0, 0, 0, 0, 7805468, 8805468, 0, 0, 2805468, 2805468,],
                    [0, 0, 0, 7805468, 10805468, 0, 0, 0, 0, 8805468, 9805468, 0, 0, 0, 0, 1805468,],]

#Add up the population of a certain array (can be defined)
def countPopulation(arrayType):
    xCount = 0
    yCount = 0
    popCount = 0
    while xCount < 16:
        while yCount < 16:
            popCount = popCount + arrayType[xCount][yCount]
            yCount = yCount + 1
        yCount = 0
        xCount = xCount + 1
    return popCount

#Count of all the people remaining alive in Europe
aliveTotal = [countPopulation(populationArray)]

#Array of all the amounts of people infected by square of land
infectedArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]
#Array with count of all the people infected using countPopulation(infectedArray) method
infectedTotal = [countPopulation(infectedArray)]

#Array of all the amounts of people dead by square of land
deadArray =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]
#Array with count of all the people dead using countPopulation(deadArray) method
deadTotal = [countPopulation(deadArray)]

#multiplyer of how many people are infected per week
infectivity = [.12]
#multiplyer of how many INFECTED people are killed each week
deadly = [0.001]

#cure progress tracker ou of 100%
cureProgress = [0]

#counts the year that each square is on
yearArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]

#Array that keeps track of the time
weekCounter = [0]
def dateGenerator():
    year = 2017 + int(weekCounter[0] / 52)
    week = weekCounter[0] % 52
    date = "Year:", year, " Week:", week
    return date
dateDisplay = [dateGenerator()]


def printMap(board):
    for row in board:
        print("  ".join(row))

def checkOtherSquares(x, y):
        if displayArray[x][y] == "x" or displayArray[x][y] == "X" or displayArray[x][y] == "#":
            #top left
            if x - 1 >= 0 and y - 1 >= 0:
                if displayArray[x - 1][y - 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x - 1][y - 1] = "x"
                        infectedArray[x - 1][y - 1] = 1 / 35 * populationArray[x - 1][y - 1]
            #top
            if x - 1 >= 0:
                if displayArray[x - 1][y] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x - 1][y] = "x"
                        infectedArray[x - 1][y] = 1 / 35 * populationArray[x - 1][y]
            #top right
            if x - 1 >= 0 and y + 1 <= 15:
                if displayArray[x - 1][y + 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x - 1][y + 1] = "x"
                        infectedArray[x - 1][y + 1] = 1 / 35 * populationArray[x - 1][y + 1]
            #right
            if y + 1 <= 15:
                if displayArray[x][y + 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x][y + 1] = "x"
                        infectedArray[x][y + 1] = 1 / 35 * populationArray[x][y + 1]
            #bottom right
            if y + 1 <= 15 and x + 1 <= 15:
                if displayArray[x + 1][y + 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x + 1][y + 1] = "x"
                        infectedArray[x + 1][y + 1] = 1 / 35 * populationArray[x + 1][y + 1]
            #bottom
            if x + 1 <= 15:
                if displayArray[x + 1][y] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x + 1][y] = "x"
                        infectedArray[x + 1][y] = 1 / 35 * populationArray[x + 1][y]
            #bottom left
            if x + 1 <= 15 and y - 1 >= 0:
                if displayArray[x + 1][y - 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x + 1][y - 1] = "x"
                        infectedArray[x + 1][y - 1] = 1 / 35 * populationArray[x + 1][y - 1]
            #left
            if y - 1 >= 0:
                if displayArray[x][y - 1] == "O":
                    if .1 < resistanceArray[x][y] * infectedArray[x][y] / populationArray[x][y]:
                        displayArray[x][y - 1] = "x"
                        infectedArray[x][y - 1] = 1 / 35 * populationArray[x][y - 1]

def simulateSquare(x, y):
    if displayArray[x][y] == "x" or displayArray[x][y] == "X" or displayArray[x][y] == "#":
        deadArray[x][y] = deadArray[x][y] + deadly[0] * infectedArray[x][y]
        populationArray[x][y] = populationArray[x][y] - deadly[0] * infectedArray[x][y]
        infectedArray[x][y] = infectedArray[x][y] - deadly[0] * infectedArray[x][y]
        infectedArray[x][y] = infectedArray[x][y] + resistanceArray[x][y] * infectivity[0] * (populationArray[x][y] * math.exp(infectivity[0] * yearArray[x][y] + 8)) / ((math.exp(infectivity[0] * yearArray[x][y]) + (math.exp(8))) ** 2)
        yearArray[x][y] = yearArray[x][y] + 1
        checkOtherSquares(x, y)
        if infectedArray[x][y] + deadArray[x][y] >= 1:
            displayArray[x][y] = "x"
        if (infectedArray[x][y] + deadArray[x][y]) / populationArray[x][y] > .5:
            displayArray[x][y] = "X"
        if (infectedArray[x][y] + deadArray[x][y]) / populationArray[x][y] > .8:
            displayArray[x][y] = "#"
        if deadArray[x][y] / infectedArray[x][y] > .8:
            displayArray[x][y] = "$"

def runWeek():
    xCoord = 0
    yCoord = 0
    while xCoord < 16:
        while yCoord < 16:
            simulateSquare(xCoord, yCoord)
            yCoord = yCoord + 1
        yCoord = 0
        xCoord = xCoord + 1
    weekCounter[0] = weekCounter[0] + 1
    print(dateGenerator())
    printMap(displayArray)
    print("People Infected:",int(countPopulation(infectedArray)))
    print("People Dead:    ", int(countPopulation(deadArray)))
    print("Infectivity:", infectivity[0])
    print("Deadly:", deadly[0])
    print("------------------------------------------------------")

def randomSpot():
    spotx = np.random.randint(1, 16)
    spoty = np.random.randint(1, 16)
    if displayArray[spotx][spoty] == "O":
        displayArray[spotx][spoty] = "x"
        infectedArray[spotx][spoty] = 10000
        printMap(displayArray)
    else:
        randomSpot()

def mutate():
    mutateChance = np.random.randint(1, 25)
    if mutateChance == 15:
        infectivity[0] = infectivity[0] + .015
    if mutateChance == 12:
        deadly[0] = deadly[0] + .0003

def simulatePeriod(duration):
    randomSpot()
    timeIndex = 1
    pause = input("press enter to simulate...")
    while timeIndex < duration:
        if timeIndex % 20 == 0:
            pausetemp = input("Press enter to simulate another 20 weeks...")
        runWeek()
        timeIndex = timeIndex + 1
        mutate()

simulatePeriod(600)
