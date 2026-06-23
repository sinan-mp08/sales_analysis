import streamlit as st

from components.product_charts import *


def product_page(filtered_df):

    st.header("📦 Product Analytics")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("📦 Products", filtered_df["ProductID"].nunique())
    c2.metric("📂 Categories", filtered_df["Category"].nunique())
    c3.metric("🗂 SubCategories", filtered_df["SubCategory"].nunique())
    c4.metric("💰 Avg Price", f"₹{filtered_df['UnitPrice'].mean():.0f}")
    c5.metric("🏷 Avg Discount", f"{filtered_df['Discount'].mean()*100:.1f}%")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(top_products(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(bottom_products(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(category_performance(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(subcategory_performance(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(product_profitability(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(pareto_chart(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(discount_analysis(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(quantity_analysis(filtered_df), use_container_width=True)
