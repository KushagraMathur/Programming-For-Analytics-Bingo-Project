import numpy as np
import random
import BingoConstantsClass

'''
@description
CardsGenerationClass - Class which contains the card generation logic.
'''


class CardsGenerationClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self):
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()

    '''
    @description
    Method to generate the card numbers in ranges for all the cards.
    Values are stored in a column to list of array dictionary.
    @parameter
    cardRanges - The Dictionary containing the column index to max range of elements allowed for column.
    inputToValueDict - Dictionary with the user input values.
    @return
    cardValuesDict - Values are stored in a column to list of array dictionary
    '''

    def generateCardElements(self, cardRanges, inputToValueDict):
        start = inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS]
        cardValuesDict = {}
        columnValuesSet = set()
        for key, value in cardRanges.items():
            columnValuesSet = set()
            # genereate a set of unquie tuples which contain the values in the range. Continue this till we reach the number of cards.
            while len(columnValuesSet) != inputToValueDict[self.bingoConstantsClassInstance.CARDS]:
                randomList = random.sample(
                    range(start, value+1), inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW])
                columnValuesSet.add(tuple(randomList))
            # Store the unique column values in a dictionary of column to n unique arrays
            cardValuesDict[key] = [np.asarray(
                arrayValue) for arrayValue in columnValuesSet]
            start = value+1
        return cardValuesDict

    '''
    @description
    Method to generate the total number of cards.
    @parameter
    inputToValueDict - Dictionary with the user input values.
    indicesOfFreeCellDict - Dictionary with the free cell indexs
    @return
    cardsArray - The array of cards generated.
    '''

    def generateCards(self, inputToValueDict, indicesOfFreeCellDict):
        cardRanges = {}
        # Set the max range of numbers each column in the array can take
        for number in range(inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]):
            cardRanges[number] = inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS] + \
                int((number+1)*(inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] -
                    inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS]) / inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL])
        cardValuesDict = self.generateCardElements(
            cardRanges, inputToValueDict)
        cardsArray = np.empty([inputToValueDict[self.bingoConstantsClassInstance.CARDS],
                              inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW], inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]])
        # store the column values in the array
        for index in range(0, inputToValueDict[self.bingoConstantsClassInstance.CARDS]):
            for column in range(inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]):
                cardsArray[index][:, column] = cardValuesDict[column][index]
        # set free cell values to -1
        for value in indicesOfFreeCellDict.values():
            cardsArray[:, value[0]-1, value[1]-1] = -1
        return cardsArray
