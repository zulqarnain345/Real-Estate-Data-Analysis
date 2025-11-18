import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go 

df=pd.read_csv("DATA.csv")
print(df.head(5))
print(df.describe())

# Check for Missing Values
print(df.isnull().sum())

# Check how many duplicate rows exist
duplicate=df.duplicated().sum()
print(f"there are no of {duplicate}")

# Display the duplicate rows
print(df[df.duplicated()])

# Remove duplicates (if any)
df = df.drop_duplicates()
print("After removing duplicates:", df.duplicated().sum())

# property Type
property_type=df["property_type"].nunique()

print(f"Types of Property:: {property_type}")

# types of neighborhood
neighborhood_types=df["neighborhood"].nunique()
print(f"Types of Neighborhood:: {neighborhood_types}")

# garage_spaces type 
garage_spaces=df["garage_spaces"].nunique()
print(f"Types garage_spaces:: {garage_spaces}")


# types of views 
views_types=df["view"].nunique()
print(f"Types of Views:: {views_types}")

# heating_type
heating_type=df["heating_type"].nunique()
print(f"Types of Heating:: {heating_type}")

# cooling_type
cooling_type=df["cooling_type"].nunique()
print(f"Types of Cooling:: {cooling_type}")

# foundation_type
foundation_type=df["foundation_type"].nunique()
print(f"Types of foundation :: {foundation_type}")

# roof_material type
roof_material=df["roof_material"].nunique()
print(f"Types of Roof Material :: {roof_material}")

category=["property_type","neighborhood_types","garage_spaces","views_types","heating_type","cooling_type","foundation_type","roof_material"]

values=[property_type,neighborhood_types,garage_spaces,views_types,heating_type,cooling_type,foundation_type,roof_material]

fig1=go.Figure()
fig1.add_trace(go.Bar(x=category,y=values,marker_color="skyblue",name="Bar chart"
))
fig1.update_layout(title="Number of Unique Categories in Property Dataset",
    xaxis_title="Category",yaxis_title="Unique Values Count",
    template="plotly_white"
)
st.plotly_chart(fig1,use_container_width=True)

# plt.figure(figsize=(10,6))
# plt.bar(category,values,color="skyblue",edgecolor="black")
# plt.title("Number of Unique Categories in Property Dataset", fontsize=14)
# plt.xlabel("Category", fontsize=12)
# plt.ylabel("Unique Values Count", fontsize=12)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.grid(True,linestyle="--",alpha=0.5)
# # plt.show()
# print("\n")

# total renovation_cost
total_renovation_cost=df["renovation_cost"].sum(axis=0)
print(f"The Total  Renovation cost of the properties are:: {total_renovation_cost}")

# selling_price
total_selling_price=df["selling_price"].sum(axis=0)
print(f"The Total  Selling Price of all the properties are:: {total_selling_price}")

# overall profit from these properties are 
overall_profit=total_selling_price-total_renovation_cost
print(f"The overall profit from all these properties we get is ::{overall_profit}")
chart=["Total Renovation Cost","Total Selling Price","Overall Profit"]
values=[total_renovation_cost,total_selling_price,overall_profit]

fig2=go.Figure(go.Pie(labels=chart,values=values,textinfo="percent+label")
)
fig2.update_layout(title="COST")
st.plotly_chart(fig2,use_container_width=True)

# pie chart of price
# plt.figure(figsize=(10,6))
# plt.pie(values,labels=chart,autopct="%1.1f%%",startangle=90)
# plt.title("COST")
# plt.axis("equal")
# plt.tight_layout()
# # plt.show()



# renovation_year which is held before the 2000
renovation_y=df[df["renovation_year"]<2000].shape[0]
print(f"\nNumbers of properties renovate before 2000 ::{renovation_y}")

renovation_ye=df[df["renovation_year"]>2000].shape[0]
print(f"\nNumbers of properties renovate after 2000 ::{renovation_ye}")

chart=["Renovation Before 2000","Renovation After 2000"]
values=[renovation_y,renovation_ye]

fig3=go.Figure(go.Pie(
    values=values,labels=chart,textinfo="percent+label"
))
fig3.update_layout(title="CHART SHOWS RENOVATION YEARS")
st.plotly_chart(fig3,use_container_width=True)

