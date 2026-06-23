import streamlit as st

from components.geography_charts import (
    region_sales,
    region_profit,
    top_states,
    top_cities,
    region_distribution,
    state_distribution,
)


def geography_page(filtered_df):

    st.header("🌍 Geography Analytics")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("🌎 Countries", filtered_df["Country"].nunique())
    c2.metric("🏙 States", filtered_df["State"].nunique())
    c3.metric("📍 Cities", filtered_df["City"].nunique())
    c4.metric("🗺 Regions", filtered_df["Region"].nunique())
    c5.metric("💰 Avg Sales", f"₹{filtered_df['Sales'].mean():,.0f}")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.plotly_chart(region_sales(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(region_profit(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(top_states(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(top_cities(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(region_distribution(filtered_df), use_container_width=True)

    with right:
        st.plotly_chart(state_distribution(filtered_df), use_container_width=True)
