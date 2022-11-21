import UserInputClass
import CardsGenerationClass
import SimulationClass
import PdfGenerationClass
import GraphPlottingClass
from collections import defaultdict, OrderedDict

class CallingClass:
    def run(self):
        self.inputToValueDict = {'cards': 0, 'simulations': 0, 'sizeOfCard': 0, 'numOfFreeCells': 0}
        self.inputToValueDict = UserInputClass.UserInputClass(
        ).takingInputsFromUser(self.inputToValueDict)
        self.indicesOfFreeCellDict = defaultdict(list)        
        self.indicesOfFreeCellDict = UserInputClass.UserInputClass(
        ).takingIndicesForFreeCells(self.inputToValueDict['numOfFreeCells'], self.indicesOfFreeCellDict, self.inputToValueDict['sizeOfCard'])        
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict['cards'], self.inputToValueDict['sizeOfCard'], self.indicesOfFreeCellDict)        
        PdfGenerationClass.PdfGenerationClass().CreatePdf(self.cardsArray, self.inputToValueDict['sizeOfCard'])
        self.numOfWinnersDict = SimulationClass.SimulationsClass().CountSimulations(
            self.inputToValueDict['cards'], self.cardsArray, self.inputToValueDict['simulations'], self.inputToValueDict['sizeOfCard'], self.indicesOfFreeCellDict)
        GraphPlottingClass.GraphPlottingClass().plotLineGraph(self.numOfWinnersDict)


if __name__ == "__main__":
    CallingClass().run()