# pie chart 
# plt.pie(values,labels=chart,autopct="%1.1f%%",startangle=90)
# plt.title("CHART SHOWS RENOVATION YEARS")
# plt.axis("equal")
# plt.tight_layout()
# # plt.show()

# Property Type vs Price
property_type1=df.groupby("property_type")["selling_price"].sum()
print("\n",property_type1)

fig4=go.Figure()
fig4.add_trace(go.Bar(
    x=property_type1.index,y=property_type1.values,marker_color="red"
))
fig4.update_layout(
    title="Chart show the each category total selling price ",xaxis_title="category",
    yaxis_title="Price",template="plotly_white"
)
st.plotly_chart(fig4,use_container_width=True)

# # bar chart show the each property type by the selling price 
# plt.figure(figsize=(12,6))
# plt.bar(property_type1.index,property_type1.values,color="red",edgecolor="black")
# plt.tight_layout()
# plt.xlabel("category")
# plt.ylabel("Price")
# plt.title("Chart show the each category total selling price ")
# plt.xticks(rotation=45)
# plt.grid(True,linestyle="--",alpha=0.5)
# # plt.show()

# bedrooms wise total price 
bedrooms=df.groupby("bedrooms")["selling_price"].sum()
print("\n",bedrooms)

# # give the each graph different color 



unique_bedroom=df["bedrooms"].unique()
palette=sns.color_palette("husl",len(unique_bedroom))
palette_hex=["rgb({},{},{})".format(int(r*255),int(g*255),int(b*255))for r,g,b in palette]
brand_color={brand: palette_hex[i %len(palette_hex)]for i,brand in enumerate(unique_bedroom)}

# if len(unique_bedroom)<=10:
#     palette=sns.color_palette("tab10",len(unique_bedroom))
# elif len(unique_bedroom)<=20:
#     palette=sns.color_palette("tab20",len(unique_bedroom))
# else:
#     palette=sns.color_palette("husl",len(unique_bedroom))
# bedroom_color_map={bedrooms: palette[i % len(unique_bedroom)]for i,bedrooms  in enumerate(unique_bedroom)}
# colors=[bedroom_color_map[bedrooms] for bedrooms in df["bedrooms"]]

# chart show the bedrooms per price 
fig5=go.Figure()
fig5.add_trace(go.Bar(x=bedrooms.index,y=bedrooms.values,
                      marker_color=[brand_color[b]for b in bedrooms.index]
))
fig5.add_hline(
    y=bedrooms.mean(),line_dash="dash",line_color="Black",
    annotation_text="Average",annotation_position="top left"
)
fig5.update_layout(
    title="PER BEDROOM TOTAL PRICE",xaxis_title="BEDROOM",
    yaxis_title="PRICE",template="plotly_white"
)
st.plotly_chart(fig5,use_container_width=True)


# plt.figure(figsize=(12,6))
# plt.bar(bedrooms.index,bedrooms.values,color=colors,edgecolor="black")
# plt.axhline(df["bedrooms"].mean(),linestyle="--",linewidth=2,color="black",label="average")
# plt.title("PER BEDROOM TOTAL PRICE")
# plt.xlabel("BEDROOM")
# plt.ylabel("PRICE")
# plt.tight_layout()
# plt.grid(True,linestyle="--",alpha=0.5)
# plt.xticks(rotation=45)
# plt.legend()
# # plt.show()

# pool wise price
pool=df.groupby("pool")["selling_price"].sum()
# bar chart show the pool wise price 

fig6=go.Figure()

fig6.add_trace(go.Bar(
    x=pool.index,
    y=pool.values,
    marker_color=[brand_color.get(b, "gray") for b in pool.index]
))
fig6.update_layout(
    title="CHART SHOW THE PRICE OF POOL WITH OR WITHOUT",
    xaxis_title="POOL",yaxis_title="Price",template="plotly_white"
)
st.plotly_chart(fig6,use_container_width=True)

# plt.bar(pool.index,pool.values,color=colors)
# plt.title("CHART SHOW THE PRICE OF POOL WITH OR WITHOUT ")
# plt.xlabel("POOL")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # fireplace wise price
fireplace=df.groupby("fireplace")["selling_price"].sum()

