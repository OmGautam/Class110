import plotly.figure_factory as ff 
import statistics
import random
import pandas as pd 
import csv
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def randomSetMean():
    dataSet = []
    for i in range(0,100):
        rand = random.randint(0,len(data))
        value = data[rand]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setUp():
    meanList = []
    for i in range(1,1001):
        setOfMeans = randomSetMean()
        meanList.append(setOfMeans)
    showFig(meanList)

setUp()

# def sd():
#     meanList = []
#     for i in range(0,1000):
#         setOfMeans = randomSetMean(100)
#         meanList.append(setOfMeans)
#     standard = statistics.stdev(meanList)
#     print("Standard Deviation is", standard)

# sd()




