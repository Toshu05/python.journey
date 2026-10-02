# ============================================================
# 1. DOWNLOAD DATASET
# ============================================================

medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

from urllib.request import urlretrieve

urlretrieve(medical_charges_url, 'medical.csv')


# ============================================================
# 2. LOAD DATASET
# ============================================================

import pandas as pd

medical_df = pd.read_csv('medical.csv')


# ============================================================
# 3. INSPECT DATASET
# ============================================================

print("--- Head ---")
print(medical_df.head())

print("\n--- Tail ---")
print(medical_df.tail())

print("\n--- Shape ---")
print(medical_df.shape)

print("\n--- Columns ---")
print(medical_df.columns)

print("\n--- Info ---")
medical_df.info()

print("\n--- Describe ---")
print(medical_df.describe())


# ============================================================
# 4. CHECK DATA TYPES AND MISSING VALUES
# ============================================================

print("\n--- Data Types ---")
print(medical_df.dtypes)

print("\n--- Missing Values ---")
print(medical_df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(medical_df.duplicated().sum())


# ============================================================
# 5. SELECTING, FILTERING AND SORTING
# ============================================================

# 1. Select one column
print("\n--- Charges ---")
print(medical_df["charges"])


# 2. Select multiple columns
print("\n--- Selected Columns ---")
print(medical_df[["age", "bmi", "smoker", "charges"]])


# 3. Filter rows: BMI over 30
print("\n--- BMI > 30 ---")
print(medical_df[medical_df["bmi"] > 30])


# 4. Multiple conditions: smokers over age 40
print("\n--- Smokers over age 40 ---")
print(
    medical_df[
        (medical_df["age"] > 40) &
        (medical_df["smoker"] == "yes")
    ]
)


# 5. Sort by medical charges: highest to lowest
print("\n--- Charges: Highest to Lowest ---")
print(
    medical_df.sort_values(
        by="charges",
        ascending=False
    )
)


# 6. Select by integer position
print("\n--- First 5 Rows, First 3 Columns ---")
print(medical_df.iloc[0:5, 0:3])


# 7. Select by labels
print("\n--- Selected Rows and Columns ---")
print(
    medical_df.loc[
        0:5,
        ["age", "bmi", "smoker", "charges"]
    ]
)


# ============================================================
# 6. DATA CLEANING
# ============================================================

# Remove duplicate rows
medical_df = medical_df.drop_duplicates()

# Count missing values
print("\n--- Missing Values After Removing Duplicates ---")
print(medical_df.isnull().sum())

# Remove rows with missing values
medical_df = medical_df.dropna()

# Fill missing numeric values with median
medical_df["bmi"] = medical_df["bmi"].fillna(
    medical_df["bmi"].median()
)

# Fill missing categorical values with mode
medical_df["region"] = medical_df["region"].fillna(
    medical_df["region"].mode()[0]
)

# Convert charges to numeric
medical_df["charges"] = pd.to_numeric(
    medical_df["charges"],
    errors="coerce"
)


# ============================================================
# 7. DATA ANALYSIS AND FEATURE ENGINEERING
# ============================================================

# Mean
print("\nMean Charges:")
print(medical_df["charges"].mean())

# Median
print("\nMedian Charges:")
print(medical_df["charges"].median())

# Minimum
print("\nMinimum Charges:")
print(medical_df["charges"].min())

# Maximum
print("\nMaximum Charges:")
print(medical_df["charges"].max())


# Count smokers
print("\n--- Smoker Count ---")
print(medical_df["smoker"].value_counts())


# Percentage of smokers
smoker_percentage = (
    (medical_df["smoker"] == "yes").mean() * 100
)

print("\nPercentage of Smokers:")
print(smoker_percentage)


# Average charges by region
print("\n--- Average Charges by Region ---")
print(
    medical_df.groupby("region")["charges"].mean()
)


# Multiple statistics by smoker status
print("\n--- Charges by Smoker Status ---")
print(
    medical_df.groupby("smoker")["charges"].agg(
        ["mean", "min", "max"]
    )
)


# Create a new feature
medical_df["age_children_ratio"] = (
    medical_df["age"] * medical_df["children"]
)


# Correlation matrix
print("\n--- Correlation Matrix ---")
print(
    medical_df[
        ["age", "bmi", "children", "charges"]
    ].corr()
)


# ============================================================
# 8. VISUALIZATION
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

# Histogram
medical_df["charges"].hist()

plt.xlabel("Charges")
plt.ylabel("Frequency")
plt.title("Distribution of Medical Charges")
plt.show()


# Scatter plot
plt.scatter(
    medical_df["age"],
    medical_df["charges"]
)

plt.xlabel("Age")
plt.ylabel("Charges")
plt.title("Age vs Medical Charges")
plt.show()


# Categorical counts
medical_df["smoker"].value_counts().plot(
    kind="bar"
)

plt.xlabel("Smoker")
plt.ylabel("Count")
plt.title("Number of Smokers vs Non-Smokers")
plt.show()


# ============================================================
# 9. SCIKIT-LEARN: PREPARE THE DATA
# ============================================================

from sklearn.model_selection import train_test_split

# Encode smoker
medical_df["smoker_encoded"] = (
    medical_df["smoker"] == "yes"
).astype(int)


# Features
X = medical_df[
    ["age", "bmi", "children", "smoker_encoded"]
]

# Target
y = medical_df["charges"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n--- Train/Test Shapes ---")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


# ============================================================
# 10. SCALING
# ============================================================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# Convert scaled data back to DataFrame for inspection
X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

print("\n--- Scaled Training Data ---")
print(X_train_scaled_df.head())


# ============================================================
# 11. LINEAR REGRESSION
# ============================================================

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()

linear_model.fit(
    X_train_scaled,
    y_train
)

linear_pred = linear_model.predict(X_test_scaled)


# ============================================================
# 12. RANDOM FOREST REGRESSION
# ============================================================

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)


# Feature importances
print("\n--- Feature Importances ---")

print(
    pd.Series(
        rf_model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)
)


# ============================================================
# 13. EVALUATE RANDOM FOREST MODEL
# ============================================================

import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


mae = mean_absolute_error(
    y_test,
    rf_pred
)

mse = mean_squared_error(
    y_test,
    rf_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    rf_pred
)


print("\n--- Random Forest Evaluation ---")

print(f"MAE: ${mae:.2f}")

print(f"MSE: {mse:.2f}")

print(f"RMSE: ${rmse:.2f}")

print(f"R² Score: {r2:.4f}")


# ============================================================
# 14. COMPLETE MINI PRACTICAL
# ============================================================

# Create a small sample medical dataset

sample_df = pd.DataFrame({

    "age": [
        19, 18, 28, 33, 32, 31,
        46, 37, 37, 60, 25, 62
    ],

    "sex": [
        "female", "male", "male", "male",
        "male", "female", "female", "female",
        "male", "female", "male", "female"
    ],

    "bmi": [
        27.9, 33.77, 33.0, 22.7,
        28.88, 25.74, 33.44, 27.74,
        29.83, 25.84, 26.22, 26.29
    ],

    "children": [
        0, 1, 3, 0, 0, 0,
        1, 3, 2, 0, 0, 0
    ],

    "smoker": [
        "yes", "no", "no", "no",
        "no", "no", "no", "no",
        "no", "no", "no", "yes"
    ],

    "region": [
        "southwest", "southeast", "southeast",
        "northwest", "northwest", "southeast",
        "southeast", "northwest", "northeast",
        "northwest", "northeast", "southeast"
    ],

    "charges": [
        16884.92, 1725.55, 4449.46, 21984.47,
        3866.86, 3756.62, 8240.59, 7281.50,
        6406.41, 28923.14, 2721.32, 27808.72
    ]
})


# Inspect sample data
print("\n--- Sample Dataset Head ---")
print(sample_df.head())

print("\n--- Sample Dataset Summary ---")
print(sample_df.describe())


# ============================================================
# 15. ENCODE CATEGORICAL VARIABLES
# ============================================================

sample_df_encoded = pd.get_dummies(
    sample_df,
    columns=["sex", "smoker", "region"],
    drop_first=True
)


# Define X and y
X = sample_df_encoded.drop(
    columns=["charges"]
)

y = sample_df_encoded["charges"]


# ============================================================
# 16. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# ============================================================
# 17. TRAIN RANDOM FOREST
# ============================================================

final_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

final_model.fit(
    X_train,
    y_train
)


# ============================================================
# 18. PREDICT
# ============================================================

y_pred = final_model.predict(X_test)


# ============================================================
# 19. EVALUATE
# ============================================================

print("\n--- Final Model Evaluation ---")

print(
    f"R² Score: {r2_score(y_test, y_pred):.4f}"
)

print(
    f"Mean Absolute Error (MAE): "
    f"${mean_absolute_error(y_test, y_pred):.2f}"
)

print(
    f"Root Mean Squared Error (RMSE): "
    f"${np.sqrt(mean_squared_error(y_test, y_pred)):.2f}"
)


# ============================================================
# 20. PREDICT FOR A NEW PATIENT
# ============================================================

new_patient = pd.DataFrame({

    "age": [35],

    "bmi": [29.5],

    "children": [2],

    "sex_male": [1],

    "smoker_yes": [1],

    "region_northwest": [0],

    "region_southeast": [1],

    "region_southwest": [0]
})


# Make sure columns match training data exactly
new_patient = new_patient.reindex(
    columns=X.columns,
    fill_value=0
)


predicted_charge = final_model.predict(
    new_patient
)


print(
    f"\nPredicted Medical Charges for New Patient: "
    f"${predicted_charge[0]:,.2f}"
)