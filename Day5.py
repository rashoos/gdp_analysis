import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
df = pd.read_csv(url)

start_year = df[df["Year"]==2010]
end_year = df[df["Year"]==2019]

exclude = ["World", "income", "OECD", "dividend", "IDA",
           "IBRD", "middle", "Middle", "Low", "High",
           "East", "North", "South", "Europe", "Asia",
           "Africa", "America", "Pacific", "Caribbean",
           "fragile", "Fragile", "Euro", "Arab", "Latin"]

mask = ~start_year["Country Name"].str.contains("|".join(exclude),na=False)
start_year = start_year[mask]

countries = start_year["Country Name"].tolist()

results = []
for country in countries:
    try:
        start = start_year[start_year["Country Name"]== country]["Value"].iloc[0]
        end = end_year[end_year["Country Name"]== country]["Value"].iloc[0]
        growth = ((end - start) /start)*100
        results.append({"country":country, "growth":growth})
    except:
        pass
results_df = pd.DataFrame(results)

top10 = results_df.sort_values("growth", ascending=False)
top10 = top10.reset_index(drop=True)
top10.index = top10.index+1
print(top10.head(10))

india = top10[top10["country"]=="India"]
print(india)