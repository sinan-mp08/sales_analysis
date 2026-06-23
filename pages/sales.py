import streamlit as st

from utils.calculations import calculate_kpis


from components.sales_charts import (
    monthly_sales,
    monthly_profit,
    quarterly_sales,
    sales_heatmap,
    discount_profit,
    sales_profit,
)


def sales_page(filtered_df):

    kpis = calculate_kpis(filtered_df)

    c1, c2, c3, c4, c5 = st.columns(5)

    metrics = [
        ("💰 Revenue", f"₹{kpis['Revenue']:,.0f}"),
        ("📈 Profit", f"₹{kpis['Profit']:,.0f}"),
        ("🛒 Orders", f"{kpis['Orders']:,}"),
        ("💳 AOV", f"₹{kpis['AOV']:,.0f}"),
        ("📊 Margin", f"{kpis['Margin']:.2f}%"),
    ]

    for col, (title, value) in zip([c1, c2, c3, c4, c5], metrics):
        with col:
            st.metric(title, value)

    # ==========================
    # Row 1
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            monthly_sales(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            monthly_profit(filtered_df),
            use_container_width=True,
        )

    # Row 2 (Coming Next)
    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            quarterly_sales(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            sales_heatmap(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 3
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            discount_profit(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            sales_profit(filtered_df),
            use_container_width=True,
        )
