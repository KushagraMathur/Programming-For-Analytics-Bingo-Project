class Error(Exception):
    '''Base class for other exceptions '''
    pass

class IncorrectValueException(Error):
    '''Raised when the input value for number of free cells is not an integer value'''
    pass

class ValueTooLargeException(Error):
    '''Raised when the input value for number of free cells is greater than total number of cells in a bingo card'''
    pass

class numberOutOfRangeException(Error):
    '''Raised when the input value for number of numbers called for generating a histogram is greater than total number range'''
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
                    if inputVariable == 'imageURL':
                        while (inputToValueDict['upperRangeOfCardNo'] - inputToValueDict['lowerRangeOfCardNo']) <= inputToValueDict['sizeOfCardRow']*inputToValueDict['sizeOfCardCol']:
                            print(
                                'Incorrect range of card numbers entered. Number range cannot be smaller or equal to size of card. Pls try again: ')
                            inputToValueDict['lowerRangeOfCardNo'] = int(
                                input('Enter the lower range of card number:'))
                            inputToValueDict['upperRangeOfCardNo'] = int(
                                input('Enter the upper range of card number:'))
                            
                    print('Enter the number of', inputVariable, ':')
                    if inputVariable == 'imageURL':
                        inputToValueDict[inputVariable] = input()
                        check = 1
                        continue
                    else:
                        userInput = int(input())
                        
                    if userInput < 1 and inputVariable != "numOfFreeCells":
                        raise IncorrectValueException
                    if inputVariable == "numOfFreeCells":
                        if userInput > inputToValueDict['sizeOfCard']*inputToValueDict['sizeOfCard']:
                            raise ValueTooLargeException
                        elif userInput < 0:
                            raise IncorrectValueException
                        if inputVariable == 'numbersCalledforHistogram' and userInput > (inputToValueDict['upperRangeOfCardNo'] - inputToValueDict['lowerRangeOfCardNo']):
                            raise numberOutOfRangeException
                    check = 1
                    inputToValueDict[inputVariable] = userInput
                
                except (IncorrectValueException, ValueError):
                    print('Incorrect number of', inputVariable,
                          'entered. Value can be only positive integer values greater than 0.')
                except ValueTooLargeException:
                    print(
                        'Incorrect number of free cells entered. Number of free cells cannot be grater than size of card.')
                except numberOutOfRangeException:
                    print(
                        'Incorrect input for number of number called, value should be within the card numbers range. Pls try again.')
        return inputToValueDict
    
    def takingIndicesForFreeCells(self, numOfFreeCells, indicesOfFreeCellDict, sizeOfCardRow, sizeOfCardCol):
        for key in range(0, numOfFreeCells):
            for indice in ['row', 'column']:
                check = 0
                while check == 0:
                    try:
                        print('Enter the indice for ', indice,
                              ' for free cell no. ', key+1, ':')
                        userInput = int(input())
                        if indice == "row" and (userInput <= 0 or userInput > sizeOfCardRow):
                            raise Exception()
                        elif indice == "column" and (userInput <= 0 or userInput > sizeOfCardCol):
                            raise Exception()
                        check = 1
                        indicesOfFreeCellDict[key].append(userInput)
                    except:
                        print('Incorrect indice of', indice,
                              'entered. Value can be only positive integer value greater than 0 and less than or equal to number of ', indice, 's of a card.')

        return indicesOfFreeCellDict
