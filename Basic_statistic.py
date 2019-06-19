import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



dataset = pd.read_csv('D:\\study\\fourth academic year\\firstTerm\\KBS\\project\\datamining\\Data.csv')

beer_servings = dataset.iloc[:,1].values
spirit_servings = dataset.iloc[:,2].values
wine_servings = dataset.iloc[:,3].values
total_litres_of_pure_alcohol = dataset.iloc[:,4].values

def mean(data):
    sumData = 0
    for element in data:
        sumData += element

    return sumData / len(data)


def medium(data):
    mediumData = 0
    if len(data) % 2 == 0:  # Even
        mediumData = int(len(data) / 2)
        mediumData = (data[mediumData-1] + data[mediumData]) / 2
    else:
        mediumData = int(len(data) / 2)
        mediumData = data[mediumData]

    return mediumData


def mode(data):
    modeData = []
    dataCount = []
    maxCount = 0
    for i in range(len(data)):
        count = 0
        for j in range(len(data)):
            if data[j] == data[i]:
                count += 1
        if isFound(dataCount, data[i]):
            dataCount.append([data[i], count])
            if count > maxCount:
                maxCount = count

    for i in range(len(dataCount)):
        if maxCount == dataCount[i][1]:
            modeData.append(dataCount[i][0])

    return modeData[0]


def isFound(dataCount, element):
    for i in range(len(dataCount)):
        if element == dataCount[i][0]:
            return False
    return True


def range_(data):
    Max = max(data)
    Min = min(data)

    return Max - Min


def variance(data):
    mean_ = mean(data)
    count = 0
    sum = 0
    for i in data:
        count += 1
        sum += np.math.pow(i - mean_, 2)
    variance_ = (1/(count-1)) * sum

    return variance_


def standard_deviation(data):

    return np.math.sqrt(variance(data))


def quartile_IQR(data):
    medium_50 = medium(data)
    l = []
    for i in range(0, (int(len(data) / 2))):
        l.append(data[i])
    medium_25 = medium(l)
    r = []
    for j in range((int(len(data) / 2))+1, len(data)):
        r.append(data[j])
    medium_75 = medium(r)
    IQR = medium_75 - medium_25

    return IQR


columns = ['beer', 'spirit', 'wine',  'litres']
titles = ["Mean", "Meadian", "Mode", "Range", "IQR", "Variance", "Standard deviation" ]
operationData = [[mean(beer_servings), mean(spirit_servings), mean(wine_servings), mean(total_litres_of_pure_alcohol)],
                 [medium(beer_servings), medium(spirit_servings), medium(wine_servings), medium(total_litres_of_pure_alcohol)],
                 [mode(beer_servings), mode(spirit_servings), mode(wine_servings), mode(total_litres_of_pure_alcohol)],
                 [range_(beer_servings), range_(spirit_servings), range_(wine_servings), range_(total_litres_of_pure_alcohol)],
                 [quartile_IQR(beer_servings), quartile_IQR(spirit_servings), quartile_IQR(wine_servings), quartile_IQR(total_litres_of_pure_alcohol)],
                 [variance(beer_servings), variance(spirit_servings), variance(wine_servings), variance(total_litres_of_pure_alcohol)],
                 [standard_deviation(beer_servings), standard_deviation(spirit_servings), standard_deviation(wine_servings), standard_deviation(total_litres_of_pure_alcohol)]]

print('Mean for beer_servings = ' + str(mean(beer_servings)))
print('Medium for beer_servings = ' + str(medium(beer_servings)))
print('Mode for beer_servings = ' + str(mode(beer_servings)))
print('Range for beer_servings = ' + str(range_(beer_servings)))
print('Variance for beer_servings = ' + str(variance(beer_servings)))
print('Standard_Deviation for beer_servings = ' + str(standard_deviation(beer_servings)))
print('Quartile IQR = ' + str(quartile_IQR(beer_servings)))
#print(dataset.iloc[:,1].describe())
print('-----------------------------------------------------------')
print('Mean for spirit_servings = ' + str(mean(spirit_servings)))
print('Medium for spirit_servings = ' + str(medium(spirit_servings)))
print('Mode for spirit_servings = ' + str(mode(spirit_servings)))
print('Range for spirit_servings = ' + str(range_(spirit_servings)))
print('Variance for spirit_servings = ' + str(variance(spirit_servings)))
print('Standard_Deviation for spirit_servings = ' + str(standard_deviation(spirit_servings)))
print('Quartile IQR = ' + str(quartile_IQR(spirit_servings)))
#print(dataset.iloc[:,2].describe())
print('-----------------------------------------------------------')
print('Mean for wine_servings = ' + str(mean(wine_servings)))
print('Medium for wine_servings = ' + str(medium(wine_servings)))
print('Mode for wine_servings = ' + str(mode(wine_servings)))
print('Range for wine_servings = ' + str(range_(wine_servings)))
print('Variance for wine_servings = ' + str(variance(wine_servings)))
print('Standard_Deviation for wine_servings = ' + str(standard_deviation(wine_servings)))
print('Quartile IQR = ' + str(quartile_IQR(wine_servings)))
#print(dataset.iloc[:,3].describe())
print('-----------------------------------------------------------')
print('Mean for total_litres_of_pure_alcohol = ' + str(mean(total_litres_of_pure_alcohol)))
print('Medium for total_litres_of_pure_alcohol = ' + str(medium(total_litres_of_pure_alcohol)))
print('Mode for total_litres_of_pure_alcohol = ' + str(mode(total_litres_of_pure_alcohol)))
print('Range for total_litres_of_pure_alcohol = ' + str(range_(total_litres_of_pure_alcohol)))
print('Variance for total_litres_of_pure_alcohol = ' + str(variance(total_litres_of_pure_alcohol)))
print('Standard_Deviation for total_litres_of_pure_alcohol = ' + str(standard_deviation(total_litres_of_pure_alcohol)))
print('Quartile IQR = ' + str(quartile_IQR(total_litres_of_pure_alcohol)))
#print(dataset.iloc[:,4].describe())
print('-----------------------------------------------------------')



for i in range(7):
    plt.subplot(2, 4, i+1)
    plt.bar(columns, operationData[i])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(titles[i])

plt.show()