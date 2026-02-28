from flask import Flask, render_template, request
import pickle
import numpy as np

# -----------------------------
# Create Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Load Trained Model
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction Route
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        present_price = float(request.form["present_price"])
        kms_driven = float(request.form["kms_driven"])
        owner = int(request.form["owner"])
        years = float(request.form["years"])

        fuel = int(request.form["fuel_type"])
        seller = int(request.form["seller_type"])
        transmission = int(request.form["transmission"])

        # ----- Dummy Encoding (MATCH TRAINING) -----

        # Fuel Type Encoding
        fuel_diesel = 1 if fuel == 1 else 0
        fuel_petrol = 1 if fuel == 0 else 0

        # Seller Type Encoding
        seller_individual = 1 if seller == 1 else 0

        # Transmission Encoding
        transmission_manual = 1 if transmission == 0 else 0

        # FINAL FEATURE ORDER (VERY IMPORTANT)
        features = [[
            present_price,
            kms_driven,
            owner,
            years,
            fuel_diesel,
            fuel_petrol,
            seller_individual,
            transmission_manual
        ]]

        prediction = model.predict(features)
        output = round(prediction[0], 2)

        return render_template(
            "index.html",
            prediction_text=f"Estimated Car Price: ₹ {output} Lakhs"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error occurred: {str(e)}"
        )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1",
            port=5000,
            debug=False,
            use_reloader=False)