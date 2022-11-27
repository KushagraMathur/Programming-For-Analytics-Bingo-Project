import tkinter as tk
from tkinter import messagebox
import CallingClass
import requests
from io import BytesIO
from PIL import Image
from collections import defaultdict, OrderedDict
import BingoConstantsClass


class Error(Exception):
    '''Base class for other exceptions '''
    pass


class IncorrectValueException(Error):
    '''Raised when the input value for number of free cells is not an integer value'''
    pass


class ValueTooLargeException(Error):
    '''Raised when the input value for number of free cells is greater than total number of cells in a bingo card'''
    pass


'''
@description
TKinterGUIClass - Class which contains the GUI creation logic for accepting inputs from user.
'''


class TKinterGUIClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self, master):
        self.master = master
        master.title('BINGO Simulator')
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()
        self.cardsArray = []
        self.numOfWinnersDict = {}
        self.inputToValueDict = {self.bingoConstantsClassInstance.CARDS: 0,
                                 self.bingoConstantsClassInstance.SIMULATIONS: 0,
                                 self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW: 0,
                                 self.bingoConstantsClassInstance.SIZE_OF_CARD_COL: 0,
                                 self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS: 0,
                                 self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS: 0,
                                 self.bingoConstantsClassInstance.NUMBER_OF_NUMBERS: 0,
                                 self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS: 0,
                                 self.bingoConstantsClassInstance.IMAGE_REQUESTED: ''}
        self.indicesOfFreeCellDict = defaultdict(list)

        # Creating the bingo input form
        self.welcomeText = tk.Label(
            master, text='Hello!!, Welcome to the BINGO simulator')
        self.welcomeText.grid(row=0, column=4)
        self.detailsText = tk.Label(
            master, text='Please enter the below details to simulate a game of BINGO')
        self.detailsText.grid(row=1, column=4)

        numOfCardsLabel = tk.Label(
            master, text='Number of Cards: ')
        self.numOfCardsEntry = tk.Entry(master, textvariable=numOfCardsLabel)
        numOfCardsLabel.grid(row=2, column=0)
        self.numOfCardsEntry.grid(row=2, column=1)

        numOfSimulationLabel = tk.Label(
            master, text='Number of Simulations: ')
        self.numOfSimulationsEntry = tk.Entry(
            master, textvariable=numOfSimulationLabel)
        numOfSimulationLabel.grid(row=3, column=0)
        self.numOfSimulationsEntry.grid(row=3, column=1)

        numOfCardRowsLabel = tk.Label(
            master, text='Number of rows in the card: ')
        self.numOfCardRowsEntry = tk.Entry(
            master, textvariable=numOfCardRowsLabel)
        numOfCardRowsLabel.grid(row=4, column=0)
        self.numOfCardRowsEntry.grid(row=4, column=1)

        numOfCardColumnsLabel = tk.Label(
            master, text='Number of columns in the card: ')
        self.numOfCardColumnsEntry = tk.Entry(
            master, textvariable=numOfCardColumnsLabel)
        numOfCardColumnsLabel.grid(row=5, column=0)
        self.numOfCardColumnsEntry.grid(row=5, column=1)

        lowerRangeNumberLabel = tk.Label(
            master, text='Enter the lower range of numbers: ')
        self.lowerRangeNumberEntry = tk.Entry(
            master, textvariable=lowerRangeNumberLabel)
        lowerRangeNumberLabel.grid(row=6, column=0)
        self.lowerRangeNumberEntry.grid(row=6, column=1)

        upperRangeNumberLabel = tk.Label(
            master, text='Enter the upper range of numbers: ')
        self.upperRangeNumberEntry = tk.Entry(
            master, textvariable=upperRangeNumberLabel)
        upperRangeNumberLabel.grid(row=7, column=0)
        self.upperRangeNumberEntry.grid(row=7, column=1)

        numberOfNumbersLabel = tk.Label(
            master, text='Enter the number of numbers for histogram: ')
        self.numberOfNumbersEntry = tk.Entry(
            master, textvariable=numberOfNumbersLabel)
        numberOfNumbersLabel.grid(row=8, column=0)
        self.numberOfNumbersEntry.grid(row=8, column=1)

        numOfFreeCellsLabel = tk.Label(
            master, text='Number of free cells: ')
        self.numOfFreeCellsEntry = tk.Entry(
            master, textvariable=numOfFreeCellsLabel)
        numOfFreeCellsLabel.grid(row=9, column=0)
        self.numOfFreeCellsEntry.grid(row=9, column=1)

        imageUrlLabel = tk.Label(
            master, text='Enter the image URL: ')
        self.imageUrlEntry = tk.Entry(
            master, textvariable=imageUrlLabel)
        imageUrlLabel.grid(row=10, column=0)
        self.imageUrlEntry.grid(row=10, column=1)

        posOfFreeCellsText = tk.Label(
            master, text='Please enter the rows and columns indexes of the free cells. For multiple free cells, separate indexes by commas. Ex Rows: 1,3,5 Columns: 2,4,3 ')
        posOfFreeCellsText.grid(row=11, column=4)

        rowLabel = tk.Label(
            master, text='Rows: ')
        self.freeCellRowsEntry = tk.Entry(master, textvariable=rowLabel)
        rowLabel.grid(row=12, column=0)
        self.freeCellRowsEntry.grid(row=12, column=1)

        columnLabel = tk.Label(
            master, text='Columns: ')
        self.freeCellColumnsEntry = tk.Entry(master, textvariable=columnLabel)
        columnLabel.grid(row=12, column=2)
        self.freeCellColumnsEntry.grid(row=12, column=3)

        buttonInfoText = tk.Label(
            master, text='The Generate Cards Button will generate the Bingo cards. Run simulations will run Bingo game simualtions.')
        buttonInfoText.grid(row=13, column=4)

        generateCardsButton = tk.Button(
            master, text='Generate Cards', command=self.validateDataAndGenerateCards)
        generateCardsButton.grid(row=20, column=2)

        runSimulationsButton = tk.Button(
            master, text='Run Simulations', command=self.runSimualtionsForCards)
        runSimulationsButton.grid(row=20, column=5)

        self.quitButton = tk.Button(
            master, text='Quit Program', command=self.quit)
        self.quitButton.grid(row=30, column=4)
        self.callingClassInstance = CallingClass.CallingClass(
            self.inputToValueDict, self.indicesOfFreeCellDict)

    '''
    @description
    Method to validate the user inputs and then create cards and PDF.
    If any error is found, user must re-enter data till correct data is provided.
    '''

    def validateDataAndGenerateCards(self):
        self.inputToValueDict = OrderedDict({self.bingoConstantsClassInstance.CARDS: self.numOfCardsEntry.get(),
                                             self.bingoConstantsClassInstance.SIMULATIONS: self.numOfSimulationsEntry.get(),
                                             self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW: self.numOfCardRowsEntry.get(),
                                             self.bingoConstantsClassInstance.SIZE_OF_CARD_COL: self.numOfCardColumnsEntry.get(),
                                             self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS: self.lowerRangeNumberEntry.get(),
                                             self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS: self.upperRangeNumberEntry.get(),
                                             self.bingoConstantsClassInstance.NUMBER_OF_NUMBERS: self.numberOfNumbersEntry.get(),
                                             self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS: self.numOfFreeCellsEntry.get(),
                                             self.bingoConstantsClassInstance.IMAGE_REQUESTED: self.imageUrlEntry.get()})
        self.indicesOfFreeCellDict = defaultdict(list)
        for inputVariable in self.inputToValueDict.keys():
            try:
                if inputVariable != self.bingoConstantsClassInstance.IMAGE_REQUESTED:
                    userInput = int(self.inputToValueDict[inputVariable])
                    if userInput < 1 and inputVariable != self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS:
                        raise IncorrectValueException
                    if inputVariable == self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS:
                        if userInput > int(self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW])*int(self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]):
                            raise ValueTooLargeException
                        elif userInput < 0:
                            raise IncorrectValueException
                    self.inputToValueDict[inputVariable] = userInput
            except (IncorrectValueException, ValueError):
                messagebox.showerror(
                    message='Incorrect value of '+inputVariable + ' entered. Value can be only positive integer values greater than 0.')
                return
            except ValueTooLargeException:
                messagebox.showerror(
                    message='Incorrect number of free cells entered. Number of free cells cannot be grater than size of card.')
                return
            except Exception as e:
                messagebox.showerror(
                    message='Incorrect value has been entered. Please re-check the inputs. Error: '+e)
                return
        if self.inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS] != 0:
            try:
                response = requests.get(
                    self.inputToValueDict[self.bingoConstantsClassInstance.IMAGE_REQUESTED])
                imageResponse = Image.open(BytesIO(response.content))
                self.inputToValueDict[self.bingoConstantsClassInstance.IMAGE_REQUESTED] = imageResponse
            except:
                messagebox.showerror(
                    message='Incorrect value entered for image URL. Please enter valid URL')
                return
            if self.freeCellRowsEntry.get() == '' or self.freeCellColumnsEntry.get() == '':
                messagebox.showerror(
                    message='Please provide the free cells index postions')
                return
            rowIndexes = self.freeCellRowsEntry.get().split(',')
            columnIndexes = self.freeCellColumnsEntry.get().split(',')
            if len(rowIndexes) != len(columnIndexes) or len(rowIndexes) != self.inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS] or len(columnIndexes) != self.inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_FREE_CELLS]:
                messagebox.showerror(
                    message='Incorrect values for free cells indexes entered.')
                return
            for index in range(len(rowIndexes)):
                try:
                    userInputRow = int(rowIndexes[index])
                    userInputCol = int(columnIndexes[index])
                    if userInputRow > int(self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW]) or userInputCol > int(self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL]):
                        raise ValueTooLargeException
                    elif userInputRow < 1 or userInputCol < 1:
                        raise IncorrectValueException
                    self.indicesOfFreeCellDict[index].extend(
                        (userInputRow, userInputCol))
                except (IncorrectValueException, ValueError):
                    messagebox.showerror(
                        message='Incorrect value of free cell row,column index. Please re-enter the values')
                    return
                except ValueTooLargeException:
                    messagebox.showerror(
                        message='Value of row or column is too large. Value should be <= size of the row or column')
                    return
        else:
            if len(self.freeCellRowsEntry.get()) or len(self.freeCellColumnsEntry.get()) or len(self.inputToValueDict[self.bingoConstantsClassInstance.IMAGE_REQUESTED]):
                messagebox.showwarning(
                    message='Number of free cells is 0. Free cell positions, image URL will not be considered in Card Generation.')
        rangePerColumn = int((self.inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] -
                             self.inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS] + 1)/self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL])
        maxPossibleCards = 1
        for i in range(self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW]):
            maxPossibleCards = maxPossibleCards*(rangePerColumn)
            rangePerColumn -= 1
        if (self.inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] < self.inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS]):
            messagebox.showerror(
                message='The Upper range value must be greater than lower range value')
            return
        if (self.inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] - self.inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS] + 1) < (self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_ROW]*self.inputToValueDict[self.bingoConstantsClassInstance.SIZE_OF_CARD_COL])*3:
            messagebox.showerror(
                message='Incorrect Number Range values. The Range must be atleast 3 times the size of the card (i.e. 3* Card Row Size * Card Col Size). Please try again.')
            return
        if (self.inputToValueDict[self.bingoConstantsClassInstance.CARDS] > int(maxPossibleCards/2)):
            messagebox.showerror(
                message='Maximum number of cards should be less than '+str(int(maxPossibleCards/2)))
            return
        if (self.inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_NUMBERS] > (self.inputToValueDict[self.bingoConstantsClassInstance.UPPER_RANGE_OF_CARD_NUMBERS] - self.inputToValueDict[self.bingoConstantsClassInstance.LOWER_RANGE_OF_CARD_NUMBERS] + 1)):
            messagebox.showerror(
                message='Incorrect turn for number frequency Histogram. The number must be between one and the difference between upper and lower range of the card numbers')
            return
        if (self.inputToValueDict[self.bingoConstantsClassInstance.SIMULATIONS] < 2):
            messagebox.showerror(
                message='Atleast 2 simulations are required to process variance values. Please re-enter the values.')
            return
        self.callingClassInstance = CallingClass.CallingClass(
            self.inputToValueDict, self.indicesOfFreeCellDict)
        try:
            self.cardsArray = self.callingClassInstance.cardsGeneration()
            if len(self.cardsArray) > 0:
                messagebox.showinfo(
                    message='Success!! Your cards are generated in a pdf file. You can now run the Bingo Simulation')
        except Exception as e:
            messagebox.showerror(
                message='There is an error in the cards generation. Error: '+e)
        return

    '''
    @description
    Method to run the simulation and display the simulation results once the cards are generated.
    '''

    def runSimualtionsForCards(self):
        try:
            if len(self.cardsArray) > 0:
                self.numOfWinnersDict = self.callingClassInstance.runSimulations(
                    self.cardsArray)
                self.callingClassInstance.plottingTheGraphs(
                    self.numOfWinnersDict)
                messagebox.showinfo(
                    message='Success!! Your simulations have run successfully. More information on the simulations is available in an Excel file')
            else:
                messagebox.showerror(
                    message='Please generate cards before running simulations')
                return
        except Exception as e:
            messagebox.showerror(
                message='An error occured in the simulations. Error: '+e)
            return

    '''
    @description
    Method to quit the program.
    '''

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1700x500")
    TKinterGUIClass(root)
    root.mainloop()
