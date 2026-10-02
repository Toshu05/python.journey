import numpy as np
import pandas as pd
from transformers import pipeline
from xgboost import XGBRegressor

# ---------------------------------------------------------
# STEP 1: NLP LAYER (Stance Extraction using a Pre-trained Transformer)
# ---------------------------------------------------------
# Load a pre-trained zero-shot classifier to infer stance on raw text
stance_analyzer = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Sample social media posts about a fictional tax policy debate
raw_posts = [
    "I love Candidate A, but this new tax proposal is absolute garbage!",
    "Candidate A is doing amazing work, full support for the new policy!",
    "This tax policy is terrible, Candidate A completely lost my vote.",
    "Candidate A's economic plan is brilliant, exactly what we needed."
]

candidate_target = "Candidate A"
candidate_stances = []

print("--- Running NLP Stance Detection ---")
for post in raw_posts:
    # Evaluate stance towards the specific target candidate
    result = stance_analyzer(post, candidate_labels=["Supports " + candidate_target, "Opposes " + candidate_target])
    
    # Extract support score (+1 for support, -1 for oppose)
    top_label = result['labels'][0]
    score = 1.0 if "Supports" in top_label else -1.0
    candidate_stances.append(score)
    print(f"Post: '{post}'\n  -> Inferred Stance Score: {score}\n")

# ---------------------------------------------------------
# STEP 2: ML LAYER (Popularity Trend Prediction with XGBoost)
# ---------------------------------------------------------
# Mock dataset: [Stance Score Average, Retweet/Engagement Speed] -> Target Popularity Change (%)
X_train = np.array([
    [0.80, 500],   # High support, moderate virality -> Popularity up
    [-0.75, 1200], # High opposition, high virality -> Popularity down heavily
    [0.10, 100],   # Mixed stance, low virality -> Neutral change
    [-0.90, 2000]  # Strong opposition, massive virality -> Popularity drops drastically
])
y_train = np.array([3.5, -4.2, 0.1, -6.8]) # Actual historical popularity percentage shifts

# Train a small XGBoost Regressor
ml_trend_model = XGBRegressor(n_estimators=10, max_depth=2, learning_rate=0.1)
ml_trend_model.fit(X_train, y_train)

# ---------------------------------------------------------
# STEP 3: PIPELINE EXECUTION (Combine NLP signals & Predict)
# ---------------------------------------------------------
# Aggregate current real-time batch results
avg_stance = np.mean(candidate_stances) # Average stance (-1 to +1)
current_virality_velocity = 850         # Retweets per minute (mock input)

# Predict future 24-hour popularity trajectory
X_current = np.array([[avg_stance, current_virality_velocity]])
predicted_trend = ml_trend_model.predict(X_current)[0]

print("--- ML Trend Engine Output ---")
print(f"Aggregated Stance Score: {avg_stance:.2f}")
print(f"Predicted Popularity Shift (24h): {predicted_trend:.2f}%")