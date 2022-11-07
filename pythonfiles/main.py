import UserInputClass
import CardsGenerationClass


class CallingClass:
    def run(self):
        self.numberOfCards = UserInputClass.UserInputClass().takingInputsFormUser()
        cardsArray = CardsGenerationClass.CardsGenerationClass(
        ).generateCards(self.numberOfCards)


if __name__ == "__main__":
    CallingClass().run()