# chart show the price of fireplace with or without 
fig7=go.Figure()
fig7.add_trace(go.Bar(x=fireplace.index,y=fireplace.values,
                      marker_color=[brand_color.get(b,"yellow")for b in fireplace.index]
))
fig7.update_layout(
    title="CHART SHOW THE PRICE OF fireplace WITH OR WITHOUT ",
    xaxis_title="Fireplace",yaxis_title="Price",template="plotly_white"
)
st.plotly_chart(fig7,use_container_width=True)

# plt.figure(figsize=(12,6))
# plt.bar(fireplace.index,fireplace.values,color=colors,edgecolor="black")
# plt.title("CHART SHOW THE PRICE OF fireplace WITH OR WITHOUT ")
# plt.xlabel("Fireplace")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # view wise price
view=df.groupby("view")["selling_price"].sum()
# chart show the view wise price 
fig8=go.Figure()
fig8.add_trace(go.Bar(
    x=view.index,y=view.values,marker_color=[brand_color.get(b,"white")for b in view.index]
))
fig8.update_layout(
    title="CHART SHOW THE PRICE OF view wise price",xaxis_title="view Type",yaxis_title="Price",template="plotly_white"
)
st.plotly_chart(fig8,use_container_width=True)


# plt.figure(figsize=(12,6))
# plt.bar(view.index,view.values,color=colors,edgecolor="black")
# plt.title("CHART SHOW THE PRICE OF view wise price")
# plt.xlabel("view Type")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # heating_type wise price 
heating_type=df.groupby("heating_type")["selling_price"].sum()

# # heating_type chart show the price wise
# plt.figure(figsize=(12,8))
# plt.bar(heating_type.index,heating_type.values,color=colors,edgecolor="black")
# plt.title("CHART SHOW THE PRICE OF ON  THE  BASES OF HEATIING TYPE")
# plt.xlabel("HEATING TYPE")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # cooling_type wise group 
cooling_type=df.groupby("cooling_type")["selling_price"].sum()
# cooling_type chart show the price 
fig9=go.Figure()
fig9.add_trace(go.Bar(
    x=cooling_type.index,y=cooling_type.values,
    marker_color=[brand_color.get(b,"green")for b in cooling_type.index]
))
fig9.update_layout(
    title="CHART SHOW THE PRICE OF ON THE BASES cooling type",xaxis_title="COOLING TYPE",
    yaxis_title="Price",template="plotly_white"

)
st.plotly_chart(fig9,use_container_width=True)


# plt.figure(figsize=(12,8))
# plt.bar(cooling_type.index,cooling_type.values,color=colors,edgecolor="black")
# plt.title("CHART SHOW THE PRICE OF ON THE BASES cooling type")
# plt.xlabel("COOLING TYPE")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # roof_material wise price 
roof_material=df.groupby("roof_material")["selling_price"].sum()
# roof_material wise chart show the price
fig10=go.Figure()
fig10.add_trace(go.Bar(
    x=roof_material.index,y=roof_material.values,marker_color="red"
))
fig10.update_layout(
    title="CHART SHOW THE PRICE OF ON THE BASES ROOF type",xaxis_title="ROOF TYPE",
    yaxis_title="Price",
    template="plotly_white"
)
st.plotly_chart(fig10,use_container_width=True)

# plt.figure(figsize=(12,8))
# plt.bar(roof_material.index,roof_material.values,color=colors,edgecolor="black")
# plt.title("CHART SHOW THE PRICE OF ON THE BASES ROOF type")
# plt.xlabel("ROOF TYPE")
# plt.ylabel("Price")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# # plt.show()

# # garage_spaces wise price 
garage_spaces1=df.groupby("garage_spaces")["selling_price"].sum()
# bar chart show the garage_spaces
fig11=go.Figure()
fig11.add_trace(go.Bar(
    x=garage_spaces1.index,y=garage_spaces1.values,marker_color="white"
))
fig11.update_layout(
    title="group by chart show the garage_spaces",xaxis_title="Garage Spaces",yaxis_title="price",template="plotly_white"
)
st.plotly_chart(fig11,use_container_width=True)

