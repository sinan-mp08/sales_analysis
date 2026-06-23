import pandas as pd


def calculate_kpis(df: pd.DataFrame):
    """Calculate dashboard KPI metrics."""

    revenue = df["Sales"].sum()
    profit = df["Profit"].sum()
    orders = df["OrderID"].nunique()
    customers = df["CustomerID"].nunique()
    quantity = df["Quantity"].sum()

    aov = revenue / orders if orders else 0
    margin = (profit / revenue * 100) if revenue else 0

    return {
        "Revenue": revenue,
        "Profit": profit,
        "Orders": orders,
        "Customers": customers,
        "Quantity": quantity,
        "AOV": aov,
        "Margin": margin,
    }
