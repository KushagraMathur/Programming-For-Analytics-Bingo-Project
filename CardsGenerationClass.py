import numpy as np
import random


class CardsGenerationClass:

    '''
    @description
    Method to generate the card numbers in ranges for all the cards.
    Values are stored in a column to list of array dictionary.
    @parameter
    numberOfCards - The number of cards for which elements are to be generated.
    cardRanges - The Dictionary containing the column index to max range of elements allowed for column.
    @return
    cardValuesDict - Values are stored in a column to list of array dictionary
    '''

    def generateCardElements(self, numberOfCards, cardRanges):
        start = 1
        cardValuesDict = dict()
        columnValuesSet = set()
        for key, value in cardRanges.items():
            columnValuesSet = set()
            while len(columnValuesSet) != numberOfCards:
                randomList = random.sample(range(start, value+1), 5)
                columnValuesSet.add(tuple(randomList))
            cardValuesDict[key] = [np.asarray(
                arrayValue) for arrayValue in columnValuesSet]
            start = value+1
        return cardValuesDict

    '''
    @description
    Method to generate the total number of cards.
    @parameter
    numberOfCards - The number of cards to be are to be generated.
    @return
    cardsArray - The array of cards generated.
    '''

    def generateCards(self, numberOfCards):
        cardRanges = {0: 15, 1: 30, 2: 45, 3: 60, 4: 75}
        cardsArray = np.empty([numberOfCards, 5, 5])
        cardValuesDict = self.generateCardElements(numberOfCards, cardRanges)
        for index in range(0, numberOfCards):
            for column in range(5):
                cardsArray[index][:, column] = cardValuesDict[column][index]
        cardsArray[:, 2, 2] = -1
        print(cardsArray)
        return cardsArray
