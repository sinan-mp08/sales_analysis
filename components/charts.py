import plotly.express as px
import plotly.graph_objects as go


def sales_trend(df):
    sales = (
        df.groupby("OrderDate", as_index=False)["Sales"].sum().sort_values("OrderDate")
    )

    fig = px.area(sales, x="OrderDate", y="Sales", template="plotly_dark")

    fig.update_traces(line=dict(width=3))

    fig.update_layout(
        height=420,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        title="📈 Sales Trend",
    )

    return fig


def sales_trend(df):

    sales = (
        df.groupby("OrderDate", as_index=False)["Sales"].sum().sort_values("OrderDate")
    )

    fig = px.area(
        sales,
        x="OrderDate",
        y="Sales",
        template="plotly_dark",
    )

    fig.update_traces(
        line=dict(width=3),
    )

    fig.update_layout(
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=430,
        margin=dict(l=10, r=10, t=45, b=10),
        title="📈 Sales Trend",
    )

    return fig


def region_sales(df):

    region = df.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales")

    fig = px.bar(
        region,
        x="Sales",
        y="Region",
        orientation="h",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=430,
        margin=dict(l=10, r=10, t=45, b=10),
        title="🌍 Sales by Region",
    )

    return fig


def category_sales(df):

    fig = px.sunburst(
        df,
        path=["Category", "SubCategory"],
        values="Sales",
        color="Profit",
        color_continuous_scale="RdYlGn",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=430,
        margin=dict(l=10, r=10, t=40, b=10),
        title="🌞 Category Performance",
    )

    return fig


def customer_segments(df):

    seg = df.groupby("Segment", as_index=False)["Sales"].sum()

    fig = px.treemap(
        seg,
        path=["Segment"],
        values="Sales",
        template="plotly_dark",
    )

    fig.update_layout(
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        title="👥 Customer Segments",
        height=420,
    )

    return fig


def top_products(df):

    top = (
        df.groupby("ProductName", as_index=False)["Sales"]
        .sum()
        .nlargest(10, "Sales")
        .sort_values("Sales")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=top["Sales"],
            y=top["ProductName"],
            mode="markers",
            marker=dict(size=14),
        )
    )

    for _, row in top.iterrows():
        fig.add_shape(
            type="line",
            x0=0,
            x1=row["Sales"],
            y0=row["ProductName"],
            y1=row["ProductName"],
        )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        title="🏆 Top Products",
        height=500,
    )

    return fig


def monthly_heatmap(df):

    heat = df.assign(
        Year=df["OrderDate"].dt.year,
        Month=df["OrderDate"].dt.strftime("%b"),
    ).pivot_table(
        index="Year",
        columns="Month",
        values="Sales",
        aggfunc="sum",
    )

    fig = px.imshow(
        heat,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        title="📅 Monthly Sales Heatmap",
        height=420,
    )

    return fig


def scatter_sales_profit(df):

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
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=430,
        title="📈 Sales vs Profit",
    )

    return fig
