import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("ℹ️ About This Project")

st.write("""
Welcome to the **House Price Prediction System**.

This application uses **Machine Learning** to estimate house prices based on
different housing features. It is developed as a mini project to demonstrate
the complete Machine Learning workflow, including data analysis, model training,
performance evaluation, and prediction.
""")

st.divider()

# ---------------------------------------------------
# Project Overview
# ---------------------------------------------------
st.header("📌 Project Overview")

st.write("""
The House Price Prediction System predicts the estimated price of a house
using **Linear Regression**, a supervised machine learning algorithm.

The prediction is based on the following housing features:

- 💰 Average Area Income
- 🏡 Average Area House Age
- 🚪 Average Number of Rooms
- 🛏 Average Number of Bedrooms
- 👨‍👩‍👧 Area Population
""")

# ---------------------------------------------------
# Technologies Used
# ---------------------------------------------------
st.header("🛠 Technologies Used")

st.markdown("""
- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Joblib**
""")

# ---------------------------------------------------
# Machine Learning Workflow
# ---------------------------------------------------
st.header("⚙️ Machine Learning Workflow")

st.markdown("""
1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Linear Regression Model Training
7. Model Evaluation
8. House Price Prediction
""")

# ---------------------------------------------------
# Model Information
# ---------------------------------------------------
st.header("🤖 Model Information")

st.write("""
**Algorithm Used:** Linear Regression

Linear Regression predicts the house price by finding the relationship between
the input features and the target variable (Price).

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
""")

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------
st.header("📊 Dataset Information")

st.write("""
The project uses the **USA Housing Dataset**.

The dataset contains **5,000 records** with **7 columns**:

- Avg. Area Income
- Avg. Area House Age
- Avg. Area Number of Rooms
- Avg. Area Number of Bedrooms
- Area Population
- Price
- Address
""")

# ---------------------------------------------------
# Features of the Application
# ---------------------------------------------------
st.header("✨ Features")

st.markdown("""
✅ Home Dashboard

✅ Data Analysis Dashboard

✅ Correlation Heatmap

✅ Statistical Summary

✅ Model Performance Evaluation

✅ House Price Prediction

✅ Interactive User Interface

✅ Machine Learning Powered Predictions
""")

# ---------------------------------------------------
# Advantages
# ---------------------------------------------------
st.header("🎯 Advantages")

st.markdown("""
- Fast price prediction
- Easy to use interface
- Accurate Machine Learning model
- Interactive visualizations
- Beginner-friendly implementation
""")

# ---------------------------------------------------
# Future Enhancements
# ---------------------------------------------------
st.header("🚀 Future Enhancements")

st.markdown("""
- Deploy the application online
- Add multiple Machine Learning algorithms
- Improve prediction accuracy
- Accept CSV file uploads
- Add real estate market trends
- Integrate maps and location-based pricing
""")

# ---------------------------------------------------
# Developer
# ---------------------------------------------------
st.header("👩‍💻 Developer")

st.write("""
**Name:** Harshini Vedulla

**Course:** B.Tech Computer Science and Engineering

**Project:** House Price Prediction using Machine Learning

**Framework:** Streamlit
""")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.divider()

st.success("🎉 Thank you for exploring the House Price Prediction System!")

st.caption("Developed using Python, Streamlit, and Machine Learning")