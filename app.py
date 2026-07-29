import streamlit as st

# ----------------------------------------
# Page Configuration (MUST BE FIRST)
# ----------------------------------------
st.set_page_config(
    page_title="AI House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# TEST (Remove later)
# -----------------------------
st.success("🏠 HOME PAGE (app.py) LOADED SUCCESSFULLY")

# ----------------------------------------
# Sidebar Navigation
# ----------------------------------------
st.sidebar.title("🏠 Navigation")

st.sidebar.page_link("app.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/1_Data_Analysis.py", label="📊 Data Analysis", icon="📊")
st.sidebar.page_link("pages/2_Model_Performance.py", label="📈 Model Performance", icon="📈")
st.sidebar.page_link("pages/3_Predict_House_Price.py", label="💰 Predict House Price", icon="💰")
st.sidebar.page_link("pages/4_About.py", label="ℹ️ About", icon="ℹ️")