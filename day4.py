import pandas as pd
import matplotlib.pyplot as plt

url =  "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
df = pd.read_csv(url)

latest_year = df["Year"].max()
print("Last year in dataset:", latest_year)

latest = df[df["Year"]==latest_year]

exclude = ["World", "income", "OECD", "dividend", "IDA",
           "IBRD", "middle", "Middle", "Low", "High",
           "East", "North", "South", "Europe", "Asia",
           "Africa", "America", "Pacific", "Caribbean",
           "fragile", "Fragile", "Euro", "Arab", "Latin"]

mask = ~latest["Country Name"].str.contains("|".join(exclude), na=False)
latest_countries = latest[mask]

top10 = latest_countries.sort_values("Value", ascending=False).head(10)

# Make numbers readable
top10["GDP_Trillion"] = top10["Value"] / 1e12

print(top10[["Country Name", "GDP_Trillion"]].to_string(index=False))


colors = [ "crimson" if c == "India"
           else "steelblue"
           for c in top10["Country Name"]]

plt.figure(figsize = (12,6))
plt.bar(top10["Country Name"],
        top10["Value"]/1e12,
        color = colors)

plt.title(f"Top 10 Biggest Economies - India Highlighted")
plt.xlabel("Country")
plt.ylabel("GDP (Trillions USD)")
plt.xticks(rotation = 45, ha ="right")
plt.tight_layout()
plt.show()

all_countries = latest.sort_values("Value",ascending=False)
all_countries = all_countries.reset_index(drop=True)
india_rank = all_countries[all_countries["Country Name"] == "India"].index[0]+1

print(f"India's GDP rank in {latest_year}:#{india_rank}")
print(f"Total countries in dataset: {len(all_countries)}")