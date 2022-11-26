class SingletonMeta(type):
    """
    Implementing the Singleton metaclass
    """

    _instances = {}

    def __call__(className, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if className not in className._instances:
            instance = super().__call__(*args, **kwargs)
            className._instances[className] = instance
        return className._instances[className]


'''
@description
BingoConstantsClass - Class which contains constants referred in the program.
'''


class BingoConstantsClass(metaclass=SingletonMeta):
    CARDS = 'cards'
    SIMULATIONS = 'simulations'
    SIZE_OF_CARD_ROW = 'sizeOfCardRow'
    SIZE_OF_CARD_COL = 'sizeOfCardCol'
    LOWER_RANGE_OF_CARD_NUMBERS = 'lowerRangeOfCardNo'
    UPPER_RANGE_OF_CARD_NUMBERS = 'upperRangeOfCardNo'
    IMAGE_REQUESTED = 'imageRequested'
    NUMBER_OF_NUMBERS = 'numbersCalledForHistogram'
    NUMBER_OF_FREE_CELLS = 'numOfFreeCells'
