import UserInputClass
import CardsGenerationClass
import SimulationClass
import PdfGenerationClass
import GraphPlottingClass
from collections import defaultdict, OrderedDict

class CallingClass:
    def run(self):
        self.inputToValueDict = OrderedDict({'cards': 0, 'simulations': 0, 'sizeOfCardRow': 0, 'sizeOfCardCol': 0, 'lowerRangeOfCardNo': 0, 'upperRangeOfCardNo': 0, 'imageURL': 0, 'numbersCalledForHistogram': 0, 'numOfFreeCells': 0})
        self.inputToValueDict = UserInputClass.UserInputClass(
        ).takingInputsFromUser(self.inputToValueDict)
        self.indicesOfFreeCellDict = defaultdict(list)        
        self.indicesOfFreeCellDict = UserInputClass.UserInputClass(
        ).takingIndicesForFreeCells(self.inputToValueDict['numOfFreeCells'], self.indicesOfFreeCellDict, self.inputToValueDict['sizeOfCardRow'], self.inputToValueDict['sizeOfCardCol'])        
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict['cards'], self.inputToValueDict['sizeOfCardRow'], self.inputToValueDict['sizeOfCardCol'], self.indicesOfFreeCellDict, self.inputToValueDict['lowerRangeOfCardNo'], self.inputToValueDict['upperRangeOfCardNo'])        
        PdfGenerationClass.PdfGenerationClass().CreatePdf(self.cardsArray, self.inputToValueDict['sizeOfCardRow'], self.inputToValueDict['sizeOfCardCol'], self.inputToValueDict['imageURL'])
        self.numOfWinnersDict = SimulationClass.SimulationsClass().CountSimulations(
            self.inputToValueDict['cards'], self.cardsArray, self.inputToValueDict['simulations'], self.inputToValueDict['sizeOfCardRow'], self.inputToValueDict['sizeOfCardCol'], self.indicesOfFreeCellDict,  self.inputToValueDict['lowerRangeOfCardNo'], self.inputToValueDict['upperRangeOfCardNo'])
        GraphPlottingClass.GraphPlottingClass().plotLineGraph(self.numOfWinnersDict)


if __name__ == "__main__":
    CallingClass().run()
