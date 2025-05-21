# 🟡 Gold Price Prediction Web App

This is a simple Flask-based web application that predicts gold prices based on date inputs (Year, Month, Day). The model is trained using `scikit-learn` and can be deployed on platforms like Render.

---

## 🚀 Features

- ✅ Predict gold price for a given date.
- 🧠 Trained with `scikit-learn` (Linear Regression or other models).
- 🖥️ Clean Web UI built using HTML and CSS.
- 🌐 Easily deployable on platforms like Render.

---

## 📁 Project Structure

```

Gold-Price-Prediction/
├── app.py                 # Main Flask app
├── gold\_price\_model.pkl   # Trained machine learning model (Pickle)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Homepage input form
│   └── result.html        # Result display page
├── static/
│   └── style.css          # CSS styles
├── Procfile               # For Render deployment
└── README.md              # Project documentation

````

---

## 💻 Local Setup

### 🔹 1. Clone the repo

git clone https://github.com/yourusername/Gold-Price-Prediction.git
cd Gold-Price-Prediction

### 🔹 2. Install requirements

pip install -r requirements.txt


### 🔹 3. Run the Flask app locally

python app.py

Then go to `http://127.0.0.1:5000` in your browser.

---

## 🌐 Deployment on Render

1. Push your project to a GitHub repository.
2. Go to [https://render.com](https://render.com).
3. Click **New Web Service**.
4. Connect your GitHub repository.
5. Fill in the following details:

* **Build Command**:

  pip install -r requirements.txt

* **Start Command**:

  gunicorn app:app

6. Hit deploy and wait for the web app to be live.

---

## 📌 Sample Prediction Code (Optional)

import pickle
import pandas as pd

model = pickle.load(open('gold_price_model.pkl', 'rb'))
new_date = pd.to_datetime('2024-06-01')
new_data = pd.DataFrame({'Year': [new_date.year], 'Month': [new_date.month], 'Day': [new_date.day]})
predicted_price = model.predict(new_data)
print(f"Predicted price for {new_date}: {predicted_price[0]}")

---

## 🔗 Live Demo

**🌍 Deployed on Render:**
[https://gold-price-predictor.onrender.com](https://gold-price-predictor.onrender.com)

---

## 🏷️ License

This project is licensed under the MIT License. Feel free to use, modify, and share.

---

## 🙌 Author

Developed by **\Saravanavel E**
GitHub: [https://github.com/SaravanavelE](https://github.com/SaravanavelE)
LinkedIn: [https://linkedin.com/in/saravanavel-e](https://linkedin.com/in/saravanavel-e)

---
