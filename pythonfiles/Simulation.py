import numpy as np
from collections import defaultdict
import UserInputClass


class Simulations:
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

    def CountSimulations(self, numberOfCards, cardsArray, numOfSim):
        simulationSet = defaultdict(list)
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
                for index in range(0, numberOfCards):
                    if number in cardsArray[index]:
                        countCardsSet.add(index)

                self.checkBingo(
                    countCardsSet, self.bingoCardSet, self.testArray)

                simulationSet[numbersCalled].append(len(self.bingoCardSet))
                numbersCalled += 1
            loopVariable += 1

        for key, value in simulationSet.items():
            print(key, ' : ', value)

        avgWinnersSet = {}
        maxWinnersSet = {}
        minWinnersSet = {}
        for i in range(0, 75):
            avgWinnersSet[i+1] = int(
                sum(list(simulationSet.values())[i])/numOfSim)
            maxWinnersSet[i+1] = max(list(simulationSet.values())[i])
            minWinnersSet[i+1] = min(list(simulationSet.values())[i])

        print('Avg winners')
        for key, value in avgWinnersSet.items():
            print(key, ' : ', value)

        print('Max winners')
        for key, value in maxWinnersSet.items():
            print(key, ' : ', value)

        print('Min winners')
        for key, value in minWinnersSet.items():
            print(key, ' : ', value)

        return simulationSet
