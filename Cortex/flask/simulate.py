import requests as rq
import json
import math
import time
import datetime
import plotly.express as px
import os
import random

def getYesterdayInEtherium():
    data = []
    yesterday = int(time.mktime(datetime.datetime.strptime((datetime.date.today() - datetime.timedelta(days=1)).__str__()  , "%Y-%m-%d").timetuple()))
    today = int(time.mktime(datetime.datetime.strptime((datetime.date.today()).__str__()  , "%Y-%m-%d").timetuple()))
    newData = rq.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start={}&end={}&period={}".format(yesterday, today, 300)).json()
    newData = [point for point in newData if type(point) == dict]
    data.extend(newData)
    timeData = [int(point['date']) for point in data]
    weightedAverageData = [float(point['weightedAverage']) for point in data]

    timeData = []
    for i in range(288):
        timeData.append(i)
    file2 = open("actual3.txt", 'r')
    actual = [float(num) for num in file2.read().replace(' ', '').split(',')]   
    return {'time': timeData, 'price': actual}

def plotData(data):
    fig = px.line(data, x='time', y="price")
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()

def getFakeData(data):
    fakePrice = []
    fakeConfidence = []
    for price in data['price']:
        multiplier = random.uniform(0.995, 1.005)
        confidence = random.uniform(0.3, 0.99)
        fakePrice.append(multiplier * price)
        fakeConfidence.append(confidence)
    fakePrediction = {'time': data['time'], 'price': fakePrice, 'confidence': fakeConfidence}
    #fakePrediction = {'time': data['time'], 'price': data['price'], 'confidence': fakeConfidence}

    file = open("forcast3.txt", 'r')
    forcast = [float(num) for num in file.read().replace('\n', ' ').split()]
    timeData = []
    for i in range(288):
        timeData.append(i)
    fakePrediction = {'time': timeData, 'price': forcast, 'confidence': fakeConfidence}
    return fakePrediction

def generatePricePrediction(prediction, real, seed = 1000):
    current_prog = [seed]
    invested_prog = [0]
    net_prog = [seed]
    current = seed
    invested = 0
    previous = real['price'][0]
    for i in range(len(prediction['price']) - 1):
        previous = real['price'][i]
        if prediction['price'][i + 1] > previous:
            invested += current * prediction['confidence'][i + 1]
            current -= current * prediction['confidence'][i + 1]
        elif prediction['price'][i + 1] < previous:
            current += invested * prediction['confidence'][i + 1]
            invested -= invested * prediction['confidence'][i + 1]
        change = real['price'][i + 1] / previous
        invested *= change
        current_prog.append(current)
        invested_prog.append(invested)
        net_prog.append(current + invested)
    return {'pocket': current_prog, 'invested': invested_prog, 'net': net_prog}