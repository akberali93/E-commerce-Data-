import streamlit as st #streamlit - Front end framework
import pandas as pd #data wrangling library in python
import plotly.express as px #Dynamic Visualization library in python

st.title("E Commerce Sales analysis Dashboard")

def load_data(file_path):
    data=pd.read_csv(file_path)
    return data
data_path="./ecommerce.csv"

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.sidebar.header("Filter Data")

if "Category" in df.columns:
    category = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )
    df = df[df["Category"].isin(category)]

if "Region" in df.columns:
    region = st.sidebar.multiselect(
        "Select Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )
    df = df[df["Region"].isin(region)]


st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

if "Sales" in df.columns:
    col1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")

if "Profit" in df.columns:
    col2.metric("Total Profit", f"{df['Profit'].sum():,.0f}")

col3.metric("Total Orders", len(df))

st.subheader("Visualizations")

if "Category" in df.columns and "Sales" in df.columns:
    fig1 = px.bar(df, x="Category", y="Sales", color="Category", title="Sales by Category")
    st.plotly_chart(fig1, use_container_width=True)

if "Region" in df.columns and "Profit" in df.columns:
    fig2 = px.pie(df, names="Region", values="Profit", title="Profit by Region")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Data Explorer")
st.dataframe(df)