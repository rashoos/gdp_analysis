"""
GDP Growth Analysis Tool
Author: Muhammad Rashad TP
Description: Analyzes real world GDP data to find
             the fastest growing economies
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
df = pd.read_csv(url)

# Config
START = 2000
END = 2015
TOP_N = 10

# Clean Data
exclude = ["World", "income", "OECD", "dividend", "IDA",
           "IBRD", "middle", "Middle", "Low", "High",
           "East", "North", "South", "Europe", "Asia",
           "Africa", "America", "Pacific", "Caribbean",
           "fragile", "Fragile", "Euro", "Arab", "Latin"]

start_year = df[df["Year"]== START]
end_year = df[df["Year"]== END]
mask = ~start_year["Country Name"].str.contains("|".join(exclude),na=False)
start_year = start_year[mask]
countries = start_year["Country Name"].tolist()

# Growth Calculation
results =[]
for country in countries:
    try:
        start = start_year[start_year["Country Name"]==country]["Value"].iloc[0]
        end = end_year[end_year["Country Name"]==country]["Value"].iloc[0]
        growth = ((end-start)/start)*100
        results.append({"country":country, "growth":growth})
    except:
        pass
results_df = pd.DataFrame(results)

# Top
all_ranked = results_df.sort_values("growth", ascending=False)
top = all_ranked.head(TOP_N)
top = top.reset_index(drop=True)
top.index.name = "Rank"
top.index = top.index+1
print(f"\nTOP {TOP_N} Fastest Growing Economies ({START}-{END})")
print(top)

# India Rank
all_ranked = all_ranked.reset_index(drop=True)
all_ranked.index = all_ranked.index+1
india = all_ranked[all_ranked["country"]=="India"]
print(f"\n India's Rank is #{india.index[0]} with {india['growth'].values[0]:.1f}% growth")

colors = ["crimson" if c == "India" else "steelblue" for c in top["country"]]
plt.figure(figsize = (12,6))
plt.bar(top["country"],top["growth"],color = colors)
plt.title(f"Top {TOP_N} Growing Economies ({START}-{END})")
plt.xlabel("Country")
plt.ylabel("Growth %")
plt.xticks(rotation = 45,ha = "right")
plt.savefig("gdp_growth.png")
plt.tight_layout()
plt.show()
print("\nChart Saved as gdp_growth.png")

