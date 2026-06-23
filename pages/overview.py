import streamlit as st
from components.charts import (
    sales_trend,
    region_sales,
    category_sales,
    customer_segments,
    top_products,
)
from utils.calculations import calculate_kpis


def overview_page(filtered_df):

    # KPI Cards
    kpis = calculate_kpis(filtered_df)

    k1, k2, k3, k4, k5, k6 = st.columns(6)

    cards = [
        ("💰 Revenue", f"₹{kpis['Revenue']:,.0f}"),
        ("📈 Profit", f"₹{kpis['Profit']:,.0f}"),
        ("🛒 Orders", f"{kpis['Orders']:,}"),
        ("👥 Customers", f"{kpis['Customers']:,}"),
        ("💳 AOV", f"₹{kpis['AOV']:,.0f}"),
        ("📊 Margin", f"{kpis['Margin']:.2f}%"),
    ]

    for col, (title, value) in zip(
        [k1, k2, k3, k4, k5, k6],
        cards,
    ):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-title">{title}</div>
                    <div class="kpi-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("<br>", unsafe_allow_html=True)

    # Placeholder Chart Layout
    # ==========================
    # Row 1
    # ==========================

    left, right = st.columns([2, 1])

    with left:
        st.plotly_chart(
            sales_trend(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            region_sales(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 2
    # ==========================

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            category_sales(filtered_df),
            use_container_width=True,
        )

    with right:
        st.plotly_chart(
            customer_segments(filtered_df),
            use_container_width=True,
        )

    # ==========================
    # Row 3
    # ==========================

    st.plotly_chart(
        top_products(filtered_df),
        use_container_width=True,
    )
    st.markdown("---")
    st.subheader("📋 Sales Transactions")

    display_df = filtered_df[
        [
            "OrderDate",
            "CustomerName",
            "Category",
            "SubCategory",
            "ProductName",
            "Region",
            "Sales",
            "Profit",
            "Quantity",
        ]
    ].copy()

    display_df["Sales"] = display_df["Sales"].map(lambda x: f"₹{x:,.2f}")

    display_df["Profit"] = display_df["Profit"].map(lambda x: f"₹{x:,.2f}")

    rows = st.selectbox(
        "Show Records",
        [10, 25, 50, 100],
        index=1,
    )

    st.data_editor(
        display_df.head(rows),
        use_container_width=True,
        hide_index=True,
        disabled=True,
    )
