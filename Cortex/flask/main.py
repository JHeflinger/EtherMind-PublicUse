from flask import Flask, jsonify
from simulate import *
import time

app = Flask(__name__)

@app.route('/fakesimulation')
def simulateFakeData():
    time.sleep(2)
    data = getYesterdayInEtherium()
    prediction = getFakeData(data)
    earnings = generatePricePrediction(prediction, data)
    result = {'pocket' : earnings['pocket'], 'invested' : earnings['invested'], 'net' : earnings['net'], 'time' : data['time'], 'real' : data['price'], 'fake' : prediction['price'], 'confidence' : prediction['confidence']}
    return jsonify(result)

if __name__ == '__main__':
    app.run()