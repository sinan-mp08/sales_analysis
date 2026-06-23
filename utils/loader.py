import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv("data/retail_sales_cleaned.csv")

    # Convert dates
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["ShipDate"] = pd.to_datetime(df["ShipDate"])

    return df
