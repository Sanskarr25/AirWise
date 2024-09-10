import numpy as np
from flask import Flask, request, jsonify, render_template, redirect
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
  
@app.route('/predict_input')
def predict_input():
    return render_template('predict_input.html')

@app.route('/sanskar_github')
def github():
    return redirect('https://github.com/Sanskarr25/AirWise')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    return render_template('predict_output.html', prediction_text='Predicted Air Quality Index : {}'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
  
  
if __name__ == "__main__":
    app.run(debug=True)