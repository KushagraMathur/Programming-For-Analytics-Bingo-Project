import UserInputClass
import CardsGenerationClass
import SimulationClass
import PdfGenerationClass
import GraphPlottingClass


class CallingClass:
    def run(self):
        self.inputToValueDict = {'cards': 0, 'simulations': 0}
        self.inputToValueDict = UserInputClass.UserInputClass(
        ).takingInputsFromUser(self.inputToValueDict)
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict['cards'])
        PdfGenerationClass.PdfGenerationClass().CreatePdf(self.cardsArray)
        self.numOfWinnersDict = SimulationClass.SimulationsClass().CountSimulations(
            self.inputToValueDict['cards'], self.cardsArray, self.inputToValueDict['simulations'])
        GraphPlottingClass.GraphPlottingClass().plotLineGraph(self.numOfWinnersDict)


if __name__ == "__main__":
    CallingClass().run()
