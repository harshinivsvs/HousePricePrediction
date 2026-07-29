import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="Data Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Analysis Dashboard")
st.write("This page provides an exploratory analysis of the USA Housing dataset.")

# ----------------------------------------
# Load Dataset
# ----------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("dataset/housing.csv")

df = load_data()

# ----------------------------------------
# Dataset Preview
# ----------------------------------------
st.header("📋 Dataset Preview")
st.dataframe(df.head())

st.header("🎲 Random Sample")
st.dataframe(df.sample(5))

# ----------------------------------------
# Dataset Information
# ----------------------------------------
st.header("📑 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", int(df.isnull().sum().sum()))

st.write("### Column Names")
st.write(df.columns.tolist())

st.write("### Data Types")
st.dataframe(df.dtypes.astype(str))

# ----------------------------------------
# Statistical Summary
# ----------------------------------------
st.header("📈 Statistical Summary")
st.dataframe(df.describe())

# ----------------------------------------
# Missing Values
# ----------------------------------------
st.header("❌ Missing Values")

missing = df.isnull().sum()

st.dataframe(missing)

if missing.sum() == 0:
    st.success("✅ No Missing Values Found")
else:
    st.warning("⚠ Dataset contains Missing Values.")

# ----------------------------------------
# Correlation Heatmap
# ----------------------------------------
st.header("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(10,7))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Price Distribution
# ----------------------------------------
st.header("🏠 House Price Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Price"],
    bins=30,
    kde=True,
    color="royalblue",
    ax=ax
)

ax.set_xlabel("House Price")
ax.set_ylabel("Count")

st.pyplot(fig)

# ----------------------------------------
# Income Distribution
# ----------------------------------------
st.header("💰 Income Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Avg. Area Income"],
    bins=30,
    kde=True,
    color="green",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Population Distribution
# ----------------------------------------
st.header("👨‍👩‍👧 Area Population Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Area Population"],
    bins=30,
    kde=True,
    color="orange",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# House Age Distribution
# ----------------------------------------
st.header("🏡 House Age Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Avg. Area House Age"],
    bins=30,
    kde=True,
    color="purple",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Rooms Distribution
# ----------------------------------------
st.header("🚪 Rooms Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Avg. Area Number of Rooms"],
    bins=30,
    kde=True,
    color="red",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Bedrooms Distribution
# ----------------------------------------
st.header("🛏 Bedrooms Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Avg. Area Number of Bedrooms"],
    bins=20,
    kde=True,
    color="teal",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Income vs Price
# ----------------------------------------
st.header("📈 Income vs House Price")

fig, ax = plt.subplots(figsize=(8,6))

sns.scatterplot(
    x=df["Avg. Area Income"],
    y=df["Price"],
    color="blue",
    ax=ax
)

ax.set_xlabel("Average Area Income")
ax.set_ylabel("House Price")

st.pyplot(fig)

# ----------------------------------------
# Rooms vs Price
# ----------------------------------------
st.header("🏠 Rooms vs House Price")

fig, ax = plt.subplots(figsize=(8,6))

sns.scatterplot(
    x=df["Avg. Area Number of Rooms"],
    y=df["Price"],
    color="darkgreen",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Population vs Price
# ----------------------------------------
st.header("👨‍👩‍👧 Population vs House Price")

fig, ax = plt.subplots(figsize=(8,6))

sns.scatterplot(
    x=df["Area Population"],
    y=df["Price"],
    color="darkorange",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Box Plot
# ----------------------------------------
st.header("📦 House Price Box Plot")

fig, ax = plt.subplots(figsize=(8,2))

sns.boxplot(
    x=df["Price"],
    color="skyblue",
    ax=ax
)

st.pyplot(fig)

# ----------------------------------------
# Conclusion
# ----------------------------------------
st.header("📝 Key Observations")

st.success("""
✅ The dataset contains **5000 housing records**.

✅ No missing values are present.

✅ Average Area Income has a strong positive correlation with House Price.

✅ Most numerical features have meaningful relationships with the target variable.

✅ Linear Regression is an appropriate algorithm for this dataset.
""")

st.info("""
This analysis helps us understand the dataset before training the Machine Learning model.
""")