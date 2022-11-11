import UserInputClass
import CardsGenerationClass
import Simulation


class CallingClass:
    def run(self):
        self.numberOfCards = UserInputClass.UserInputClass().takingInputsFormUser()
        self.cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.numberOfCards)
        Simulation.Simulations().CountSimulations(
            self.numberOfCards, self.cardsArray)
        


if __name__ == "__main__":
    CallingClass().run()
