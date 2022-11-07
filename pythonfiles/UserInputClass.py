class UserInputClass:

    '''
    @description
    Method to accept values from user.
    @return
    numberOfCards - The number of cards to be generated.
    '''

    def takingInputsFormUser(self):
        self.numberOfCards = int(
            input('Enter the number of cards to create: '))
        return self.numberOfCards