# plt.figure(figsize=(12,8))
# plt.bar(garage_spaces1.index,garage_spaces1.values,color=colors,edgecolor="black")
# plt.xlabel("Garage Spaces")
# plt.ylabel("price")
# plt.title("group by chart show the garage_spaces")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.tight_layout()
# plt.xticks(rotation=45)
# # plt.show()

# sales trend over time 
df["selling_date"]=pd.to_datetime(df["selling_date"])
sales_trend=df.groupby("selling_date")["selling_price"].sum()
fig12=go.Figure()
fig12.add_trace(go.Scatter(
    x=sales_trend.index,y=sales_trend.values,mode="lines+markers",line=dict(color="red",width=2),marker=dict(size=8,color="red"),name="trand"
))
fig12.update_layout(
    title="sale trend over time",xaxis_title="Date",yaxis_title="Price",template="plotly_white",hovermode="x unified",xaxis=dict(showgrid=True,gridwidth=1,gridcolor="lightGray"),yaxis=dict(showgrid=True,gridwidth=1,gridcolor="lightGray")
)
st.plotly_chart(fig12,use_container_width=True)

# plt.figure(figsize=(14, 8))
# plt.plot(sales_trend.index,sales_trend.values,color="blue",marker="o")
# plt.grid(True,alpha=0.5,linestyle="--")
# plt.title("sale trend over time")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.tight_layout()
# # plt.show()

correlation = df.select_dtypes(include=['int64', 'float64']).corr()
# heatmap
fig13=go.Figure(data=go.Heatmap(
    z=correlation.values,x=correlation.columns,y=correlation.index,colorscale="viridis",zmin=-1,zmax=1,colorbar=dict(title="correlation")
))
fig13.update_layout(title="correlation Heatmap",template="plotly_white")
st.plotly_chart(fig13,use_container_width=True)

# plt.figure(figsize=(16, 10))
# sns.heatmap(
#     df.corr(numeric_only=True).round(2),
#     annot=True,
#     cmap="coolwarm",
#     linewidths=0.5,
#     annot_kws={"size": 8}
# )
# plt.title("Correlation Between Numerical Features", fontsize=16, pad=15)
# plt.xticks(rotation=45, ha='right', fontsize=9)
# plt.yticks(rotation=0, fontsize=9)
# plt.tight_layout()
# # plt.show()

# distance_to_school
df["school_distance_category"] = df["distance_to_school"].apply(
    lambda x: "Near" if x <= 5 else "Far")
print(df[["distance_to_school", "school_distance_category"]])

#Average price for “Near” and “Far” categories
avg_price_near_far=df.groupby('school_distance_category')["selling_price"].mean().round(2)
print(f"\nThe average price of the propert Near and Far \n{avg_price_near_far}")
# barchart
# plt.bar(avg_price_near_far.index, avg_price_near_far.values, color=["green", "red"], edgecolor="black")
# for i, val in enumerate(avg_price_near_far.values):
#     plt.text(i, val, f"{val:.0f}", ha="center", va="bottom", fontsize=10)
# plt.title("Average Selling Price: Near vs Far Properties")
# plt.xlabel("Distance Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# year_built
df["year_built_category"]=df["year_built"].apply(lambda x: "Before 2000" if x<2000 else "After 2000")
print(df[["year_built" , "year_built_category"]])

# average price for before 2000 and after 2000
avg_year=df.groupby("year_built_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert Before and After 2000 \n{avg_year}")

fig14=go.Figure()
fig14.add_trace(go.Bar(
    x=avg_year.index,y=avg_year.values,marker_color=['#ff0000', '#00ff00'],marker_line_color="black",marker_line_width=1.5,text=avg_year.values,textposition="outside"
))
fig14.update_layout(
    title="Average Selling Price: before vs after 2000",xaxis_title="Before After 2000 Category",yaxis_title="Average Selling Price",template="plotly_white"
)
st.plotly_chart(fig14,use_container_width=True)

