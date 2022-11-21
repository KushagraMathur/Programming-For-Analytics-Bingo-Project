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

    def generateCardElements(self, numberOfCards, cardRanges, sizeOfCardRow, lowerRangeOfCardNo):
        start = lowerRangeOfCardNo
        cardValuesDict = dict()
        columnValuesSet = set()
        for key, value in cardRanges.items():
            columnValuesSet = set()
            while len(columnValuesSet) != numberOfCards:
                randomList = random.sample(range(start, value+1), sizeOfCardRow)
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

    def generateCards(self, numberOfCards, sizeOfCardRow, sizeOfCardCol, indicesOfFreeCellDict, lowerRangeOfCardNo, upperRangeOfCardNo):
        cardRanges = {}
        for number in range(sizeOfCardCol):
            cardRanges[number] = lowerRangeOfCardNo + int((number+1)*(upperRangeOfCardNo - lowerRangeOfCardNo) / sizeOfCardCol)
        cardValuesDict = self.generateCardElements(numberOfCards, cardRanges, sizeOfCardRow, lowerRangeOfCardNo)
        cardsArray = np.empty([numberOfCards, sizeOfCardRow, sizeOfCardCol])
        for index in range(0, numberOfCards):
            for column in range(sizeOfCardCol):
                cardsArray[index][:, column] = cardValuesDict[column][index]
        for value in indicesOfFreeCellDict.values():
            cardsArray[:, value[0]-1, value[1]-1] = -1
        return cardsArray
