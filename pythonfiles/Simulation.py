import numpy as np
from collections import defaultdict
import UserInputClass


class Simulations:
    '''
    @description
    Method to check how many players reached bingo for 'n' number of simulations
    @parameter
    numberOfCards - The number of cards created by user.
    cardsArray- An array equal to size of cards array.
    numOfSim- The number of simulations entered by user.
    '''
    def checkBingo(self, countCardsSet, bingoCardsSet, testArray):
        for index in countCardsSet:
            if np.diagonal(self.testArray[index]).sum() == 5:
                bingoCardsSet.add(index)
            elif (np.diag(np.fliplr(self.testArray[index])).sum()) == 5:
                bingoCardsSet.add(index)

            if index in bingoCardsSet:
                continue
            for row in range(0, 5):
                if self.testArray[index, row].sum() == 5:
                    bingoCardsSet.add(index)
                elif self.testArray[index, :, row].sum() == 5:
                    bingoCardsSet.add(index)

     '''
    @description
    Method to check how many players reached bingo for 'n' number of simulations
    @parameter
    numberOfCards - The number of cards created by user.
    cardsArray- An array equal to size of cards array.
    numOfSim- The number of simulations entered by user.
    '''
    def CountSimulations(self, numberOfCards, cardsArray, numOfSim):
        numOfWinnersDict = defaultdict(list)
        loopVariable = 1
        while loopVariable <= numOfSim:
            self.bingoNumbers = np.arange(1, 76)
            np.random.shuffle(self.bingoNumbers)

            self.testArray = np.zeros((numberOfCards, 5, 5))
            self.testArray[:, 2, 2] = 1

            self.bingoCardSet = set()
            countCardsSet = set()
            numbersCalled = 1
            for number in self.bingoNumbers:
                countCardsSet = set()
                self.testArray[cardsArray == number] = 1
                countCardsSet.update(list((np.where(cardsArray == number))[0]))

                self.checkBingo(
                    countCardsSet, self.bingoCardSet, self.testArray)

                numOfWinnersDict[numbersCalled].append(len(self.bingoCardSet))
                numbersCalled += 1
            loopVariable += 1

        for key, value in numOfWinnersDict.items():
            print(key, ' : ', value)

        return numOfWinnersDict