# bar chart
# plt.bar(avg_year.index,avg_year.values,color=["red","green"],edgecolor="black")
# for i,val in enumerate(avg_year.values):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price: before vs after 2000")
# plt.xlabel("Before After 2000 Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# lot_size 
df['lot_size_category']=df["lot_size"].apply(lambda x: "small" if x<=3 else "medium" if x<=6 else "big")
print(df[["lot_size","lot_size_category"]])

# average price for lot size
avg_lot_size=df.groupby("lot_size_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert By the LOT size \n{avg_lot_size}")

fig15=go.Figure()
fig15.add_trace(go.Bar(
    x=avg_lot_size.index,y=avg_lot_size.values,marker_color=['#ff0000', '#00ff00',"#00f7ff"],marker_line_color="black",marker_line_width=1.5,text=avg_lot_size.values,textposition="outside"
))
fig15.update_layout(
    title="Average Selling Price: By lot size",xaxis_title="lot size Category",yaxis_title="Average Selling Pric",template="plotly_white"
)
st.plotly_chart(fig15,use_container_width=True)

# bar chart 
# plt.bar(avg_lot_size.index,avg_lot_size.values,color=["blue","skyblue","gray"],edgecolor="black")
# for i,val in enumerate(avg_lot_size.values):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price: By lot size")
# plt.xlabel("lot size Category")
# plt.ylabel("Average Selling Price")
# # plt.show()


# garage_spaces
df['garage_spaces_category']=df["garage_spaces"].apply(lambda x:"Small House" if x==0 else "Medium House" if x==1 else "Big House" if x>=3 else "Outclass")
print(df[["garage_spaces","garage_spaces_category"]])

# average price for lot size
avg_garage_spaces=df.groupby("garage_spaces_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert By the LOT size \n{avg_garage_spaces}")

# Calculate average selling price for properties with pool and without pool
small_avg = df[df["garage_spaces"] == 0]["selling_price"].mean()
medium_avg = df[df["garage_spaces"] == 1]["selling_price"].mean()
big_avg = df[df["garage_spaces"] >= 3]["selling_price"].mean()

print(f"Average price for Small House: {small_avg:.2f}")
print(f"Average price for Medium House: {medium_avg:.2f}")
print(f"Average price for Big House: {big_avg:.2f}")

# Percentage difference compared to Small House
medium_diff = ((medium_avg - small_avg) / small_avg) * 100
big_diff = ((big_avg - small_avg) / small_avg) * 100

print(f"Properties with Medium Garage are {medium_diff:.2f}% more expensive than Small Garage on average.")
print(f"Properties with Big Garage are {big_diff:.2f}% more expensive than Small Garage on average.")


# # # bar chart 
# plt.bar(avg_garage_spaces.index,avg_garage_spaces.values,color=["blue","skyblue","gray"],edgecolor="black")
# for i,val in enumerate(avg_garage_spaces.values):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price: By garage spaces")
# plt.xlabel("garage spaces Category")
# plt.ylabel("Average Selling Price")
# # plt.show()


# pool
df["pool_category"]=df["pool"].apply(lambda x:"HAS POOL"if x=="TRUE" else "NO POOL")
avg_pool=df.groupby("pool_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with POOL AND without POOL \n{avg_pool}")

# Calculate average selling price for properties with pool and without pool
pool_avg = df[df["pool"] == True]["selling_price"].mean()
no_pool_avg = df[df["pool"] == False]["selling_price"].mean()
# Calculate percentage difference
difference = ((pool_avg - no_pool_avg) / no_pool_avg) * 100
print(f"Properties with a pool are {difference:.2f}% more expensive on average.")
# bar chart 
fig17=go.Figure()
fig17.add_trace(go.Bar(
    x=avg_pool.index,y=avg_pool.values,marker_color=["#2cd4c6", "#0e37ed"],
    marker_line_color="black",marker_line_width=1.5,
    text=avg_pool.values,textposition="outside"
))
fig17.update_layout(
    title="Average Selling Price by Pool",
    xaxis_title="Pool Category",yaxis_title="Average Selling Pric",
    template="plotly_white"
)
st.plotly_chart(fig17,use_container_width=True)



# plt.bar(avg_pool.index,avg_pool.values,color=["blue","skyblue"],edgecolor="black")
# for i,val in enumerate(avg_pool.values):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title(f"Average Selling Price by Pool (Difference: {difference:.2f}%)")
# plt.xlabel("Pool Category")
# plt.ylabel("Average Selling Price")
# plt.show()

