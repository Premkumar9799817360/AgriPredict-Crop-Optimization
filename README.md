# 🌾 AgriPredict - AI-Powered Precision Farming Solution

## 📋 Overview
AgriPredict is a Flask-based web application that predicts the most suitable crops based on soil nutrients (N-P-K ratios), climatic conditions, and pH levels using Machine Learning with **97% accuracy**.

---


## 🌐 Live Demo

You can test the project live using the link below:

👉 **[Live Testing URL](https://agripredict-9lbe.onrender.com/)**  

Or click the button below 👇  

<p align="center">
  <a href="https://agripredict-9lbe.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/🔗%20Open%20Live%20App-00C853?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live App Button"/>
  </a>
</p>

---



## 🚀 Quick Start Guide

### Step 1: Project Structure
Ensure your project has the following structure:
```
AgriPredict/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── argriculture_production.pkl     # Your trained model (already have)
├── templates/
│   └── index.html                  # UI template
└── README.md                       # This file
```

### Step 2: Installation

1. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Step 3: Verify Model File
Make sure your `argriculture_production.pkl` file is in the root directory of the project.

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 📊 Features

✨ **AI-Powered Predictions** - Logistic Regression model with 97% accuracy
🎨 **Beautiful Animated UI** - Modern gradient design with particle effects
📋 **Sample Data Table** - Reference data with copy-to-clipboard functionality
🌡️ **Climate Analysis** - Temperature, humidity, and rainfall assessment
🧪 **Soil Insights** - NPK ratios and pH level analysis
📱 **Responsive Design** - Works on all devices

---

## 🌾 Supported Crops

The model can predict the following crops:
- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Black Gram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

---

## 🔧 Input Parameters

| Parameter | Description | Unit | Example |
|-----------|-------------|------|---------|
| **N** | Nitrogen ratio in soil | Ratio | 90 |
| **P** | Phosphorus ratio in soil | Ratio | 42 |
| **K** | Potassium ratio in soil | Ratio | 43 |
| **Temperature** | Ambient temperature | °C | 20.88 |
| **Humidity** | Relative humidity | % | 82.00 |
| **pH** | Soil pH value | pH | 6.50 |
| **Rainfall** | Annual rainfall | mm | 202.94 |

---

## 🎯 Model Performance

```
Model: Logistic Regression
Accuracy: 97%

Classification Report:
              precision    recall  f1-score   support
   accuracy                           0.97       440
  macro avg       0.97      0.97      0.97       440
weighted avg       0.97      0.97      0.97       440
```

---

## 💻 Usage Example

1. **Open the application** in your browser
2. **Fill in the form** with soil and climate parameters:
   - Nitrogen (N): 90
   - Phosphorus (P): 42
   - Potassium (K): 43
   - Temperature: 20.88°C
   - Humidity: 82.00%
   - pH: 6.50
   - Rainfall: 202.94mm
3. **Click "Predict Optimal Crop"**
4. **View the recommendation** - e.g., "Recommended Crop: RICE"


## 📦 Dependencies

```
Flask==3.0.0          # Web framework
numpy==1.24.3         # Numerical computing
joblib==1.3.2         # Model loading
scikit-learn==1.3.2   # ML library
pandas==2.0.3         # Data manipulation
Werkzeug==3.0.1       # WSGI utilities
```



**Happy Farming! 🌾🚜**

