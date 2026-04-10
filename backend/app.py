# from flask import Flask, request, jsonify
# import pickle
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# # Load model
# model = pickle.load(open("spam_model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
#
# @app.route("/")
# def home():
#     return jsonify({"message": "Spam Detection API Running"})
#
#//Detecter router
# @app.route("/detect", methods=["POST"])
# def detect_spam():
#
#     data = request.json
#     email_text = data.get("email")
#
#     if not email_text:
#         return jsonify({"error": "Email text required"}), 400
#
#     transformed = vectorizer.transform([email_text])
#
#     prediction = model.predict(transformed)[0]
#
#     result = "Spam" if prediction == 1 else "Not Spam"
#
#     return jsonify({
#         "email": email_text,
#         "prediction": result
#     })
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

import pickle

# Load model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

print("Spam Mail Detector Started")
print("Paste message and press ENTER twice to analyze")
print("Type 'exit' to quit\n")

while True:

    print("Enter Message:\n")

    lines = []

    while True:
        line = input()

        # stop program
        if line.lower() == "exit":
            print("Program stopped")
            exit()

        # empty line means input finished
        if line == "":
            break

        lines.append(line)

    # Convert multiple lines → single line
    message = " ".join(lines)

    # Remove extra spaces
    message = " ".join(message.split())

    print("\nProcessed Text:")
    print(message)

    # Transform text
    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    result = "SPAM" if prediction == 1 else "NOT SPAM"

    print("\nPrediction:", result)
    print("-" * 60)