# fireplace 
df["fireplace_category"]=df["fireplace"].apply(lambda x:"Has fireplace"if x else "No fireplace")
avg_fireplace=df.groupby("fireplace_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Fireplace and withour Fireplace \n{avg_fireplace}")

fig18=go.Figure()
fig18.add_trace(go.Bar(
    x=avg_fireplace.index,y=avg_fireplace.values,marker_color=["#2cd4c6", "#0e37ed"],
    marker_line_color="black",marker_line_width=1.5,
    text=avg_fireplace.index,textposition="outside"
))
fig18.update_layout(
    title="Average Selling Price:  By fireplace",
    xaxis_title="fireplace Category",
    yaxis_title="Average Selling Price",template="plotly_white"
)
st.plotly_chart(fig18,use_container_width=True)



# plt.bar(avg_fireplace.index,avg_fireplace.values,color=['skyblue',"blue"],edgecolor="black")
# for i,val in enumerate(avg_fireplace):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By fireplace")
# plt.xlabel("fireplace Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# view
df["view_category"]=df["view"].apply(lambda x:"Ocean" if x=="ocean" else "City" if x=="city" else "Mountain" if x== "mountain" else "other")
avg_view=df.groupby("view_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with VIEW \n{avg_view}")

fig19=go.Figure()
fig19.add_trace(go.Bar(
    x=avg_view.index,y=avg_view.values,marker_color=["#2cd4c6", "#0e37ed","#10ebd8"],
    marker_line_color="black",marker_line_width=1.5,
    text=avg_view.index,textposition="outside"
))
fig19.update_layout(
    title="Average Selling Price:  By VIEW",xaxis_title="VIEW Category",
    yaxis_title="Average Selling Price",template="plotly_white"
)
st.plotly_chart(fig19,use_container_width=True)


# plt.bar(avg_view.index,avg_view.values,color=["blue","skyblue"],edgecolor="black")
# for i,val in enumerate(avg_view):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By VIEW")
# plt.xlabel("VIEW Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# distance_to_hospital

df["distance_to_hospital_category"]=df["distance_to_hospital"].apply(lambda x: "Near" if x<=6 else "Far")
print(df[["distance_to_hospital","distance_to_hospital_category"]])
avg_distance_to_hospital=df.groupby("distance_to_hospital_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Hospital near or far \n{avg_distance_to_hospital}")

fig20=go.Figure()
fig20.add_trace(go.Bar(
    x=avg_distance_to_hospital.index,y=avg_distance_to_hospital.values,
    marker_color=["#2cd4c6", "#0e37ed"],marker_line_color="black",
    marker_line_width=1.5,text=avg_distance_to_hospital.index,textposition="outside"
))
fig20.update_layout(
    title="Average Selling Price:  By Hospital distance Near or Far",
    xaxis_title="Hospital Category",yaxis_title="Average Selling Price"
)
st.plotly_chart(fig20,use_container_width=True)


# plt.bar(avg_distance_to_hospital.index,avg_distance_to_hospital.values,color=["blue","skyblue"],edgecolor="black")
# for i,val in enumerate(avg_distance_to_hospital):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Hospital distance Near or Far")
# plt.xlabel("Hospital Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# distance_to_grocery_store
df["distance_to_grocery_store_category"]=df["distance_to_grocery_store"].apply(lambda x: "Near" if x<=3.5 else "Far")
print(df[["distance_to_grocery_store","distance_to_grocery_store_category"]])
avg_distance_to_grocery_store=df.groupby("distance_to_grocery_store_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Grocery store near or far \n{avg_distance_to_grocery_store}")

fig21=go.Figure()
fig21.add_trace(go.Bar(
    x=avg_distance_to_grocery_store.index,y=avg_distance_to_grocery_store.values,
    marker_color=["#2cd4c6", "#0e37ed"],marker_line_color="black",marker_line_width=1.5
    ,text=avg_distance_to_grocery_store.index,textposition="outside"
))
fig21.update_layout(
    title="Average Selling Price:  By Grocery Store Near or Far",xaxis_title="Grocery Store Category"
    ,yaxis_title="Average Selling Price",
    template="plotly_white"
)
st.plotly_chart(fig21,use_container_width=True)


