import joblib

model = joblib.load("model.pkl")
vector = joblib.load("vector.pkl")

while True:
    message = input("Enter message: ")

    message_vec = vector.transform([message])
    prediction = model.predict(message_vec)

    if prediction[0] == 1:
        print("⚠ Scam Message Detected")
    else:
        print("✅ Safe Message")
