import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd



app = Flask(__name__)

# Load your model (ensure the path is correct)
model = joblib.load('model.pkl')

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data from the request
        limit_bal = float(request.form['LIMIT_BAL'])
        sex = int(request.form['SEX'])
        education = int(request.form['EDUCATION'])
        marriage = int(request.form['MARRIAGE'])
        age = int(request.form['AGE'])
        pay_0 = int(request.form['PAY_0'])
        pay_2 = int(request.form['PAY_2'])
        pay_3 = int(request.form['PAY_3'])
        pay_4 = int(request.form['PAY_4'])
        pay_5 = int(request.form['PAY_5'])
        pay_6 = int(request.form['PAY_6'])
        bill_amt1 = float(request.form['BILL_AMT1'])
        bill_amt2 = float(request.form['BILL_AMT2'])
        bill_amt3 = float(request.form['BILL_AMT3'])
        bill_amt4 = float(request.form['BILL_AMT4'])
        bill_amt5 = float(request.form['BILL_AMT5'])
        bill_amt6 = float(request.form['BILL_AMT6'])
        pay_amt1 = float(request.form['PAY_AMT1'])
        pay_amt2 = float(request.form['PAY_AMT2'])
        pay_amt3 = float(request.form['PAY_AMT3'])
        pay_amt4 = float(request.form['PAY_AMT4'])
        pay_amt5 = float(request.form['PAY_AMT5'])
        pay_amt6 = float(request.form['PAY_AMT6'])

        # Prepare input data as DataFrame
        feature_names = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4',
                         'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5',
                         'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

        input_data = pd.DataFrame([{
            'LIMIT_BAL': limit_bal,
            'SEX': sex,
            'EDUCATION': education,
            'MARRIAGE': marriage,
            'AGE': age,
            'PAY_0': pay_0,
            'PAY_2': pay_2,
            'PAY_3': pay_3,
            'PAY_4': pay_4,
            'PAY_5': pay_5,
            'PAY_6': pay_6,
            'BILL_AMT1': bill_amt1,
            'BILL_AMT2': bill_amt2,
            'BILL_AMT3': bill_amt3,
            'BILL_AMT4': bill_amt4,
            'BILL_AMT5': bill_amt5,
            'BILL_AMT6': bill_amt6,
            'PAY_AMT1': pay_amt1,
            'PAY_AMT2': pay_amt2,
            'PAY_AMT3': pay_amt3,
            'PAY_AMT4': pay_amt4,
            'PAY_AMT5': pay_amt5,
            'PAY_AMT6': pay_amt6
        }], columns=feature_names)


        # Make prediction
        prediction = model.predict(input_data)

        # Prepare response
        result = int(prediction[0])  # Convert to native Python int
        message = 'Will Not Default' if result == 0 else 'Will Default'

        # Return result as JSON with message
        return jsonify({'result': result, 'message': message}), 200  # Return result as JSON
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error message as JSON if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)
