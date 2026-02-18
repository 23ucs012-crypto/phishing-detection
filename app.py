from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model files
model = joblib.load("model.pkl")
vector = joblib.load("vector.pkl")

# Home route
@app.route("/")
def home():
    return "Phishing Detection API is Running Successfully 🚀"

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data["message"]

    message_vec = vector.transform([message])
    prediction = model.predict(message_vec)

    result = "Scam" if prediction[0] == 1 else "Safe"

    return jsonify({"prediction": result})

# Run app
if __name__ == "__main__":
    app.run(debug=True)


