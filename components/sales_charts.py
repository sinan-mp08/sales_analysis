import plotly.express as px
import streamlit as st


def monthly_sales(df):

    monthly = df.groupby(df["OrderDate"].dt.to_period("M"))["Sales"].sum().reset_index()

    monthly["OrderDate"] = monthly["OrderDate"].astype(str)

    fig = px.area(
        monthly,
        x="OrderDate",
        y="Sales",
        markers=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="📈 Monthly Revenue Trend",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=420,
    )

    return fig


def monthly_profit(df):

    monthly = (
        df.groupby(df["OrderDate"].dt.to_period("M"))["Profit"].sum().reset_index()
    )

    monthly["OrderDate"] = monthly["OrderDate"].astype(str)

    fig = px.area(
        monthly,
        x="OrderDate",
        y="Profit",
        markers=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="💰 Monthly Profit Trend",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=420,
    )

    return fig


def sales_page(filtered_df):

    st.header("📈 Sales Analytics")

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            monthly_sales(filtered_df),
            use_container_width=True,
        )

    with c2:
        st.plotly_chart(
            monthly_profit(filtered_df),
            use_container_width=True,
        )


def quarterly_sales(df):

    quarter = df.groupby(df["OrderDate"].dt.to_period("Q"))["Sales"].sum().reset_index()

    quarter["OrderDate"] = quarter["OrderDate"].astype(str)

    fig = px.bar(
        quarter,
        x="OrderDate",
        y="Sales",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="📅 Quarterly Sales",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=400,
    )

    return fig


def discount_profit(df):

    fig = px.scatter(
        df,
        x="Discount",
        y="Profit",
        color="Category",
        size="Sales",
        template="plotly_dark",
    )

    fig.update_layout(
        title="🎯 Discount vs Profit",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=400,
    )

    return fig


def sales_profit(df):

    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        color="Segment",
        size="Quantity",
        hover_name="ProductName",
        template="plotly_dark",
    )

    fig.update_layout(
        title="📈 Sales vs Profit",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=400,
    )

    return fig


def sales_heatmap(df):

    heat = df.copy()

    heat["Year"] = heat["OrderDate"].dt.year
    heat["Month"] = heat["OrderDate"].dt.strftime("%b")

    pivot = heat.pivot_table(
        index="Year", columns="Month", values="Sales", aggfunc="sum"
    )

    fig = px.imshow(
        pivot,
        text_auto=True,
        color_continuous_scale="Blues",
    )

    fig.update_layout(
        title="🔥 Monthly Sales Heatmap",
        template="plotly_dark",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=400,
    )

    return fig
