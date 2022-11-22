import numpy as np
from collections import defaultdict


class SimulationsClass:
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
    numberOfCards - The number of cards created by user.
    cardsArray- An array equal to size of cards array.
    numOfSim- The number of simulations entered by user.
    sizeOfCardRow- The number of rows in a card specified by user.
    sizeOfCardCol- The number of columns in a card specified by user.
    indicesOfFreeCellDict- 
    lowerRangeOfCardNo- 
    upperRangeOfCardNo- 
    '''

    def CountSimulations(self, numberOfCards, cardsArray, numOfSim, sizeOfCardRow, sizeOfCardCol, indicesOfFreeCellDict, lowerRangeOfCardNo, upperRangeOfCardNo):
        numOfWinnersDict = defaultdict(list)
        loopVariable = 1
        while loopVariable <= numOfSim:
            self.bingoNumbers = np.arange(lowerRangeOfCardNo, upperRangeOfCardNo + 1)
            np.random.shuffle(self.bingoNumbers)
            self.testArray = np.zeros((numberOfCards, sizeOfCardRow, sizeOfCardCol))
            for value in indicesOfFreeCellDict.values():
                self.testArray[:, value[0]-1, value[1]-1] = 1
            self.bingoCardSet = set()
            countCardsSet = set()
            numbersCalled = 1
            for number in self.bingoNumbers:
                countCardsSet = set()
                self.testArray[cardsArray == number] = 1
                countCardsSet.update(list((np.where(cardsArray == number))[0]))
                if (len(countCardsSet) > 0):
                    self.checkBingo(
                        countCardsSet, self.bingoCardSet, self.testArray, sizeOfCardRow, sizeOfCardCol)
                numOfWinnersDict[numbersCalled].append(len(self.bingoCardSet))
                numbersCalled += 1
            loopVariable += 1
        return numOfWinnersDict
