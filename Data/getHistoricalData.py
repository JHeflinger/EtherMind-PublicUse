import requests as rq
import json
import math
import time




def getData(startEpoch: int, endEpoch: int, period: int, pointsPerRequest: int = 500):
    data = []
    if ((endEpoch - startEpoch)/period) > period*pointsPerRequest:
        for i in range(0, endEpoch-startEpoch, period*pointsPerRequest):
            startPeriod = startEpoch + i
            endPeriod = startEpoch + (i + period*pointsPerRequest)
            newData = rq.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start={}&end={}&period={}".format(startPeriod, endPeriod, period)).json()
            # time.sleep(0.1)
            newData = [point for point in newData if type(point) == dict]
            data.extend(newData)
            print(f"Getting {len(newData)} data points from {startPeriod} to {endPeriod}")
    return data


datJson = getData(1546300800, 1682208000, 300)

# print(datJson)

print(datJson[0])

print(len(datJson))

json_object = json.dumps(datJson, indent=4)

with open("ethData.json", "w") as outfile:
    outfile.write(json_object)