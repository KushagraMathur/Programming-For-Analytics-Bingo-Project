import UserInputClass
import CardsGenerationClass
import numpy as np
import random
from collections import defaultdict


class Simulations:
    def CountSimulations(self, numberOfCards, cardsArray):

        simulationSet = defaultdict(list)
        numOfSim = 10
        while numOfSim != 0:

            # Check for random nos function
            self.bingoNumbers = np.arange(1, 76)
            np.random.shuffle(self.bingoNumbers)

            self.testArray = np.zeros((numberOfCards, 5, 5))
            self.testArray[:, 2, 2] = 1

            bingoCardsSet = set()
            # [10,4,6,8,1,3,75]
            countCardsSet = set()
            numbersCalled = 1
            for number in self.bingoNumbers:
                countCardsSet = set()
                # [0,1,2,3,4,5.......]
                self.testArray[cardsArray == number] = 1
                for index in range(0, numberOfCards):
                    # (24,25)  (25,26,27)
                    if number in cardsArray[index]:
                        countCardsSet.add(index)

                for index in countCardsSet:
                    for row in range(0, 5):
                        if self.testArray[index, row].sum() == 5:
                            bingoCardsSet.add(index)
                        elif self.testArray[index, :, row].sum() == 5:
                            bingoCardsSet.add(index)

                    if np.diagonal(self.testArray[index]).sum() == 5:
                        bingoCardsSet.add(index)
                    elif (self.testArray[index, 0, 4] + self.testArray[index, 1, 3] + self.testArray[index, 2, 2] + self.testArray[index, 3, 1] + self.testArray[index, 4, 0]) == 5:
                        bingoCardsSet.add(index)

                simulationSet[numbersCalled].append(len(bingoCardsSet))
                numbersCalled += 1
            numOfSim -= 1

        for key, value in simulationSet.items():
            print(key, ' : ', value)

            # print(simulationSet)
        # print('After callin ', a,
        #       ' numbers there are :', len(bingoCardsSet), ' winners')
        #
