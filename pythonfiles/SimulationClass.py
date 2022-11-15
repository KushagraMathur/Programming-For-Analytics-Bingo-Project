import numpy as np
from collections import defaultdict
import UserInputClass


class SimulationsClass:
    '''
    @description
    Method to check how many players reached bingo after every number called
    @parameter
    countCardsSet- Contains the indices of cards that might have reached bingo after every number being called.
    bingoCardsSet- Contains the indices of cards that have reached bingo.
    testArray- An array equal to size of cards array. Contains one(1) for free cells and zeros(0) for others. 
               Zeros are replaced by ones if a number is found in cards array.
    sizeOfCard- The size of card specified by user.
    '''

    def checkBingo(self, countCardsSet, bingoCardsSet, testArray, sizeOfCard):
        for index in countCardsSet:
            if np.diagonal(self.testArray[index]).sum() == sizeOfCard:
                bingoCardsSet.add(index)
            elif (np.diag(np.fliplr(self.testArray[index])).sum()) == sizeOfCard:
                bingoCardsSet.add(index)
            if index in bingoCardsSet:
                continue
            for row in range(0, sizeOfCard):
                if self.testArray[index, row].sum() == sizeOfCard:
                    bingoCardsSet.add(index)
                elif self.testArray[index, :, row].sum() == sizeOfCard:
                    bingoCardsSet.add(index)

    '''
    @description
    Method to check how many players reached bingo for 'n' number of simulations
    @parameter
    numberOfCards - The number of cards created by user.
    cardsArray- An array equal to size of cards array.
    numOfSim- The number of simulations entered by user.
    sizeOfCard- The size of card specified by user.
    '''

    def CountSimulations(self, numberOfCards, cardsArray, numOfSim, sizeOfCard):
        numOfWinnersDict = defaultdict(list)
        loopVariable = 1
        while loopVariable <= numOfSim:
            self.bingoNumbers = np.arange(1, sizeOfCard*sizeOfCard*3+1)
            np.random.shuffle(self.bingoNumbers)
            self.testArray = np.zeros((numberOfCards, sizeOfCard, sizeOfCard))
            self.testArray[:, 2, 2] = 1
            self.bingoCardSet = set()
            countCardsSet = set()
            numbersCalled = 1
            for number in self.bingoNumbers:
                countCardsSet = set()
                self.testArray[cardsArray == number] = 1
                countCardsSet.update(list((np.where(cardsArray == number))[0]))
                self.checkBingo(
                    countCardsSet, self.bingoCardSet, self.testArray, sizeOfCard)
                numOfWinnersDict[numbersCalled].append(len(self.bingoCardSet))
                numbersCalled += 1
            loopVariable += 1
        for key, value in numOfWinnersDict.items():
            print(key, ' : ', value)
        return numOfWinnersDict
