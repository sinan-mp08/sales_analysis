import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def top_products(df):

    top = df.groupby("ProductName", as_index=False)["Sales"].sum().nlargest(10, "Sales")

    fig = px.bar(
        top,
        x="Sales",
        y="ProductName",
        orientation="h",
        template="plotly_dark",
        text_auto=True,
    )

    fig.update_layout(
        title="🏆 Top Products",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def bottom_products(df):

    bottom = (
        df.groupby("ProductName", as_index=False)["Sales"].sum().nsmallest(10, "Sales")
    )

    fig = px.bar(
        bottom,
        x="Sales",
        y="ProductName",
        orientation="h",
        template="plotly_dark",
        text_auto=True,
    )

    fig.update_layout(
        title="📉 Bottom Products",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def category_performance(df):

    fig = px.sunburst(
        df,
        path=["Category", "SubCategory"],
        values="Sales",
        color="Profit",
        color_continuous_scale="RdYlGn",
    )

    fig.update_layout(
        title="📦 Category Performance",
        template="plotly_dark",
        paper_bgcolor="#161F2F",
        height=450,
    )

    return fig


def product_profitability(df):

    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        size="Quantity",
        color="Category",
        hover_name="ProductName",
        template="plotly_dark",
    )

    fig.update_layout(
        title="💰 Product Profitability", paper_bgcolor="#161F2F", height=450
    )

    return fig


def pareto_chart(df):

    pareto = (
        df.groupby("ProductName")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    pareto["Cum%"] = pareto["Sales"].cumsum() / pareto["Sales"].sum() * 100

    fig = go.Figure()

    fig.add_bar(x=pareto["ProductName"][:20], y=pareto["Sales"][:20], name="Sales")

    fig.add_scatter(
        x=pareto["ProductName"][:20],
        y=pareto["Cum%"][:20],
        yaxis="y2",
        mode="lines+markers",
        name="Cum %",
    )

    fig.update_layout(
        template="plotly_dark",
        title="Pareto Analysis (80/20)",
        yaxis2=dict(overlaying="y", side="right", range=[0, 100]),
        height=500,
    )

    return fig


def subcategory_performance(df):

    sub = (
        df.groupby("SubCategory", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        sub,
        x="Sales",
        y="SubCategory",
        orientation="h",
        color="Sales",
        color_continuous_scale="Blues",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="📂 Sub-Category Performance",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=450,
        coloraxis_showscale=False,
    )

    return fig


def discount_analysis(df):

    discount = df.groupby("Category", as_index=False)["Discount"].mean()

    fig = px.bar(
        discount,
        x="Category",
        y="Discount",
        color="Discount",
        color_continuous_scale="Oranges",
        text_auto=".1%",
        template="plotly_dark",
    )

    fig.update_layout(
        title="🏷 Average Discount by Category",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=450,
        coloraxis_showscale=False,
    )

    fig.update_yaxes(tickformat=".0%")

    return fig


def quantity_analysis(df):

    qty = df.groupby("Category", as_index=False)["Quantity"].sum()

    fig = px.bar(
        qty,
        x="Category",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Viridis",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="📦 Quantity Sold by Category",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=450,
        coloraxis_showscale=False,
    )

    return fig
