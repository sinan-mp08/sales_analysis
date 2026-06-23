import streamlit as st

from utils.calculations import calculate_kpis

from components.customer_charts import (
    top_customers,
    customer_segments,
    age_distribution,
    gender_distribution,
    loyalty_distribution,
    repeat_customers,
    customer_lifetime_value,
    top_customer_cities,
)


def customer_page(filtered_df):

    st.header("👥 Customer Analytics")

    # ==========================
    # KPIs
    # ==========================

    total_customers = filtered_df["CustomerID"].nunique()

    repeat = filtered_df.groupby("CustomerID").size().gt(1).sum()

    avg_customer_value = filtered_df.groupby("CustomerID")["Sales"].sum().mean()

    avg_age = filtered_df["Age"].mean()

    loyalty = filtered_df["LoyaltyTier"].notna().sum()

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("👥 Customers", f"{total_customers:,}")
    c2.metric("🔁 Repeat", f"{repeat:,}")
    c3.metric("💰 Avg Value", f"₹{avg_customer_value:,.0f}")
    c4.metric("🎂 Avg Age", f"{avg_age:.0f}")
    c5.metric("💎 Loyalty", f"{loyalty:,}")

    st.markdown("---")

    # ==========================
    # Row 1
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            top_customers(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            customer_segments(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 2
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            age_distribution(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            gender_distribution(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 3
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            loyalty_distribution(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            repeat_customers(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 4
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            customer_lifetime_value(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            top_customer_cities(filtered_df),
            use_container_width=True,
        )
