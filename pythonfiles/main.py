import UserInputClass
import CardsGenerationClass
import Simulation


class CallingClass:
    def run(self):
        self.inputToValueDict = {'cards': 0, 'simulations': 0}
        self.inputToValueDict = UserInputClass.UserInputClass(
        ).takingInputsFormUser(self.inputToValueDict)
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict['cards'])
        self.simulationSet = Simulation.Simulations().CountSimulations(
            self.inputToValueDict['cards'], self.cardsArray, self.inputToValueDict['simulations'])


if __name__ == "__main__":
    CallingClass().run()
