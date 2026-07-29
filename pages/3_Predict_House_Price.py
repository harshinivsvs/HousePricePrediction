import streamlit as st
import joblib
import numpy as np

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Predict House Price",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("model/house_price_model.pkl")

model = load_model()

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("🏠 House Price Prediction")

st.write("""
Enter the property details below and click **Predict House Price**
to estimate the market value using the trained Machine Learning model.
""")

st.divider()

# ---------------------------------------------------
# Input Section
# ---------------------------------------------------
st.header("📥 Enter House Details")

col1, col2 = st.columns(2)

with col1:

    income = st.number_input(
        "💰 Average Area Income",
        min_value=0.0,
        value=70000.0,
        step=1000.0
    )

    age = st.number_input(
        "🏡 Average Area House Age",
        min_value=0.0,
        value=6.0,
        step=0.5
    )

    rooms = st.number_input(
        "🚪 Average Number of Rooms",
        min_value=0.0,
        value=7.0,
        step=0.5
    )

with col2:

    bedrooms = st.number_input(
        "🛏 Average Number of Bedrooms",
        min_value=0.0,
        value=4.0,
        step=0.5
    )

    population = st.number_input(
        "👨‍👩‍👧 Area Population",
        min_value=0.0,
        value=35000.0,
        step=500.0
    )

st.write("")

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------
if st.button("🔍 Predict House Price", use_container_width=True):

    features = np.array([[
        income,
        age,
        rooms,
        bedrooms,
        population
    ]])

    prediction = model.predict(features)[0]

    st.balloons()

    st.success("Prediction Completed Successfully!")

    c1, c2, c3 = st.columns(3)

    with c2:
        st.metric(
            label="🏠 Estimated House Price",
            value=f"${prediction:,.2f}"
        )

    st.divider()

    st.subheader("📊 Property Category")

    if prediction >= 1500000:
        st.success("🏆 Luxury House")

    elif prediction >= 1000000:
        st.info("🏡 Premium House")

    elif prediction >= 700000:
        st.warning("🏠 Mid-Range House")

    else:
        st.error("💰 Budget-Friendly House")

    st.divider()

    st.subheader("📝 Prediction Summary")

    st.write(f"**Average Area Income:** ${income:,.2f}")
    st.write(f"**Average House Age:** {age:.1f} Years")
    st.write(f"**Average Rooms:** {rooms}")
    st.write(f"**Average Bedrooms:** {bedrooms}")
    st.write(f"**Area Population:** {population:,.0f}")

    st.success(f"### 💲 Predicted House Price: ${prediction:,.2f}")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.divider()

st.caption(
    "House Price Prediction using Linear Regression | Developed by Harshini Vedulla"
)