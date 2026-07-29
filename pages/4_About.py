import streamlit as st

st.set_page_config(
    page_title="AI House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏠 AI House Price Prediction System")

st.sidebar.title("🏠 Navigation")
st.sidebar.page_link("app.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/1_Data_Analysis.py", label="📊 Data Analysis", icon="📊")
st.sidebar.page_link("pages/2_Model_Performance.py", label="📈 Model Performance", icon="📈")
st.sidebar.page_link("pages/3_Predict_House_Price.py", label="💰 Predict House Price", icon="💰")
st.sidebar.page_link("pages/4_About.py", label="ℹ️ About", icon="ℹ️")

st.markdown("""
## Welcome 👋

This application predicts **house prices** using a **Linear Regression Machine Learning Model**.

### Project Modules
- 📊 Data Analysis
- 📈 Model Performance
- 💰 Predict House Price
- ℹ️ About

Use the **sidebar** to navigate through the project.
""")

st.divider()

st.header("📌 Project Workflow")

c1,c2,c3,c4 = st.columns(4)

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

st.header("🛠 Technologies Used")

a,b,c,d = st.columns(4)
with a:
    st.metric("Language","Python")
with b:
    st.metric("Framework","Streamlit")
with c:
    st.metric("ML","Scikit-Learn")
with d:
    st.metric("Dataset","USA Housing")

st.divider()

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

st.header("📂 Dataset Information")

x,y = st.columns(2)
with x:
    st.write("**Dataset:** USA Housing")
    st.write("**Records:** 5000")
    st.write("**Target Variable:** Price")
with y:
    st.write("**Algorithm:** Linear Regression")
    st.write("**Features:** 5")
    st.write("**Deployment:** Streamlit Cloud")

st.divider()

st.header("🚀 How to Use")
st.markdown("""
1. Open **Data Analysis** to explore the dataset.
2. Open **Model Performance** to view evaluation metrics.
3. Open **Predict House Price** to estimate a house price.
4. Open **About** to learn more about the project.
""")

st.divider()

st.markdown("### 👩‍💻 Developed By")
st.write("**Harshini Vedulla**")
st.write("B.Tech Computer Science and Engineering")
st.write("Amrita Vishwa Vidyapeetham")

st.caption("Powered by Python • Streamlit • Scikit-Learn")