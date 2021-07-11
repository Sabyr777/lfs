import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd 
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    horizon = [int(x) for x in request.form.values()]
    future = model.make_future_dataframe(periods = horizon[0])
	
    prediction = model.predict(future)

    output = prediction['yhat'][horizon[0]]
	
    return render_template('index.html', prediction_text='Energy should be MW {}'.format(output))

#@app.route('/results',methods=['POST'])
#def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)