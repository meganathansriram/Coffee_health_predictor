☕ Coffee Health Predictor
🔍 Overview

Coffee Health Predictor is a machine learning–based web application built using Django and XGBoost.
It predicts possible health issues of a person based on their coffee consumption habits and lifestyle factors such as age, gender, stress level, and sleep quality.

This project demonstrates a complete end-to-end AI pipeline — from data preprocessing and model training to web integration and deployment.

🧩 Features

✅ Predicts potential health issues from user input
✅ Trained using XGBoost Classifier for high accuracy
✅ Interactive HTML frontend with Django backend
✅ Real-time predictions with instant feedback
✅ Encodes categorical data automatically
✅ Saves and loads trained model using Joblib

⚙️ Tech Stack
Layer	Technologies Used
Frontend	HTML5, CSS3
Backend	Python, Django Framework
Machine Learning	XGBoost, Pandas, NumPy, Scikit-learn
Model Deployment	Joblib
Database	SQLite (default Django database)
📁 Project Structure
coffee_health_predictor/
│
├── coffee_health_predictor/         # Main Django project folder
│   ├── __init__.py
│   ├── settings.py                  # Global settings
│   ├── urls.py                      # URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── predictor/                       # Core app
│   ├── templates/
│   │   ├── index.html               # Input form
│   │   └── result.html              # Prediction output
│   ├── __init__.py
│   ├── views.py                     # Logic for prediction
│   ├── urls.py                      # App URL routes
│   ├── models.py
│   ├── admin.py
│   └── apps.py
│
├── static/                          # (Optional) CSS, images, JS
├── db.sqlite3                       # Default Django DB
├── manage.py
├── xgboost_health_model.pkl         # Trained model
└── requirements.txt                 # Dependencies

🧠 How It Works
1️⃣ Dataset Preparation

Synthetic dataset of 10,000 records with coffee and health attributes.

Columns include: Age, Gender, Coffee_Consumption, Sleep_Quality, Stress_Level, etc.

2️⃣ Data Preprocessing

Used LabelEncoder and OneHotEncoder to encode categorical variables.

Split dataset using train_test_split() for training and testing.

3️⃣ Model Training

Trained an XGBoostClassifier with tuned hyperparameters for better accuracy.

Evaluated model using accuracy_score and classification_report.

4️⃣ Model Saving

Exported trained model using joblib.dump() for later use.

5️⃣ Web Integration (Django)

User enters data through index.html.

views.py loads the model and predicts the health outcome.

Result displayed dynamically in result.html.

🖥️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/coffee-health-predictor.git
cd coffee-health-predictor

2️⃣ Create a virtual environment
python -m venv env
source env/bin/activate   # For Linux/Mac
env\Scripts\activate      # For Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Django server
python manage.py runserver

5️⃣ Open in browser

👉 http://127.0.0.1:8000/

📦 requirements.txt Example
Django==5.0.4
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
xgboost==2.0.3
joblib==1.4.2

📊 Sample Output

Input:
Age = 25, Gender = Male, Sleep_Quality = Poor, Stress_Level = High

Output:
Predicted Health Issue → “Risk of Heart Problem”

🚀 Future Enhancements

Add user authentication and profile history

Visualize health trends and analysis

Deploy on Render, AWS, or Heroku

Integrate Deep Learning models for improved accuracy

👨‍💻 Author

R. Meganathan
B.Tech – Artificial Intelligence and Data Science
Karpagam College of Engineering

📧 sriram21214g@gmail.com

🌐 LinkedIn
 | GitHub
