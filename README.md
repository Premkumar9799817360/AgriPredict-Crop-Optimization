# 🌾 AgriPredict - AI-Powered Precision Farming Solution

## 📋 Overview
AgriPredict is a Flask-based web application that predicts the most suitable crops based on soil nutrients (N-P-K ratios), climatic conditions, and pH levels using Machine Learning with **97% accuracy**.

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

---

## 🎨 UI Features

### Animated Background
- 50 floating particles with smooth animations
- Dynamic gradient background
- Responsive to screen size

### Interactive Elements
- Smooth form transitions
- Hover effects on cards and buttons
- Loading animation on form submission
- Success/error message animations

### Sample Data Table
- Displays 23 reference data points
- Copy-to-clipboard functionality
- Hover effects on table rows
- Responsive table design

---

## 🛠️ Troubleshooting

### Issue: Module not found error
**Solution**: Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Model file not found
**Solution**: Ensure `argriculture_production.pkl` is in the same directory as `app.py`

### Issue: Port already in use
**Solution**: Change the port in `app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change to any available port
```

### Issue: Templates not found
**Solution**: Create a `templates` folder and place `index.html` inside it

---

## 📦 Dependencies

```
Flask==3.0.0          # Web framework
numpy==1.24.3         # Numerical computing
joblib==1.3.2         # Model loading
scikit-learn==1.3.2   # ML library
pandas==2.0.3         # Data manipulation
Werkzeug==3.0.1       # WSGI utilities
```

---

## 🔄 Updates & Modifications

### To Change Model
Replace `argriculture_production.pkl` with your new model file and update the filename in `app.py`:
```python
model = joblib.load("your_new_model.pkl")
```

### To Add More Sample Data
Edit the `SAMPLE_DATA` list in `app.py`:
```python
SAMPLE_DATA = [
    {"N": 90, "P": 42, "K": 43, ...},
    # Add more entries here
]
```

### To Customize UI Colors
Modify the gradient colors in `index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

---

## 📝 API Endpoints

### GET `/`
Returns the main application page with the prediction form

### POST `/predict`
Accepts form data and returns crop prediction

**Form Parameters**:
- nitrogen (float)
- phosphorus (float)
- potassium (float)
- temperature (float)
- humidity (float)
- ph (float)
- rainfall (float)

**Response**: Rendered HTML with prediction result

---

## 🎓 Educational Purpose

This application demonstrates:
- Flask web framework implementation
- Machine Learning model deployment
- Modern responsive UI design
- Form handling and validation
- Dynamic content rendering with Jinja2 templates

---

## 📄 License

This project is created for educational and agricultural optimization purposes.

---

## 👨‍💻 Developer Notes

- The application runs in debug mode by default
- All predictions are processed server-side
- Model predictions are cached in memory during runtime
- Input validation is handled both client-side and server-side

---

## 🌟 Future Enhancements

- [ ] Add data visualization charts
- [ ] Export predictions to PDF
- [ ] Multi-language support
- [ ] Historical prediction tracking
- [ ] Mobile app version
- [ ] API for third-party integration

---

## 📞 Support

If you encounter any issues:
1. Check this README file
2. Verify all dependencies are installed
3. Ensure Python version is 3.8 or higher
4. Check that the model file exists

---

**Happy Farming! 🌾🚜**