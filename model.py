import joblib
import pandas as pd

class FloodPredictionModel:
    def __init__(self, model_path="flood_model.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, rainfall, cloud_visibility):
        data = pd.DataFrame({
            "Rainfall": [rainfall],
            "CloudVisibility": [cloud_visibility]
        })

        prediction = self.model.predict(data)

        if prediction[0] == 1:
            return "Flood Likely"
        else:
            return "No Flood"

# Example Usage
if __name__ == "__main__":
    predictor = FloodPredictionModel()
    result = predictor.predict(120, 60)
    print("Prediction:", result)