# plt.bar(avg_distance_to_grocery_store.index,avg_distance_to_grocery_store.values,color=["blue","skyblue"],edgecolor="black")
# for i,val in enumerate(avg_distance_to_grocery_store):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Grocery Store Near or Far")
# plt.xlabel("Grocery Store Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# crime_rate
df["crime_rate_category"]=df["crime_rate"].apply(lambda x: "good" if x <= 1.5 else "fair" if x<=5 else "very poor" if x>10 else "poor")
print(df[["crime_rate","crime_rate_category"]])
avg_crime_rate=df.groupby("crime_rate_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Crime Rate Category  \n{avg_crime_rate}")

fig22=go.Figure()
fig22.add_trace(go.Bar(
    x=avg_crime_rate.index,y=avg_crime_rate.values,marker_color=["#2cd4c6", "#0e37ed","#10ebd8"],
    marker_line_color="black",marker_line_width=1.5,text=avg_crime_rate.index,
    textposition="outside"
))
fig22.update_layout(title="Average Selling Price:  By CRIME RATE",
                    xaxis_title="CRIME RATE Category",yaxis_title="Average Selling Price"
                    )

st.plotly_chart(fig22,use_container_width=True)
# plt.bar(avg_crime_rate.index,avg_crime_rate.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_crime_rate):
#     plt.text(i,val ,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By CRIME RATE")
# plt.xlabel("CRIME RATE Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# heating_type
df["heating_type_category"]=df["heating_type"].apply(lambda x: "Gas" if x== "gas" else "Oil" if x== "oil" else "Electric" if x=="electric" else "other")
avg_heating_type=df.groupby("heating_type_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Heating type  \n{avg_heating_type}")

fig23=go.Figure()
fig23.add_trace(go.Bar(
    x=avg_heating_type.index,y=avg_heating_type.values,marker_color=["#2cd4c6", "#0e37ed"],
    marker_line_color="black",
    marker_line_width=1.5,text=avg_heating_type.index,textposition="outside"
))
fig23.update_layout(
    title="Average Selling Price:  By Heating Type",
    yaxis_title="Average Selling Price",
    xaxis_title="Heating Type Categor",template="plotly_white"
)
st.plotly_chart(fig23,use_container_width=True)
# plt.bar(avg_heating_type.index,avg_heating_type.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_heating_type):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Heating Type")
# plt.xlabel("Heating Type Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# cooling_type
df["cooling_type_category"]=df["cooling_type"].apply(lambda x: "None" if x=="none" else "Central" if x=="central" else "Window" if x=="window" else "other")
avg_cooling_type=df.groupby("cooling_type_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with cooling type  \n{avg_cooling_type}")
fig24=go.Figure()
fig24.add_trace(go.Bar(
    x=avg_cooling_type.index,y=avg_cooling_type.values,marker_color=["#2cd4c6", "#0e37ed","#10ebd8"],
    marker_line_color="black",
    marker_line_width=1.5,text=avg_cooling_type.index,textposition="outside"
))
fig24.update_layout(
    title="Average Selling Price:  By Cooling Type",
    xaxis_title="Cooling Type Category",
    yaxis_title="Average Selling Price",
    template="plotly_white"
)
st.plotly_chart(fig24,use_container_width=True)



# plt.bar(avg_cooling_type.index,avg_cooling_type.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_cooling_type):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Cooling Type")
# plt.xlabel("Cooling Type Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# foundation_type
df["foundation_type_category"]=df["foundation_type"].apply(lambda x: "Slab" if x=="slab" else "Basement" if x=="basement" else "Crawl space" if x=="crawl space" else "other")
avg_foundation_type=df.groupby("foundation_type_category")["selling_price"].mean().round(2)
print(f"\nThe average price of the propert with Foundation type  \n{avg_foundation_type}")

