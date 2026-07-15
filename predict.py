import joblib
import pandas as pd

# Load trained model
model = joblib.load("flood_model.pkl")

def predict_flood(rainfall, cloud_visibility):
    data = pd.DataFrame({
        "Rainfall": [rainfall],
        "CloudVisibility": [cloud_visibility]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Flood Likely"
    else:
        return "No Flood"

# Example
result = predict_flood(120, 60)
print("Prediction:", result)
