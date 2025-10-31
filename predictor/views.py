from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load saved model and encoders
model = joblib.load(os.path.join(BASE_DIR, 'models/xgboost_health_model.pkl'))
health_encoder = joblib.load(os.path.join(BASE_DIR, 'models/label_encoder.pkl'))
stress_encoder = joblib.load(os.path.join(BASE_DIR, 'models/stress_encoder.pkl'))
sleep_encoder = joblib.load(os.path.join(BASE_DIR, 'models/sleep_encoder.pkl'))
onehot_encoder = joblib.load(os.path.join(BASE_DIR, 'models/onehot_encoder.pkl'))

# Get encoded column names used during training
# (You can save this from training script using joblib.dump(X.columns, "feature_columns.pkl"))
try:
    feature_columns = joblib.load(os.path.join(BASE_DIR, 'models/feature_columns.pkl'))
except:
    feature_columns = None  # optional fallback

encode_cols = ["Gender", "Country", "Occupation"]

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        try:
            # Collect form inputs
            data = {
                "Age": float(request.POST.get('Age', 0)),
                "Gender": request.POST.get('Gender', 'Male'),
                "Country": request.POST.get('Country', 'USA'),
                "Coffee_Intake": float(request.POST.get('Coffee_Intake', 0)),
                "Caffeine_mg": float(request.POST.get('Caffeine_mg', 0)),
                "Sleep_Hours": float(request.POST.get('Sleep_Hours', 0)),
                "Sleep_Quality": request.POST.get('Sleep_Quality', 'Good'),
                "BMI": float(request.POST.get('BMI', 0)),
                "Heart_Rate": float(request.POST.get('Heart_Rate', 0)),
                "Stress_Level": request.POST.get('Stress_Level', 'Medium'),
                "Physical_Activity_Hours": float(request.POST.get('Physical_Activity_Hours', 0)),
                "Occupation": request.POST.get('Occupation', 'Other'),
                "Smoking": int(request.POST.get('Smoking', 0)),
                "Alcohol_Consumption": int(request.POST.get('Alcohol_Consumption', 0)),
            }

            df = pd.DataFrame([data])

            # Encode categorical features (same as training)
            df['Stress_Level'] = stress_encoder.transform(df['Stress_Level'])
            df['Sleep_Quality'] = sleep_encoder.transform(df['Sleep_Quality'])

            # One-hot encode
            encoded = onehot_encoder.transform(df[encode_cols])
            encoded_df = pd.DataFrame(encoded, columns=onehot_encoder.get_feature_names_out(encode_cols))

            # Combine
            df_final = pd.concat([df.drop(columns=encode_cols), encoded_df], axis=1)

            # Align with training columns if available
            if feature_columns is not None:
                df_final = df_final.reindex(columns=feature_columns, fill_value=0)

            # Predict
            pred_encoded = model.predict(df_final)
            result = health_encoder.inverse_transform(pred_encoded)[0]

            return render(request, 'result.html', {'prediction': result})

        except Exception as e:
            return render(request, 'result.html', {'error': str(e)})

    return JsonResponse({'error': 'POST request only'})
