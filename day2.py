import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
df = pd.read_csv(url)

print(df.head(100))
print("--------")
print(df.shape)
print("--------")
print(df.columns)

india = df[df["Country Name"] == "India"]
print(india)
india_recent = india[india["Year"]>2000]
print(india_recent)

plt.plot(india_recent["Year"],india_recent["Value"])
plt.title("India GDP Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (USD)")
plt.show()

# Find the years where GDP dropped
india_recent["change"] = india_recent["Value"].diff()
dips = india_recent[india_recent["change"] < 0]
print(dips[["Year", "Value", "change"]])