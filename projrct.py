import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("DATA.csv")
print(df.head(5))

print(df.describe())

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

plt.figure(figsize=(10,6))
plt.bar(category,values,color="skyblue",edgecolor="black")
plt.title("Number of Unique Categories in Property Dataset", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Unique Values Count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()
print("\n")

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
# pie chart of price
plt.figure(figsize=(10,6))
plt.pie(values,labels=chart,autopct="%1.1f%%",startangle=90)
plt.title("COST")
plt.axis("equal")
plt.tight_layout()
plt.show()



# renovation_year which is held before the 2000
renovation_y=df[df["renovation_year"]<2000].shape[0]
print(f"\nNumbers of properties renovate before 2000 ::{renovation_y}")

renovation_ye=df[df["renovation_year"]>2000].shape[0]
print(f"\nNumbers of properties renovate after 2000 ::{renovation_ye}")

chart=["Renovation Before 2000","Renovation After 2000"]
values=[renovation_y,renovation_ye]

# pie chart 
plt.pie(values,labels=chart,autopct="%1.1f%%",startangle=90)
plt.title("CHART SHOWS RENOVATION YEARS")
plt.axis("equal")
plt.tight_layout()
plt.show()

# Property Type vs Price

property_type1=df.groupby("property_type")["selling_price"].sum()
print("\n",property_type1)

# bar chart show the each property type by the selling price 
plt.figure(figsize=(12,6))
plt.bar(property_type1.index,property_type1.values,color="red",edgecolor="black")
plt.tight_layout()
plt.xlabel("category")
plt.ylabel("Price")
plt.title("Chart show the each category total selling price ")
plt.xticks(rotation=45)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()

# bedrooms wise total price 

bedrooms=df.groupby("bedrooms")["selling_price"].sum()
print("\n",bedrooms)

# give the each graph different color 

unique_bedroom=df["bedrooms"].unique()

if len(unique_bedroom)<=10:
    palette=sns.color_palette("tab10",len(unique_bedroom))
elif len(unique_bedroom)<=20:
    palette=sns.color_palette("tab20",len(unique_bedroom))
else:
    palette=sns.color_palette("husl",len(unique_bedroom))

bedroom_color_map={bedrooms: palette[i % len(unique_bedroom)]for i,bedrooms  in enumerate(unique_bedroom)}

colors=[bedroom_color_map[bedrooms] for bedrooms in df["bedrooms"]]

# chart show the bedrooms per price 
plt.figure(figsize=(12,6))
plt.bar(bedrooms.index,bedrooms.values,color=colors,edgecolor="black")
plt.axhline(df["bedrooms"].mean(),linestyle="--",linewidth=2,color="black",label="average")
plt.title("PER BEDROOM TOTAL PRICE")
plt.xlabel("BEDROOM")
plt.ylabel("PRICE")
plt.tight_layout()
plt.grid(True,linestyle="--",alpha=0.5)
plt.xticks(rotation=45)
plt.legend()
plt.show()

# pool wise price
pool=df.groupby("pool")["selling_price"].sum()

# bar chart show the pool wise price 
plt.bar(pool.index,pool.values,color=colors)
plt.title("CHART SHOW THE PRICE OF POOL WITH OR WITHOUT ")
plt.xlabel("POOL")
plt.ylabel("Price")
plt.grid(True,alpha=0.5,linestyle="--")
plt.tight_layout()
plt.show()

# fireplace wise price
fireplace=df.groupby("fireplace")["selling_price"].sum()

# chart show the price of fireplace with or without 
plt.figure(figsize=(12,6))
plt.bar(fireplace.index,fireplace.values,color=colors,edgecolor="black")
plt.title("CHART SHOW THE PRICE OF fireplace WITH OR WITHOUT ")
plt.xlabel("Fireplace")
plt.ylabel("Price")
plt.grid(True,alpha=0.5,linestyle="--")
plt.tight_layout()
plt.show()

# view wise price
view=df.groupby("view")["selling_price"].sum()

# chart show the view wise price 
plt.figure(figsize=(12,6))
plt.bar(view.index,view.values,color=colors,edgecolor="black")
plt.title("CHART SHOW THE PRICE OF view wise price")
plt.xlabel("view")
plt.ylabel("Price")
plt.grid(True,alpha=0.5,linestyle="--")
plt.tight_layout()
plt.show()

# garage_spaces wise price 
garage_spaces1=df.groupby("garage_spaces")["selling_price"].sum()

# bar chart show the garage_spaces

plt.figure(figsize=(12,8))
plt.bar(garage_spaces1.index,garage_spaces1.values,color=colors,edgecolor="black")
plt.xlabel("Garage Spaces")
plt.ylabel("price")
plt.title("group by chart show the garage_spaces")
plt.grid(True,alpha=0.5,linestyle="--")
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()



# sales trend over time 
df["selling_date"]=pd.to_datetime(df["selling_date"])
sales_trend=df.groupby("selling_date")["selling_price"].sum()
plt.figure(figsize=(14, 8))
plt.plot(sales_trend.index,sales_trend.values,color="blue",marker="o")
plt.grid(True,alpha=0.5,linestyle="--")
plt.title("sale trend over time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.show()


