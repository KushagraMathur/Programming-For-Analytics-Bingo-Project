class UserInputClass:

    '''
    @description
    Method to accept values from user.
    @return
    numberOfCards - The number of cards to be generated.
    '''

    def takingInputsFormUser(self, inputToValueDict):
        for inputVariable in inputToValueDict.keys():
            check = 0
            while check == 0:
                try:
                    print('Enter the number of', inputVariable, ':')
                    userInput = int(input())
                    if userInput < 1:
                        raise Exception()
                    check = 1
                    inputToValueDict[inputVariable] = userInput
                except:
                    print('Incorrect number of', inputVariable,
                        'entered. Value can be only positive integer values greater than 0.')
                    check = 0
        return inputToValueDict
