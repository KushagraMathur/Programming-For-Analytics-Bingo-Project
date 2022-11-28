import numpy as np
from collections import defaultdict
import BingoConstantsClass

'''
@description
SimulationsClass - Class which contains the logic for Bingo game simulation.
'''


class SimulationsClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self):
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()

    '''
    @description
    Method to check how many players reached bingo after every number called
    @parameter
    countCardsSet- Contains the indices of cards that might have reached bingo after every number being called.
    bingoCardsSet- Contains the indices of cards that have reached bingo.
    testArray- An array equal to size of cards array. Contains one(1) for free cells and zeros(0) for others.
               Zeros are replaced by ones if a number is found in cards array.
    sizeOfCardRow- The number of rows in a card specified by user.
    sizeOfCardCol- The number of columns in a card specified by user.
    '''

    def checkBingo(self, countCardsSet, bingoCardsSet, testArray, sizeOfCardRow, sizeOfCardCol):
        # To check for the bingo possibility for square matrix; row-wise, column-wise and and by both diagonals.
        if sizeOfCardRow == sizeOfCardCol:
            for index in countCardsSet:
                if np.diagonal(self.testArray[index]).sum() == sizeOfCardRow:
                    bingoCardsSet.add(index)
                elif (np.diag(np.fliplr(self.testArray[index])).sum()) == sizeOfCardRow:
                    bingoCardsSet.add(index)
                elif sizeOfCardRow in np.sum(testArray[index], axis=0):
                    bingoCardsSet.add(index)
                elif sizeOfCardRow in np.sum(testArray[index], axis=1):
                    bingoCardsSet.add(index)
        
        # To check for the bingo possibility for asymmetric matrix; only row-wise and column-wise.
        else:
            for index in countCardsSet:
                if sizeOfCardRow in np.sum(testArray[index], axis=0):
                    bingoCardsSet.add(index)
                elif sizeOfCardCol in np.sum(testArray[index], axis=1):
                    bingoCardsSet.add(index)

    '''
    @description
    Method to check how many players reached bingo for 'n' number of simulations
    @parameter
    cardsArray- An array equal to size of cards array.
    inputToValueDict - Dictionary with the user input values.
    indicesOfFreeCellDict- The dictionary of all the indices (row, column) for free cells
    @return
    numOfWinnersDict - Dictionary mapping each turn to the total number of winners at that turn in each simulation
    '''

    def CountSimulations(self, cardsArray, inputToValueDict, indicesOfFreeCellDict):
        numOfWinnersDict = defaultdict(list)
        loopVariable = 1
        while loopVariable <= inputToValueDict[self.bingoConstantsClassInstance.SIMULATIONS]:
            # To generate user specified bingo card numbers from lower range to upper range and storing it after shuffling in random order. 
            self.bingoNumbers = np.arange(
                inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS], inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] + 1)
            np.random.shuffle(self.bingoNumbers)
            # testArray(equal to number of cardsArray) is the array with zeros in all cells except -1 for free cells,  
            self.testArray = np.zeros(
                (inputToValueDict[self.bingoConstantsClassInstance.CARDS], inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW], inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]))
            for value in indicesOfFreeCellDict.values():
                self.testArray[:, value[0]-1, value[1]-1] = 1
            self.bingoCardSet = set()
            countCardsSet = set()
            numbersCalled = 1
            for number in self.bingoNumbers:
                countCardsSet = set()
                # To replace the zero in testArray by 1 at the same indice where the bingo number is found in cardsArray. 
                self.testArray[cardsArray == number] = 1
                countCardsSet.update(list((np.where(cardsArray == number))[0]))
                # To check how many cards have reached BINGO after each bingo number being called. 
                if (len(countCardsSet) > 0):
                    self.checkBingo(
                        countCardsSet, self.bingoCardSet, self.testArray, inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW], inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL])
                numOfWinnersDict[numbersCalled].append(len(self.bingoCardSet))
                numbersCalled += 1
            loopVariable += 1
        return numOfWinnersDict
