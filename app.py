import streamlit as st

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="AI House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Sidebar
# ----------------------------------------
st.sidebar.title("🏠 Navigation")
st.sidebar.success("Select a page from below")

st.sidebar.markdown("""
### 📂 Project Pages

- 📊 Data Analysis
- 📈 Model Performance
- 💰 Predict House Price
- ℹ️ About

Use the sidebar to navigate through the application.
""")

# ----------------------------------------
# Main Title
# ----------------------------------------
st.title("🏠 AI House Price Prediction System")

st.markdown("""
## Welcome 👋

This application predicts **house prices** using a **Linear Regression Machine Learning Model**.

The project demonstrates the complete Machine Learning workflow, including:

- Data Analysis
- Model Building
- Model Evaluation
- House Price Prediction
""")

st.divider()

# ----------------------------------------
# Project Workflow
# ----------------------------------------
st.header("📌 Project Workflow")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
### 📊 Data Analysis

- Dataset Preview
- Statistical Summary
- Missing Values
- Correlation Heatmap
- Distribution Graphs
""")

with col2:
    st.success("""
### 🤖 Model Building

- Data Preprocessing
- Feature Selection
- Train-Test Split
- Linear Regression Training
""")

with col3:
    st.warning("""
### 📈 Model Performance

- MAE
- RMSE
- R² Score
- Actual vs Predicted
- Residual Analysis
""")

with col4:
    st.error("""
### 💰 Prediction

- User Input
- House Price Estimation
- Prediction Summary
""")

st.divider()

# ----------------------------------------
# Technologies
# ----------------------------------------
st.header("🛠 Technologies Used")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Language", "Python")

with c2:
    st.metric("Framework", "Streamlit")

with c3:
    st.metric("ML Library", "Scikit-Learn")

with c4:
    st.metric("Dataset", "USA Housing")

st.divider()

# ----------------------------------------
# Project Objective
# ----------------------------------------
st.header("🎯 Project Objective")

st.write("""
The objective of this project is to estimate the price of a house based on the following features:

- 💰 Average Area Income
- 🏡 Average Area House Age
- 🚪 Average Number of Rooms
- 🛏 Average Number of Bedrooms
- 👨‍👩‍👧 Area Population

The model uses **Linear Regression**, a supervised machine learning algorithm, to predict house prices accurately.
""")

st.divider()

# ----------------------------------------
# Dataset Information
# ----------------------------------------
st.header("📂 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Dataset Name:** USA Housing Dataset")
    st.write("**Number of Records:** 5000")
    st.write("**Target Variable:** Price")

with col2:
    st.write("**Machine Learning Algorithm:** Linear Regression")
    st.write("**Features Used:** 5")
    st.write("**Programming Language:** Python")

st.divider()

# ----------------------------------------
# How to Use
# ----------------------------------------
st.header("🚀 How to Use")

st.markdown("""
1. 📊 Explore the dataset in **Data Analysis**.
2. 📈 View model evaluation in **Model Performance**.
3. 💰 Predict house prices in **Predict House Price**.
4. ℹ️ Learn more about the project in **About**.
""")

st.success("👈 Use the sidebar on the left to navigate between pages.")

st.divider()

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("### 🏠 AI House Price Prediction")

st.write("**Developed by:** Harshini Vedulla")

st.write("**Course:** B.Tech Computer Science and Engineering")

st.write("**University:** Amrita Vishwa Vidyapeetham")

st.caption("Powered by Python • Streamlit • Scikit-Learn")