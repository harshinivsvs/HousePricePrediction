import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")

st.write(
    "This page evaluates the Linear Regression model using different performance metrics."
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("dataset/housing.csv")

df = load_data()

# --------------------------------------------------
# Prepare Data
# --------------------------------------------------
df = df.drop("Address", axis=1)

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# --------------------------------------------------
# Train Model
# --------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# --------------------------------------------------
# Metrics
# --------------------------------------------------
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

st.header("📊 Evaluation Metrics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("MAE", f"{mae:,.2f}")

with c2:
    st.metric("RMSE", f"{rmse:,.2f}")

with c3:
    st.metric("R² Score", f"{r2:.3f}")

st.success("Model Accuracy: {:.2f}%".format(r2 * 100))

# --------------------------------------------------
# Actual vs Predicted
# --------------------------------------------------
st.header("📈 Actual vs Predicted Prices")

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(
    y_test,
    predictions,
    color="royalblue"
)

ax.set_xlabel("Actual Price")
ax.set_ylabel("Predicted Price")
ax.set_title("Actual vs Predicted")

st.pyplot(fig)

# --------------------------------------------------
# Residual Distribution
# --------------------------------------------------
st.header("📉 Residual Distribution")

residuals = y_test - predictions

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    residuals,
    bins=30,
    kde=True,
    color="green",
    ax=ax
)

ax.set_xlabel("Residual Error")

st.pyplot(fig)

# --------------------------------------------------
# Residual Scatter
# --------------------------------------------------
st.header("📌 Residual Scatter Plot")

fig, ax = plt.subplots(figsize=(8,5))

ax.scatter(
    predictions,
    residuals,
    color="red"
)

ax.axhline(
    y=0,
    color="black",
    linestyle="--"
)

ax.set_xlabel("Predicted Price")
ax.set_ylabel("Residuals")

st.pyplot(fig)

# --------------------------------------------------
# Feature Importance
# --------------------------------------------------
st.header("📋 Feature Coefficients")

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

st.dataframe(coef_df)

# --------------------------------------------------
# Interpretation
# --------------------------------------------------
st.header("📝 Model Interpretation")

st.success("""
✅ The model achieved a high R² score.

✅ Lower MAE and RMSE indicate good prediction accuracy.

✅ Actual and Predicted values are closely aligned.

✅ Residuals are centered around zero, indicating a good model fit.

✅ Linear Regression performs well on this housing dataset.
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.caption(
    "Developed by Harshini Vedulla | House Price Prediction using Machine Learning"
)