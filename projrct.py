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

category=["property_type","neighborhood_types","views_types","heating_type","cooling_type","foundation_type","roof_material"]

values=[property_type,neighborhood_types,views_types,heating_type,cooling_type,foundation_type,roof_material]

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

chart=["Renovation year before 2000","Renovation Year after 2000"]
values=[renovation_y,renovation_ye]

# pie chart 
plt.pie(values,labels=chart,autopct="%1.1f%%",startangle=90)
plt.title("CHART SHOWS RENOVATION YEARS")
plt.axis("equal")
plt.tight_layout()
plt.show()


