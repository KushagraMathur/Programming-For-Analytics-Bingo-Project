import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy.stats
import pandas as pd

'''
@description
GraphPlottingClass - Class which contains the results display logic like plot creation and extra statistics calculations.
'''


class GraphPlottingClass:
    '''
    @description
    Method for plotting the line graph for total numbers called vs the number of winners.
    @parameter
    numOfWinnersDict - Dictionary containing the total numbers called to the list of winners at each turn for each simulation.
    '''

    def plotLineGraph(self, numOfWinnersDict):
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
        CentralityDataDict = {"Median": medianValueDict, "Standard Deviation": standardDeviationValueDict, "Skew": skewValueDict,
                              "Kurtosis": kurtosisValueDict, "25th Percentile": firstQuartileValueDict, "50th Percentile": secondQuartileValueDict, "75th Percentile": thirdQuartileValueDict}
        data = pd.DataFrame(CentralityDataDict)
        data['Skew'] = data['Skew'].replace(np.nan, "nan")
        data['Kurtosis'] = data['Kurtosis'].replace(np.nan, "nan")
        data.to_excel('Centrality_Data.xlsx')

        plt.fill_between(listOfTurns, listOfPosStdDevValues,
                         listOfNegStdDevValues, color='skyblue', alpha=0.5)
        plt.plot(listOfTurns, listOfMaxValues, color='skyblue', alpha=0.5, linestyle='dashed')
        plt.plot(listOfTurns, listOfMinValues, color='skyblue', alpha=0.5, linestyle='dashed')
        plt.plot(listOfTurns, listOfAverageValues, color='blue')
        plt.ylabel('Winners')
        plt.xlabel('Total Numbers Called')
        plt.title('Number of winners per number called')
        plt.show()
