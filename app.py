import numpy as np
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("argriculture_production.pkl")

# Sample data for display
SAMPLE_DATA = [
    {"N": 90, "P": 42, "K": 43, "temperature": 20.88, "humidity": 82.00, "ph": 6.50, "rainfall": 202.94, "label": "rice"},
    {"N": 85, "P": 58, "K": 41, "temperature": 21.77, "humidity": 80.32, "ph": 7.04, "rainfall": 226.66, "label": "rice"},
    {"N": 99, "P": 39, "K": 18, "temperature": 19.20, "humidity": 68.31, "ph": 6.11, "rainfall": 87.85, "label": "maize"},
    {"N": 62, "P": 48, "K": 20, "temperature": 21.70, "humidity": 60.47, "ph": 6.71, "rainfall": 95.71, "label": "maize"},
    {"N": 51, "P": 72, "K": 75, "temperature": 18.89, "humidity": 14.99, "ph": 7.10, "rainfall": 80.11, "label": "chickpea"},
    {"N": 22, "P": 64, "K": 82, "temperature": 19.49, "humidity": 17.17, "ph": 6.47, "rainfall": 87.51, "label": "chickpea"},
    {"N": 9, "P": 77, "K": 17, "temperature": 20.12, "humidity": 24.45, "ph": 5.78, "rainfall": 106.16, "label": "kidneybeans"},
    {"N": 28, "P": 59, "K": 22, "temperature": 30.91, "humidity": 52.80, "ph": 7.05, "rainfall": 170.99, "label": "pigeonpeas"},
    {"N": 59, "P": 55, "K": 19, "temperature": 31.74, "humidity": 62.51, "ph": 7.33, "rainfall": 68.97, "label": "blackgram"},
    {"N": 14, "P": 67, "K": 25, "temperature": 25.29, "humidity": 60.86, "ph": 7.24, "rainfall": 49.37, "label": "lentil"},
    {"N": 33, "P": 23, "K": 45, "temperature": 20.00, "humidity": 85.84, "ph": 7.12, "rainfall": 112.34, "label": "pomegranate"},
    {"N": 85, "P": 95, "K": 47, "temperature": 25.94, "humidity": 78.34, "ph": 6.21, "rainfall": 119.85, "label": "banana"},
    {"N": 28, "P": 37, "K": 28, "temperature": 32.13, "humidity": 50.53, "ph": 6.10, "rainfall": 98.63, "label": "mango"},
    {"N": 20, "P": 122, "K": 204, "temperature": 11.80, "humidity": 80.86, "ph": 6.49, "rainfall": 65.07, "label": "grapes"},
    {"N": 97, "P": 25, "K": 50, "temperature": 26.22, "humidity": 80.90, "ph": 6.09, "rainfall": 49.09, "label": "watermelon"},
    {"N": 110, "P": 25, "K": 54, "temperature": 28.91, "humidity": 90.78, "ph": 6.43, "rainfall": 23.44, "label": "muskmelon"},
    {"N": 13, "P": 144, "K": 197, "temperature": 22.92, "humidity": 94.90, "ph": 6.28, "rainfall": 105.69, "label": "apple"},
    {"N": 13, "P": 16, "K": 8, "temperature": 34.74, "humidity": 93.12, "ph": 6.95, "rainfall": 100.20, "label": "orange"},
    {"N": 45, "P": 58, "K": 49, "temperature": 30.11, "humidity": 90.35, "ph": 6.83, "rainfall": 75.25, "label": "papaya"},
    {"N": 8, "P": 26, "K": 26, "temperature": 25.55, "humidity": 91.64, "ph": 5.70, "rainfall": 212.87, "label": "coconut"},
    {"N": 132, "P": 52, "K": 19, "temperature": 24.16, "humidity": 76.74, "ph": 6.44, "rainfall": 61.95, "label": "cotton"},
    {"N": 75, "P": 36, "K": 44, "temperature": 23.28, "humidity": 74.28, "ph": 6.61, "rainfall": 153.74, "label": "jute"},
    {"N": 104, "P": 18, "K": 30, "temperature": 23.60, "humidity": 60.40, "ph": 6.78, "rainfall": 140.94, "label": "coffee"}
]

@app.route('/')
def index():
    return render_template('index.html', sample_data=SAMPLE_DATA)

@app.route('/predict', methods=["POST"])
def predict():
    try:
        data1 = float(request.form['nitrogen'])
        data2 = float(request.form['phosphorus'])
        data3 = float(request.form['potassium'])
        data4 = float(request.form['temperature'])
        data5 = float(request.form['humidity'])
        data6 = float(request.form['ph'])
        data7 = float(request.form['rainfall'])
        
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7]], dtype=float)
        pred = model.predict(arr)
        prediction = str(pred[0])
        
        return render_template('index.html', 
                             sample_data=SAMPLE_DATA,
                             prediction_text=f"Recommended Crop: {prediction.upper()}",
                             show_result=True,
                             input_data={
                                 'nitrogen': data1,
                                 'phosphorus': data2,
                                 'potassium': data3,
                                 'temperature': data4,
                                 'humidity': data5,
                                 'ph': data6,
                                 'rainfall': data7
                             })
    except Exception as e:
        return render_template('index.html', 
                             sample_data=SAMPLE_DATA,
                             error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)