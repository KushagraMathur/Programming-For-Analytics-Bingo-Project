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
        Median = {}
        Skew = {}
        Kurtosis = {}
        I_Quartile = {}
        II_Quartile = {}
        III_Quartile = {}
        StandardDeviation = {}
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
            Median[key] = statistics.median(value)
            StandardDeviation = statistics.stdev(value)
            Skew[key] = scipy.stats.skew(value)
            Kurtosis[key] = scipy.stats.kurtosis(value)
            I_Quartile[key] = np.percentile(value, 25)
            II_Quartile[key] = np.percentile(value, 50)
            III_Quartile[key] = np.percentile(value, 75)
        my_dict = {"Median": Median, "Standard Deviation": StandardDeviation, "Skew": Skew,
                   "Kurtosis": Kurtosis, "25th Percentile": I_Quartile, "50th Percentile": II_Quartile, "75th Percentile": III_Quartile}
        data = pd.DataFrame(my_dict)
        data['Skew'] = data['Skew'].replace(np.nan, "nan")
        data['Kurtosis'] = data['Kurtosis'].replace(np.nan, "nan")
        file_name = 'Centrality_Data.xlsx'
        data.to_excel(file_name)
        print("\n\n", data.to_markdown())
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
