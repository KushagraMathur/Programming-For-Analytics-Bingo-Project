import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy.stats
import pandas as pd
import BingoConstantsClass

'''
@description
GraphPlottingClass - Class which contains the results display logic like plot creation and extra statistics calculations.
'''


class GraphPlottingClass:
    '''
    @description
    Initial constructor method.
    '''

    def __init__(self):
        self.bingoConstantsClassInstance = BingoConstantsClass.BingoConstantsClass()

    '''
    @description
    Method for plotting:
    1. line graph for total numbers called vs the number of winners.
    2. histogram for number of winners in each simulation after x number being called.
    @parameter
    numOfWinnersDict - Dictionary containing the total numbers called to the list of winners at each turn for each simulation.
    inputToValueDict - Dictionary with user input values.
    '''

    def plotLineGraph(self, numOfWinnersDict, inputToValueDict):
        listOfAverageValues = []
        listOfMaxValues = []
        listOfMinValues = []
        listOfPosStdDevValues = []
        listOfNegStdDevValues = []
        listOfTurns = []
        medianValueDict = {}
        skewValueDict = {}
        kurtosisValueDict = {}
        firstQuartileValueDict = {}
        secondQuartileValueDict = {}
        thirdQuartileValueDict = {}
        standardDeviationValueDict = {}
        
        '''
        Below "for" loop extracts the number of winners after each number called for all the simulations.Using the number of winners
        we compute average, maximum, minimum, standard deviation, median, kurtosis, skew and percentiles.
        '''
        for key, value in numOfWinnersDict.items():
            numOfWinnersDict[key] = np.array(value)
            listOfAverageValues.append(np.average(numOfWinnersDict[key]))
            listOfMaxValues.append(np.amax(numOfWinnersDict[key]))
            listOfMinValues.append(np.amin(numOfWinnersDict[key]))
            listOfPosStdDevValues.append(np.average(
                numOfWinnersDict[key]) + np.std(numOfWinnersDict[key]))
            listOfNegStdDevValues.append(np.average(
                numOfWinnersDict[key]) - np.std(numOfWinnersDict[key]))
            listOfTurns.append(key)
            medianValueDict[key] = statistics.median(value)
            standardDeviationValueDict[key] = statistics.stdev(value)
            skewValueDict[key] = scipy.stats.skew(value)
            kurtosisValueDict[key] = scipy.stats.kurtosis(value)
            firstQuartileValueDict[key] = np.percentile(value, 25)
            secondQuartileValueDict[key] = np.percentile(value, 50)
            thirdQuartileValueDict[key] = np.percentile(value, 75)
        # creating a dictionary which contains values like median, standard deviation, skew, kurtosis and percentiles.
        CentralityDataDict = {"Median": medianValueDict, "Standard Deviation": standardDeviationValueDict, "Skew": skewValueDict,
                              "Kurtosis": kurtosisValueDict, "25th Percentile": firstQuartileValueDict, "50th Percentile": secondQuartileValueDict, "75th Percentile": thirdQuartileValueDict}
       
        # Convert the dictionary into panda data frame in order to export the centrality data.
        data = pd.DataFrame(CentralityDataDict)
        
        # For some of the values we get Skew and Kurtosis as nan (Not a Number). below code will replace the empty cells in excel as "nan".
        data['Skew'] = data['Skew'].replace(np.nan, "nan")
        data['Kurtosis'] = data['Kurtosis'].replace(np.nan, "nan")
        
        # export the centrality data to an excel file.
        data.to_excel('Centrality_Data.xlsx')
        
        # Below code creates two subplots, one for the line graph and other for the histogram.

        # Creating line graph.
        plt.subplot(1, 2, 1)
        plt.fill_between(listOfTurns, listOfPosStdDevValues,
                         listOfNegStdDevValues, color='skyblue', alpha=0.5)
        plt.plot(listOfTurns, listOfMaxValues, color='skyblue',
                 alpha=0.5, linestyle='dashed')
        plt.plot(listOfTurns, listOfMinValues, color='skyblue',
                 alpha=0.5, linestyle='dashed')
        plt.plot(listOfTurns, listOfAverageValues, color='blue')
        plt.ylabel('Winners')
        plt.xlabel('Total Numbers Called')
        plt.title('Number of winners per number called')

        # Creating histogram.
        plt.subplot(1, 2, 2)
        plt.hist(numOfWinnersDict[inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_NUMBERS]],
                 inputToValueDict[self.bingoConstantsClassInstance.CARDS])
        plt.ylabel('Frequency of Winners')
        plt.xlabel('Numbers of Winners')
        plt.title(
            "Number of winners in each simulation after calling " + str(inputToValueDict[self.bingoConstantsClassInstance.NUMBER_OF_NUMBERS]) + " numbers")
        plt.tight_layout()
        
        # Convert both the grapsh obtained into a jpeg image.
        plt.gcf().set_size_inches(18.5, 10.5)
        plt.savefig('Graphs.jpeg')
        plt.show()
