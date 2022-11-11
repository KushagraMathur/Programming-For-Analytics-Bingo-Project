import UserInputClass
import CardsGenerationClass


class CallingClass:
    def run(self):
        self.inputToValueDict = {'cards': 0, 'simulations': 0}
        self.inputToValueDict = UserInputClass.UserInputClass().takingInputsFormUser(self.inputToValueDict)
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.inputToValueDict['cards'])


if __name__ == "__main__":
    CallingClass().run()
