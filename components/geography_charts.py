import plotly.express as px


def region_sales(df):

    region = df.groupby("Region", as_index=False)["Sales"].sum()

    fig = px.bar(
        region,
        x="Region",
        y="Sales",
        color="Sales",
        color_continuous_scale="Blues",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🌍 Sales by Region",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def region_profit(df):

    region = df.groupby("Region", as_index=False)["Profit"].sum()

    fig = px.bar(
        region,
        x="Region",
        y="Profit",
        color="Profit",
        color_continuous_scale="RdYlGn",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="💰 Profit by Region",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def top_states(df):

    state = df.groupby("State", as_index=False)["Sales"].sum().nlargest(10, "Sales")

    fig = px.bar(
        state,
        x="Sales",
        y="State",
        orientation="h",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🏙 Top States",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def top_cities(df):

    city = df.groupby("City", as_index=False)["Sales"].sum().nlargest(10, "Sales")

    fig = px.bar(
        city,
        x="Sales",
        y="City",
        orientation="h",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🏆 Top Cities",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def region_distribution(df):

    fig = px.pie(df, names="Region", hole=0.65, template="plotly_dark")

    fig.update_layout(
        title="🗺 Region Distribution",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def state_distribution(df):

    state = df.groupby("State", as_index=False)["Sales"].sum()

    fig = px.treemap(state, path=["State"], values="Sales", template="plotly_dark")

    fig.update_layout(
        title="🌍 State Distribution",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig
