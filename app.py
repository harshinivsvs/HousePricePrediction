import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Home Page
# --------------------------------------------------
st.title("🏠 AI House Price Prediction System")

st.markdown("""
## Welcome 👋

This application predicts **house prices** using a **Linear Regression Machine Learning Model**.

The project demonstrates the complete Machine Learning workflow including:

- 📊 Data Analysis
- 🤖 Model Building
- 📈 Model Performance Evaluation
- 💰 House Price Prediction

👈 **Use the sidebar on the left to navigate between pages.**
""")

st.divider()

# --------------------------------------------------
# Project Workflow
# --------------------------------------------------
st.header("📌 Project Workflow")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
### 📊 Data Analysis

- Dataset Preview
- Statistical Summary
- Missing Values
- Correlation Heatmap
- Data Visualization
""")

with col2:
    st.success("""
### 🤖 Model Building

- Data Preprocessing
- Feature Selection
- Train-Test Split
- Linear Regression Model
""")

with col3:
    st.warning("""
### 📈 Model Performance

- MAE
- RMSE
- R² Score
- Residual Analysis
- Actual vs Predicted
""")

with col4:
    st.error("""
### 💰 Prediction

- User Input
- Price Prediction
- Property Category
- Prediction Summary
""")

st.divider()

# --------------------------------------------------
# Technologies Used
# --------------------------------------------------
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

# --------------------------------------------------
# Project Objective
# --------------------------------------------------
st.header("🎯 Project Objective")

st.write("""
The objective of this project is to estimate house prices using the following features:

- 💰 Average Area Income
- 🏡 Average Area House Age
- 🚪 Average Number of Rooms
- 🛏 Average Number of Bedrooms
- 👨‍👩‍👧 Area Population

The prediction model is built using **Linear Regression**, a supervised machine learning algorithm.
""")

st.divider()

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------
st.header("📂 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Dataset Name:** USA Housing Dataset")
    st.write("**Number of Records:** 5000")
    st.write("**Target Variable:** Price")

with col2:
    st.write("**Machine Learning Algorithm:** Linear Regression")
    st.write("**Number of Features:** 5")
    st.write("**Deployment:** Streamlit Cloud")

st.divider()

# --------------------------------------------------
# Application Features
# --------------------------------------------------
st.header("✨ Application Features")

st.markdown("""
- 📊 Interactive Data Analysis Dashboard
- 📈 Machine Learning Model Evaluation
- 💰 Real-Time House Price Prediction
- 📉 Correlation Heatmap
- 📋 Statistical Summary
- 🤖 Linear Regression Model
- 🌐 Deployed using Streamlit Cloud
""")

st.divider()

# --------------------------------------------------
# How to Use
# --------------------------------------------------
st.header("🚀 How to Use")

st.markdown("""
1. Open **Data Analysis** to explore the dataset.
2. Open **Model Performance** to view evaluation metrics.
3. Open **Predict House Price** and enter house details.
4. Click **Predict House Price** to estimate the price.
5. Open **About** to learn more about the project.
""")

st.info("👈 Use the Streamlit sidebar (automatically shown on the left) to switch between pages.")

st.divider()

# --------------------------------------------------
# Developer
# --------------------------------------------------
st.header("👩‍💻 Developer")

st.write("**Harshini Vedulla**")
st.write("B.Tech Computer Science and Engineering")
st.write("Amrita Vishwa Vidyapeetham")

st.divider()

st.success("🎉 Welcome to the AI House Price Prediction System!")

st.caption("Developed using Python • Streamlit • Scikit-Learn")