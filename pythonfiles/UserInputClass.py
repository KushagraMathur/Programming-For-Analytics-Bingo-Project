class Error(Exception):
    '''Base class for other exceptions '''
    pass

class IncorrectValue(Error):
    '''Raised when the input value for number of free cells is not an integer value'''
    pass

class ValueTooLarge(Error):
    '''Raised when the input value for number of free cells is greater than total number of cells in a bingo card'''
    pass

class UserInputClass:
    '''
    @description
    Method to accept values from user.
    @return
    numberOfCards - The number of cards to be generated.
    '''

    def takingInputsFromUser(self, inputToValueDict):
        for inputVariable in inputToValueDict.keys():
            check = 0
            while check == 0:
                try:
                    print('Enter the number of', inputVariable, ':')
                    userInput = int(input())
                    if userInput < 1 and inputVariable != "numOfFreeCells":
                        raise IncorrectValue
                    if inputVariable == "numOfFreeCells":
                        if userInput > inputToValueDict['sizeOfCard']*inputToValueDict['sizeOfCard']:
                            raise ValueTooLarge
                        elif userInput < 0:
                            raise IncorrectValue
                    check = 1
                    inputToValueDict[inputVariable] = userInput
                except (IncorrectValue, ValueError):
                    print('Incorrect number of', inputVariable,
                          'entered. Value can be only positive integer values greater than 0.')
                    check = 0
                except ValueTooLarge:
                    print(
                        'Incorrect number of free cells entered. Number of free cells cannot be grater than size of card.')
                    check = 0
        return inputToValueDict
    
    def takingIndicesForFreeCells(self, numOfFreeCells, indicesOfFreeCellDict):
        for key in range(0, numOfFreeCells):
            for indice in ['row', 'column']:
                check = 0
                while check == 0:
                    try:
                        print('Enter the indice for ', indice,
                              ' for free cell no. ', key+1, ':')
                        userInput = int(input())
                        if userInput < 0:
                            raise Exception()
                        check = 1
                        indicesOfFreeCellDict[key].append(userInput)
                    except:
                        print('Incorrect indice of', indice,
                              'entered. Value can be only positive integer values greater than or equal to 0.')

        return indicesOfFreeCellDict
