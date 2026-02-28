import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import datetime

# Load dataset
df = pd.read_csv("car.csv")

# Create Years of Service
current_year = datetime.datetime.now().year
df["Years"] = current_year - df["Year"]

# Drop unnecessary columns
df.drop(["Car_Name", "Year"], axis=1, inplace=True)

# Convert categorical variables
df = pd.get_dummies(df, drop_first=True)

# Features and Target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")