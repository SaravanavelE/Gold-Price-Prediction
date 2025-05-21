from flask import Flask, request, render_template
import pandas as pd
import pickle
from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('gold_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    date_str = request.form['date']
    date_obj = pd.to_datetime(date_str)

    new_data = pd.DataFrame({
        'Year': [date_obj.year],
        'Month': [date_obj.month],
        'Day': [date_obj.day]
    })

    prediction = model.predict(new_data)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', prediction=prediction, date=date_str)

if __name__ == '__main__':
    app.run(debug=True)
