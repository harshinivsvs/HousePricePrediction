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

### Project Modules
- 📊 Data Analysis
- 📈 Model Performance
- 💰 Predict House Price
- ℹ️ About

👈 Use the **Streamlit sidebar** on the left to navigate between pages.
""")

st.divider()

# --------------------------------------------------
# Project Workflow
# --------------------------------------------------
st.header("📌 Project Workflow")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info("""
### 📊 Data Analysis
- Dataset Preview
- Statistical Summary
- Missing Values
- Correlation Heatmap
- Visualizations
""")

with c2:
    st.success("""
### 🤖 Model Building
- Data Preprocessing
- Train/Test Split
- Linear Regression
- Model Training
""")

with c3:
    st.warning("""
### 📈 Model Performance
- MAE
- RMSE
- R² Score
- Residual Analysis
""")

with c4:
    st.error("""
### 💰 Prediction
- User Input
- House Price Prediction
- Property Category
""")

st.divider()

# --------------------------------------------------
# Technologies Used
# --------------------------------------------------
st.header("🛠 Technologies Used")

a, b, c, d = st.columns(4)

with a:
    st.metric("Language", "Python")

with b:
    st.metric("Framework", "Streamlit")

with c:
    st.metric("ML", "Scikit-Learn")

with d:
    st.metric("Dataset", "USA Housing")

st.divider()

# --------------------------------------------------
# Project Objective
# --------------------------------------------------
st.header("🎯 Project Objective")

st.write("""
Predict house prices using:

- 💰 Average Area Income
- 🏡 Average Area House Age
- 🚪 Average Number of Rooms
- 🛏 Average Number of Bedrooms
- 👨‍👩‍👧 Area Population
""")

st.divider()

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------
st.header("📂 Dataset Information")

x, y = st.columns(2)

with x:
    st.write("**Dataset:** USA Housing")
    st.write("**Records:** 5000")
    st.write("**Target Variable:** Price")

with y:
    st.write("**Algorithm:** Linear Regression")
    st.write("**Features:** 5")
    st.write("**Deployment:** Streamlit Cloud")

st.divider()

# --------------------------------------------------
# How to Use
# --------------------------------------------------
st.header("🚀 How to Use")

st.markdown("""
1. Open **Data Analysis** to explore the dataset.
2. Open **Model Performance** to view evaluation metrics.
3. Open **Predict House Price** to estimate a house price.
4. Open **About** to learn more about the project.
""")

st.divider()

# --------------------------------------------------
# Developer
# --------------------------------------------------
st.markdown("### 👩‍💻 Developed By")

st.write("**Harshini Vedulla**")
st.write("B.Tech Computer Science and Engineering")
st.write("Amrita Vishwa Vidyapeetham")

st.caption("Powered by Python • Streamlit • Scikit-Learn")