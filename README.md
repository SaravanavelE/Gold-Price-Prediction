# 🟡 Gold Price Prediction Web App

This is a simple Flask-based web application that predicts gold prices based on date inputs (Year, Month, Day). The model is trained using `scikit-learn` and can be deployed on platforms like Render.

---

## 🚀 Features

- Predict gold price for a given date.
- Trained with `scikit-learn`.
- Web UI with HTML + CSS.
- Ready for deployment (Render, etc.).

---

## 📁 Project Structure

Gold-Price-Prediction/
├── app.py # Main Flask app
├── gold_price_model.pkl # Trained machine learning model
├── requirements.txt # Python dependencies
├── templates/
│ ├── index.html # Homepage input form
│ └── result.html # Result display page
├── static/
│ └── style.css # Optional CSS styles
├── Procfile # For Render deployment
└── README.md

---

## 💻 Local Setup

### 🔹 1. Clone the repo

git clone https://github.com/yourusername/Gold-Price-Prediction.git
cd Gold-Price-Prediction

### 🔹 2. Install requirements

pip install -r requirements.txt
### 🔹 3. Run the Flask app
python app.py

### 🔹 4.🌐 Deployment (Render)
  Push your code to GitHub.
  Go to Render.
  Create a new Web Service.
  Connect your GitHub repo.
  Use the following build and start command:
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
---
### 🏷️ License

Let me know if you want this customized with your real GitHub URL or LinkedIn.
