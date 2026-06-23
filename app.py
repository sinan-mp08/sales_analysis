import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu

# ================================
# Data Loader
# ================================

from utils.loader import load_data

# ================================
# Pages
# ================================

from pages.overview import overview_page
from pages.sales import sales_page
from pages.customers import customer_page
from pages.products import product_page
from pages.geography import geography_page

# ================================
# Page Config
# ================================

st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ================================
# Load CSS
# ================================

with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True,
    )

# ================================
# Load Dataset
# ================================


@st.cache_data
def get_data():
    return load_data()


df = get_data()

# ================================
# Header
# ================================


st.markdown(
    """
<h1 style="color:white;", align="center">Sales Analysis Dashboard</h1>
""",
    unsafe_allow_html=True,
)


# ================================
# Navigation
# ================================

selected = option_menu(
    menu_title=None,
    options=[
        "Overview",
        "Sales",
        "Customers",
        "Products",
        "Geography",
    ],
    icons=[
        "house-fill",
        "graph-up-arrow",
        "people-fill",
        "box-seam-fill",
        "globe-central-south-asia",
    ],
    orientation="horizontal",
    default_index=0,
)

st.markdown("<br>", unsafe_allow_html=True)

# ================================
# Filter Container
# ================================

st.markdown(
    '<div class="filter-container">',
    unsafe_allow_html=True,
)


# ================================
# Filter Data
# ================================

regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
segments = ["All"] + sorted(df["Segment"].dropna().unique().tolist())
ship_modes = ["All"] + sorted(df["ShipMode"].dropna().unique().tolist())

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    region = st.selectbox(
        "🌍 Region",
        regions,
    )

with c2:
    category = st.selectbox(
        "📦 Category",
        categories,
    )

with c3:
    segment = st.selectbox(
        "👤 Segment",
        segments,
    )

with c4:
    ship_mode = st.selectbox(
        "🚚 Ship Mode",
        ship_modes,
    )

with c5:
    search = st.text_input(
        "🔍 Search Product",
        placeholder="Type product name...",
    )

with c6:
    date_range = st.date_input(
        "📅 Date Range",
        value=(
            df["OrderDate"].min(),
            df["OrderDate"].max(),
        ),
    )

st.markdown("</div>", unsafe_allow_html=True)

# ================================
# Apply Filters
# ================================

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if segment != "All":
    filtered_df = filtered_df[filtered_df["Segment"] == segment]

if ship_mode != "All":
    filtered_df = filtered_df[filtered_df["ShipMode"] == ship_mode]

if search.strip():

    filtered_df = filtered_df[
        filtered_df["ProductName"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

# ================================
# Date Filter
# ================================

if len(date_range) == 2:

    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["OrderDate"] >= pd.to_datetime(start_date))
        & (filtered_df["OrderDate"] <= pd.to_datetime(end_date))
    ]

# ================================
# Empty Dataset
# ================================

if filtered_df.empty:

    st.warning("⚠ No records found for the selected filters.")

    st.stop()

# ================================
# Quick Dashboard Summary
# ================================

st.caption(f"""
Showing **{len(filtered_df):,}** records |
🌍 {region} |
📦 {category} |
👤 {segment}
""")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# PAGE ROUTING
# ==========================================

if selected == "Overview":
    overview_page(filtered_df)

elif selected == "Sales":
    sales_page(filtered_df)

elif selected == "Customers":
    customer_page(filtered_df)

elif selected == "Products":
    product_page(filtered_df)

elif selected == "Geography":
    geography_page(filtered_df)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# DOWNLOAD FILTERED DATA
# ==========================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv",
    use_container_width=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# DASHBOARD INFO
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"📄 Records : {len(filtered_df):,}")

with col2:
    st.info(f"💰 Revenue : ₹{filtered_df['Sales'].sum():,.0f}")

with col3:
    st.info(f"📈 Profit : ₹{filtered_df['Profit'].sum():,.0f}")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
<div class="footer">

<b>📊 E-Commerce Analytics Dashboard</b><br>

Developed by <b>Mohammed Sinan</b><br>

Internship Project • 2026 • Powered by Streamlit & Plotly

</div>
""",
    unsafe_allow_html=True,
)
