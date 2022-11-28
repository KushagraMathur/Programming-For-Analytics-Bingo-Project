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
        self.welcomeText1 = tk.Label(
            master, text='Hello!! Welcome to', background='skyblue', font='Helvetica 16 bold', wraplength=500, justify='left')
        self.welcomeText1.grid(row=0, column=0, sticky='e')
        self.welcomeText2 = tk.Label(
            master, text='the BINGO simulator', background='skyblue', font='Helvetica 16 bold', wraplength=500, justify='left')
        self.welcomeText2.grid(row=0, column=1, sticky='w')
        self.detailsText1 = tk.Label(
            master, text='Please enter the below details to', background='skyblue', font='Helvetica 16 bold', wraplength=500, justify='left')
        self.detailsText1.grid(row=1, column=0, sticky='e')
        self.detailsText2 = tk.Label(
            master, text='simulate a game of BINGO', background='skyblue', font='Helvetica 16 bold', wraplength=500, justify='left')
        self.detailsText2.grid(row=1, column=1, sticky='w')

        numOfCardsLabel = tk.Label(
            master, text='Number of Cards: ', background='skyblue', font='Helvetica 9 bold')
        self.numOfCardsEntry = tk.Entry(master, textvariable=numOfCardsLabel)
        numOfCardsLabel.grid(row=2, column=0, sticky='e')
        self.numOfCardsEntry.grid(row=2, column=1, sticky='e')

        numOfSimulationLabel = tk.Label(
            master, text='Number of Simulations: ', background='skyblue', font='Helvetica 9 bold')
        self.numOfSimulationsEntry = tk.Entry(
            master, textvariable=numOfSimulationLabel)
        numOfSimulationLabel.grid(row=3, column=0, sticky='e')
        self.numOfSimulationsEntry.grid(row=3, column=1, sticky='e')

        numOfCardRowsLabel = tk.Label(
            master, text='Number of rows in the card: ', background='skyblue', font='Helvetica 9 bold')
        self.numOfCardRowsEntry = tk.Entry(
            master, textvariable=numOfCardRowsLabel)
        numOfCardRowsLabel.grid(row=4, column=0, sticky='e')
        self.numOfCardRowsEntry.grid(row=4, column=1, sticky='e')

        numOfCardColumnsLabel = tk.Label(
            master, text='Number of columns in the card: ', background='skyblue', font='Helvetica 9 bold')
        self.numOfCardColumnsEntry = tk.Entry(
            master, textvariable=numOfCardColumnsLabel)
        numOfCardColumnsLabel.grid(row=5, column=0, sticky='e')
        self.numOfCardColumnsEntry.grid(row=5, column=1, sticky='e')

        lowerRangeNumberLabel = tk.Label(
            master, text='Enter the lower range of numbers: ', background='skyblue', font='Helvetica 9 bold')
        self.lowerRangeNumberEntry = tk.Entry(
            master, textvariable=lowerRangeNumberLabel)
        lowerRangeNumberLabel.grid(row=6, column=0, sticky='e')
        self.lowerRangeNumberEntry.grid(row=6, column=1, sticky='e')

        upperRangeNumberLabel = tk.Label(
            master, text='Enter the upper range of numbers: ', background='skyblue', font='Helvetica 9 bold')
        self.upperRangeNumberEntry = tk.Entry(
            master, textvariable=upperRangeNumberLabel)
        upperRangeNumberLabel.grid(row=7, column=0, sticky='e')
        self.upperRangeNumberEntry.grid(row=7, column=1, sticky='e')

        numberOfNumbersLabel = tk.Label(
            master, text='Enter the number of numbers for histogram: ', background='skyblue', font='Helvetica 9 bold')
        self.numberOfNumbersEntry = tk.Entry(
            master, textvariable=numberOfNumbersLabel)
        numberOfNumbersLabel.grid(row=8, column=0, sticky='e')
        self.numberOfNumbersEntry.grid(row=8, column=1, sticky='e')

        numOfFreeCellsLabel = tk.Label(
            master, text='Number of free cells: ', background='skyblue', font='Helvetica 9 bold')
        self.numOfFreeCellsEntry = tk.Entry(
            master, textvariable=numOfFreeCellsLabel)
        numOfFreeCellsLabel.grid(row=9, column=0, sticky='e')
        self.numOfFreeCellsEntry.grid(row=9, column=1, sticky='e')

        imageUrlLabel = tk.Label(
            master, text='Enter the image URL: ', background='skyblue', font='Helvetica 9 bold')
        self.imageUrlEntry = tk.Entry(
            master, textvariable=imageUrlLabel)
        imageUrlLabel.grid(row=10, column=0, sticky='e')
        self.imageUrlEntry.grid(row=10, column=1, sticky='e')

        posOfFreeCellsText = tk.Label(
            master, text='Please enter the rows and columns indexes of the free cells. For multiple free cells, separate indexes by commas. Ex Rows: 1,3,5 Columns: 2,4,3 ', background='skyblue', font='Helvetica 9 bold', wraplength=400, justify='left')
        posOfFreeCellsText.grid(row=11, column=0, sticky='w')

        rowLabel = tk.Label(
            master, text='Free Cell Rows: ', background='skyblue', font='Helvetica 9 bold')
        self.freeCellRowsEntry = tk.Entry(master, textvariable=rowLabel)
        rowLabel.grid(row=12, column=0, sticky='e')
        self.freeCellRowsEntry.grid(row=12, column=1)

        columnLabel = tk.Label(
            master, text='Free Cell Columns: ', background='skyblue', font='Helvetica 9 bold')
        self.freeCellColumnsEntry = tk.Entry(master, textvariable=columnLabel)
        columnLabel.grid(row=12, column=2)
        self.freeCellColumnsEntry.grid(row=12, column=3)

        buttonInfoText = tk.Label(
            master, text='The Generate Cards Button will generate the Bingo cards. Run simulations will run Bingo game simualtions.', background='skyblue', font='Helvetica 9 bold', wraplength=400, justify='left')
        buttonInfoText.grid(row=13, column=0, sticky='w')

        generateCardsButton = tk.Button(
            master, text='Generate Cards', command=self.validateDataAndGenerateCards)
        generateCardsButton.grid(row=20, column=1)

        runSimulationsButton = tk.Button(
            master, text='Run Simulations', command=self.runSimualtionsForCards)
        runSimulationsButton.grid(row=20, column=3)

        self.quitButton = tk.Button(
            master, text='Quit Program', command=self.quit)
        self.quitButton.grid(row=30, column=2)
        self.callingClassInstance = CallingClass.CallingClass(
            self.inputToValueDict, self.indicesOfFreeCellDict)

    '''
    @description
    Method to validate the user inputs and then create cards and PDF.
    If any error is found, user must re-enter data till correct data is provided.
    '''

    def validateDataAndGenerateCards(self):
        # Performing validation checks on user data. If a failure is found, user must enter details again.
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
                    message='Incorrect value has been entered. Please re-check the inputs. Error: '+str(e))
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
                        message='Value of free cell row or column is too large. Value should be <= size of the row or column')
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
                message='There is an error in the cards generation. Error: '+str(e))
        return

    '''
    @description
    Method to run the simulation and display the simulation results once the cards are generated.
    '''

    def runSimualtionsForCards(self):
        # Run the simulations and the graph plotting functionality
        try:
            if len(self.cardsArray) > 0:
                self.numOfWinnersDict = self.callingClassInstance.runSimulations(
                    self.cardsArray)
                self.callingClassInstance.plottingTheGraphs(
                    self.numOfWinnersDict, self.inputToValueDict)
                messagebox.showinfo(
                    message='Success!! Your simulations have run successfully. More information on the simulations is available in an Excel file and the graphs can be found as images')
            else:
                messagebox.showerror(
                    message='Please generate cards before running simulations')
                return
        except Exception as e:
            messagebox.showerror(
                message='An error occured in the simulations. Error: '+str(e))
            return

    '''
    @description
    Method to quit the program.
    '''

    def quit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x500")
    root.configure(background='skyblue')
    TKinterGUIClass(root)
    root.mainloop()
