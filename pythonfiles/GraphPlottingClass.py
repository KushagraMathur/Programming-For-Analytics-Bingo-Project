import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy.stats
import pandas as pd


class GraphPlottingClass:
    '''
    @description
    Method for plotting the line graph for total numbers called vs the number of winners.
    @parameter
    numOfWinnersDict - Dictionary containing the total numbers called to the list of winners at each turn for each simulation.
    '''

    def plotLineGraph(self, numOfWinnersDict):
        listOfAverageValues = list()
        listOfMaxValues = list()
        listOfMinValues = list()
        listOfPosStdDevValues = list()
        listOfNegStdDevValues = list()
        numberOfCards = list()
        MedianValueDict = {}
        SkewValueDict = {}
        KurtosisValueDict = {}
        FirstQuartileValueDict = {}
        SecondQuartileValueDict = {}
        ThirdQuartileValueDict = {}
        StandardDeviationValueDict = {}
        for key, value in numOfWinnersDict.items():
            numOfWinnersDict[key] = np.array(value)
            listOfAverageValues.append(np.average(numOfWinnersDict[key]))
            listOfMaxValues.append(np.amax(numOfWinnersDict[key]))
            listOfMinValues.append(np.amin(numOfWinnersDict[key]))
            listOfPosStdDevValues.append(np.average(
                numOfWinnersDict[key]) + np.std(numOfWinnersDict[key]))
            listOfNegStdDevValues.append(np.average(
                numOfWinnersDict[key]) - np.std(numOfWinnersDict[key]))
            numberOfCards.append(key)
            MedianValueDict[key] = statistics.median(value)
            StandardDeviationValueDict[key] = statistics.stdev(value)
            SkewValueDict[key] = scipy.stats.skew(value)
            KurtosisValueDict[key] = scipy.stats.kurtosis(value)
            FirstQuartileValueDict[key] = np.percentile(value, 25)
            SecondQuartileValueDict[key] = np.percentile(value, 50)
            ThirdQuartileValueDict[key] = np.percentile(value, 75)
        CentralityDataDict = {"Median": MedianValueDict, "Standard Deviation": StandardDeviationValueDict, "Skew": SkewValueDict,
                   "Kurtosis": KurtosisValueDict, "25th Percentile": FirstQuartileValueDict, "50th Percentile":SecondQuartileValueDict, "75th Percentile": ThirdQuartileValueDict}
        data = pd.DataFrame(CentralityDataDict)
        data['Skew'] = data['Skew'].replace(np.nan, "nan")
        data['Kurtosis'] = data['Kurtosis'].replace(np.nan, "nan")
        data.to_excel('Centrality_Data.xlsx')
        print("The data is exported to excel file successfully")
        
        plt.plot(numberOfCards, listOfAverageValues)
        plt.plot(numberOfCards, listOfPosStdDevValues)
        plt.plot(numberOfCards, listOfNegStdDevValues)
        plt.fill_between(numberOfCards, listOfPosStdDevValues,
                         listOfNegStdDevValues, color='cyan', alpha=0.5)
        plt.plot(numberOfCards, listOfMaxValues, linestyle='dashed')
        plt.plot(numberOfCards, listOfMinValues, linestyle='dashed')
        plt.ylabel('Winners')
        plt.xlabel('Total Numbers Called')
        plt.show()
