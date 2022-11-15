class Error(Exception):
    '''Base class for other exceptions '''
    pass

class IncorrectValueException(Error):
    '''Raised when the input value for number of free cells is not an integer value'''
    pass

class ValueTooLargeException(Error):
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
                        raise IncorrectValueException
                    if inputVariable == "numOfFreeCells":
                        if userInput > inputToValueDict['sizeOfCard']*inputToValueDict['sizeOfCard']:
                            raise ValueTooLargeException
                        elif userInput < 0:
                            raise IncorrectValueException
                    check = 1
                    inputToValueDict[inputVariable] = userInput
                except (IncorrectValueException, ValueError):
                    print('Incorrect number of', inputVariable,
                          'entered. Value can be only positive integer values greater than 0.')
                    check = 0
                except ValueTooLargeException:
                    print(
                        'Incorrect number of free cells entered. Number of free cells cannot be grater than size of card.')
                    check = 0
        return inputToValueDict
    
    def takingIndicesForFreeCells(self, numOfFreeCells, indicesOfFreeCellDict, sizeOfCard):
        for key in range(0, numOfFreeCells):
            for indice in ['row', 'column']:
                check = 0
                while check == 0:
                    try:
                        print('Enter the indice for ', indice,
                              ' for free cell no. ', key+1, ':')
                        userInput = int(input())
                        if userInput <= 0 or userInput > sizeOfCard:
                            raise Exception()
                        check = 1
                        indicesOfFreeCellDict[key].append(userInput)
                    except:
                        print('Incorrect indice of', indice,
                              'entered. Value can be only positive integer value greater than 0 and less than or equal to size of card.')

        return indicesOfFreeCellDict
