import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go 

# ============================
# 1. LOAD & INSPECT DATA
# ============================
df = pd.read_csv("DATA.csv")

st.header("Real Estate Property Analysis Dashboard")

st.subheader("Dataset Overview")
st.write(df.head())
st.write(df.describe())
st.write("Missing Values:", df.isnull().sum())
st.write("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# ============================
# 2. UNIQUE CATEGORY COUNTS
# ============================
unique_counts = {
    "Property Type": df["property_type"].nunique(),
    "Neighborhood": df["neighborhood"].nunique(),
    "Garage Spaces": df["garage_spaces"].nunique(),
    "View Types": df["view"].nunique(),
    "Heating Type": df["heating_type"].nunique(),
    "Cooling Type": df["cooling_type"].nunique(),
    "Foundation Type": df["foundation_type"].nunique(),
    "Roof Material": df["roof_material"].nunique()
}

fig1 = go.Figure(go.Bar(
    x=list(unique_counts.keys()),
    y=list(unique_counts.values()),
    marker_color="skyblue"
))
fig1.update_layout(
    title="Unique Categories in Dataset",
    xaxis_title="Category",
    yaxis_title="Count",
    template="plotly_white"
)
st.plotly_chart(fig1, use_container_width=True)

# ============================
# 3. TOTAL COST / SELLING PRICE / PROFIT
# ============================
total_renovation_cost = df["renovation_cost"].sum()
total_selling_price = df["selling_price"].sum()
overall_profit = total_selling_price - total_renovation_cost

labels = ["Renovation Cost", "Selling Price", "Profit"]
values = [total_renovation_cost, total_selling_price, overall_profit]

fig2 = go.Figure(go.Pie(labels=labels, values=values, textinfo="percent+label"))
fig2.update_layout(title="Renovation vs Selling Price vs Profit")
st.plotly_chart(fig2, use_container_width=True)

# ============================
# 4. RENOVATION YEAR
# ============================
before_2000 = df[df["renovation_year"] < 2000].shape[0]
after_2000 = df[df["renovation_year"] >= 2000].shape[0]

fig3 = go.Figure(go.Pie(
    labels=["Before 2000", "After 2000"],
    values=[before_2000, after_2000],
    textinfo="percent+label"
))
fig3.update_layout(title="Renovation Year Distribution")
st.plotly_chart(fig3, use_container_width=True)

# ============================
# 5. PROPERTY TYPE VS TOTAL PRICE
# ============================
property_price = df.groupby("property_type")["selling_price"].sum()

fig4 = go.Figure(go.Bar(
    x=property_price.index,
    y=property_price.values,
    marker_color="red"
))
fig4.update_layout(
    title="Total Selling Price by Property Type",
    xaxis_title="Property Type",
    yaxis_title="Total Price",
    template="plotly_white"
)
st.plotly_chart(fig4, use_container_width=True)

# ============================
# 6. BEDROOM WISE PRICE
# ============================
bedrooms = df.groupby("bedrooms")["selling_price"].sum()

palette = sns.color_palette("husl", len(bedrooms))
colors = ["rgb({},{},{})".format(int(r*255), int(g*255), int(b*255)) for r, g, b in palette]

fig5 = go.Figure(go.Bar(
    x=bedrooms.index,
    y=bedrooms.values,
    marker_color=colors
))
fig5.update_layout(
    title="Total Selling Price by Bedrooms",
    xaxis_title="Bedrooms",
    yaxis_title="Selling Price",
    template="plotly_white"
)
st.plotly_chart(fig5, use_container_width=True)

# ============================
# 7. POOL WISE PRICE
# ============================
avg_pool = df.groupby(df["pool"].map({True: "Pool", False: "No Pool"}))["selling_price"].mean()

fig6 = go.Figure(go.Bar(
    x=avg_pool.index,
    y=avg_pool.values,
    marker_color=["#2cd4c6", "#0e37ed"],
    text=avg_pool.values,
    textposition="outside"
))
fig6.update_layout(
    title="Average Price: Pool vs No Pool",
    template="plotly_white"
)
st.plotly_chart(fig6, use_container_width=True)

# ============================
# 8. FIREPLACE WISE PRICE
# ============================
avg_fireplace = df.groupby(df["fireplace"].map({True: "Fireplace", False: "No Fireplace"}))["selling_price"].mean()

fig7 = go.Figure(go.Bar(
    x=avg_fireplace.index,
    y=avg_fireplace.values,
    marker_color=["#2cd4c6", "#0e37ed"],
    text=avg_fireplace.values,
    textposition="outside"
))
fig7.update_layout(
    title="Average Price: With & Without Fireplace",
    template="plotly_white"
)
st.plotly_chart(fig7, use_container_width=True)

# ============================
# 9. VIEW WISE PRICE
# ============================
df["view_category"] = df["view"].str.capitalize()
avg_view = df.groupby("view_category")["selling_price"].mean()

fig8 = go.Figure(go.Bar(
    x=avg_view.index,
    y=avg_view.values,
    marker_color=["#2cd4c6", "#0e37ed", "#10ebd8"],
    text=avg_view.values,
    textposition="outside"
))
fig8.update_layout(
    title="Average Price by View Type",
    template="plotly_white"
)
st.plotly_chart(fig8, use_container_width=True)

# ============================
# 10. SALES TREND
# ============================
df["selling_date"] = pd.to_datetime(df["selling_date"])
sales_trend = df.groupby("selling_date")["selling_price"].sum()

fig9 = go.Figure(go.Scatter(
    x=sales_trend.index,
    y=sales_trend.values,
    mode="lines+markers"
))
fig9.update_layout(
    title="Sales Trend Over Time",
    xaxis_title="Date",
    yaxis_title="Selling Price",
    template="plotly_white"
)
st.plotly_chart(fig9, use_container_width=True)

# ============================
# 11. CORRELATION HEATMAP
# ============================
corr = df.corr(numeric_only=True).round(2)

fig_corr = go.Figure(go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.index,
    colorscale="RdBu",
    reversescale=True
))
fig_corr.update_layout(
    title="Correlation Between Numerical Features",
    xaxis_title="Features",
    yaxis_title="Features"
)
st.plotly_chart(fig_corr, use_container_width=True)
