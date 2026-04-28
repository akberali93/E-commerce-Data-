import streamlit as st
import pandas as pd
import plotly.express as px

st.title("E Commerce Sales Data Analysis Dashboard")

st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)  
    return data

data_path = "ecommerce.csv" 
data = load_data(data_path)

st.sidebar.header("Filters")

select_city = st.sidebar.multiselect(
    "Select City", options=data["City"].unique(), default=data["City"].unique()
)

select_product = st.sidebar.multiselect(
    "Select Product", options=data["Product Name"].unique(), default=data["Product Name"].unique()
)

select_segment = st.sidebar.multiselect(
    "Select Segment", options=data["Segment"].unique(), default=data["Segment"].unique()
)

select_category = st.sidebar.multiselect(
    "Select Category", options=data["Category"].unique(), default=data["Category"].unique()
)
filtered_data = data[
    (data["City"].isin(select_city)) &
    (data["Product Name"].isin(select_product)) &
    (data["Segment"].isin(select_segment)) &
    (data["Category"].isin(select_category))
]
 
st.dataframe(filtered_data)

total_sales = filtered_data["Sales"].sum().round(2)
total_profit = filtered_data["Profit"].sum().round(2)
total_discount = filtered_data["Discount"].sum().round(2)
total_quantity = filtered_data["Quantity"].sum().round(2)
cust_row = filtered_data["Row ID"].nunique()

st.subheader("Key Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="Total Customers", value=cust_row)

with col2:
    st.metric(label="Total Sales", value=total_sales)

with col3:
    st.metric(label="Total Profit", value=total_profit)

with col4:
    st.metric(label="Total Quantity", value=total_quantity)

with col5:
    st.metric(label="Total Discount", value=total_discount)

col7, col8 = st.columns(2)

sales_by_country = filtered_data.groupby("Country")["Sales"].sum().reset_index()

with col7:
    fig_country = px.bar(
        sales_by_country,
        x="Country",
        y="Sales",
        title="Total Sales By Country",
        text="Sales",
        color="Country"
    )
    st.plotly_chart(fig_country, use_container_width=True)

sales_by_region = filtered_data.groupby("Region")["Sales"].sum().reset_index()

with col8:
    fig_region = px.bar(
        sales_by_region,
        x="Region",
        y="Sales",
        title="Total Sales By Region",
        text="Sales",
        color="Region"
    )
    st.plotly_chart(fig_region, use_container_width=True)

sales_by_city = filtered_data.groupby("City")["Sales"].sum().reset_index()

fig_city_pie = px.pie(
    sales_by_city,
    values="Sales",
    names="City",
    title="Sales Distribution by City",
    hole=0.4
)
st.plotly_chart(fig_city_pie, use_container_width=True)