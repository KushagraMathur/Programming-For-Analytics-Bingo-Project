import CardsGenerationClass
import SimulationClass
import PdfGenerationClass
import GraphPlottingClass
from collections import defaultdict, OrderedDict
import BingoConstantsClass

'''
@description
CallingClass - Class which calls the backend methods for card generation, simulation run and results plotting.
'''


class CallingClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self, inputToValueDict={}, indicesOfFreeCellDict=defaultdict(list)):
        self.inputToValueDict = inputToValueDict
        self.indicesOfFreeCellDict = indicesOfFreeCellDict
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()

    '''
    @description
    Method to related to card generation process.
    Cards and first generated in numpy array and then printed in PDF file.
    @return
    cardsArray - Numpy array with the unique generated cards
    '''

    def cardsGeneration(self):
        cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict, self.indicesOfFreeCellDict)
        PdfGenerationClass.PdfGenerationClass().CreatePdf(
            cardsArray, self.inputToValueDict)
        return cardsArray

    '''
    @description
    Method to run the Bingo simulation on the generated cards.
    @parameter
    cardsArray - Numpy array with the unique generated cards
    @return
    numOfWinnersDict - Dictionary mapping each turn to the total number of winners at that turn in each simulation
    '''

    def runSimulations(self, cardsArray):
        numOfWinnersDict = SimulationClass.SimulationsClass(
        ).CountSimulations(cardsArray, self.inputToValueDict, self.indicesOfFreeCellDict)
        return numOfWinnersDict

    '''
    @description
    Method to display the results of the simulations
    @parameter
    numOfWinnersDict - Dictionary mapping each turn to the total number of winners at that turn in each simulation.
    inputToValueDict - Dictionary with user input values.
    '''

    def plottingTheGraphs(self, numOfWinnersDict, inputToValueDict):
        GraphPlottingClass.GraphPlottingClass().plotLineGraph(
            numOfWinnersDict, inputToValueDict)