fig25=go.Figure()
fig25.add_trace(go.Bar(
    x=avg_foundation_type.index,y=avg_foundation_type.values,marker_color=["#2cd4c6", "#0e37ed","#10ebd8"],
    marker_line_color="black",marker_line_width=1.5,text=avg_foundation_type.index,textposition="outside"
))
fig25.update_layout(
    title="Average Selling Price:  By Foundation Type",xaxis_title="Foundation Type Categor",
    yaxis_title="Average Selling Price",template="plotly_white"
)

st.plotly_chart(fig25,use_container_width=True)


# plt.bar(avg_foundation_type.index,avg_foundation_type.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_foundation_type):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Foundation Type")
# plt.xlabel("Foundation Type Category")
# plt.ylabel("Average Selling Price")
# # plt.show()


# roof_material
df["roof_material_category"]=df["roof_material"].apply(lambda x: "Metal" if x=="metal" else "Tile" if x=="tile" else "Asphalt" if x=="asphalt" else "other")
avg_roof_material=df.groupby("roof_material")["selling_price"].mean().round(2)
print(avg_roof_material)


# plt.bar(avg_roof_material.index,avg_roof_material.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_roof_material):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Roof material")
# plt.xlabel("Roof Material Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# # energy_efficiency_rating

# df["energy_efficiency_rating_category"]=df["energy_efficiency_rating"].apply(lambda x: "Good" if x<=3 else "Fair" if x<=6 else "Poor" if x>=7 else "very poor")
# print(df[["energy_efficiency_rating","energy_efficiency_rating_category"]])

# avg_energy_efficiency_rating=df.groupby("energy_efficiency_rating_category")["selling_price"].mean().round(2)
# print(avg_energy_efficiency_rating)
# plt.bar(avg_energy_efficiency_rating.index,avg_energy_efficiency_rating.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_energy_efficiency_rating):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Energy Efficiency Rating")
# plt.xlabel("Energy Efficiency Rating Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# # property_tax
# df["property_tax_category"]=df["property_tax"].apply(lambda x: "Low" if x<=1800 else "Medium" if x<=2700 else "High" if x<=3500 else "Very High")
# print(df[["property_tax","property_tax_category"]])

# avg_property_tax=df.groupby("property_tax_category")["selling_price"].mean().round(2)
# print(avg_property_tax)

# plt.bar(avg_property_tax.index,avg_property_tax.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_property_tax):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Property Tax")
# plt.xlabel("Property Tax Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

# # hoa_fee
# df["hoa_fee_category"]=df["hoa_fee"].apply(lambda x: "Low" if x<=150 else "Medium" if x<=210 else "High" if x<=380 else "Very High")
# print(df[["hoa_fee","hoa_fee_category"]])

# avg_hoa_fee=df.groupby("hoa_fee_category")["selling_price"].mean().round(2)
# print(avg_hoa_fee)

# plt.bar(avg_hoa_fee.index,avg_hoa_fee.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_hoa_fee):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Hoa Fee")
# plt.xlabel("Hoa Fee Category")
# plt.ylabel("Average Selling Price")
# # plt.show()


# median_income
df["median_income_category"]=df["median_income"].apply(lambda x: "Low" if x<=50000 else "Medium" if x<=95000 else "High" if x<=120000 else "Very High")
print(df[["median_income","median_income_category"]])

avg_median_income=df.groupby("median_income_category")["selling_price"].mean().round(2)
print(avg_median_income)

fig16=go.Figure()
fig16.add_trace(go.Bar(
    x=avg_median_income.index,y=avg_median_income.values,marker_color=["#00ffea", "#002fff","#3eff18", "#b9c420"],
    marker_line_color="black",marker_line_width=1.5,text=avg_median_income.values,textposition="outside"
))
fig16.update_layout(
    title="Average Selling Price:  By Median Income",xaxis_title="Median Income Category",yaxis_title="Average Selling Price",template="plotly_white"
)
st.plotly_chart(fig16,use_container_width=True)

# plt.bar(avg_median_income.index,avg_median_income.values,color=["skyblue","blue"],edgecolor="black")
# for i,val in enumerate(avg_hoa_fee):
#     plt.text(i,val,f"{val:.0f}",ha="center",va="bottom",fontsize=10)
# plt.title("Average Selling Price:  By Median Income")
# plt.xlabel("Median Income Category")
# plt.ylabel("Average Selling Price")
# # plt.show()

