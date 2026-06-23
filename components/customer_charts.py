import plotly.express as px


def top_customers(df):

    top = (
        df.groupby("CustomerName", as_index=False)["Sales"].sum().nlargest(10, "Sales")
    )

    fig = px.bar(
        top,
        x="Sales",
        y="CustomerName",
        orientation="h",
        text_auto=True,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🏆 Top Customers",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        font_color="white",
        height=450,
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
        title="👥 Customer Segments",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=20,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🎂 Age Distribution",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def gender_distribution(df):

    fig = px.pie(
        df,
        names="Gender",
        hole=0.65,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🚻 Gender Distribution",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def loyalty_distribution(df):

    fig = px.pie(
        df,
        names="LoyaltyTier",
        hole=0.65,
        template="plotly_dark",
    )

    fig.update_layout(
        title="💎 Loyalty Tier",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def repeat_customers(df):

    repeat = df.groupby("CustomerID").size().reset_index(name="Orders")

    repeat["Type"] = repeat["Orders"].apply(lambda x: "Repeat" if x > 1 else "New")

    summary = repeat.groupby("Type", as_index=False)["CustomerID"].count()

    fig = px.pie(
        summary,
        names="Type",
        values="CustomerID",
        hole=0.65,
        template="plotly_dark",
    )

    fig.update_layout(
        title="🔁 Repeat Customers",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=450,
    )

    return fig


def customer_lifetime_value(df):

    clv = (
        df.groupby("CustomerName", as_index=False)["Sales"].sum().nlargest(15, "Sales")
    )

    fig = px.bar(
        clv,
        x="Sales",
        y="CustomerName",
        orientation="h",
        template="plotly_dark",
        text_auto=True,
    )

    fig.update_layout(
        title="💰 Customer Lifetime Value",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=500,
    )

    return fig


def top_customer_cities(df):

    city = df.groupby("City", as_index=False)["Sales"].sum().nlargest(10, "Sales")

    fig = px.bar(
        city,
        x="Sales",
        y="City",
        orientation="h",
        template="plotly_dark",
        text_auto=True,
    )

    fig.update_layout(
        title="🏙️ Top Customer Cities",
        paper_bgcolor="#161F2F",
        plot_bgcolor="#161F2F",
        height=500,
    )

    return fig
