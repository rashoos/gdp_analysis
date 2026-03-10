import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
df = pd.read_csv(url)

countries = ["India", "China", "United States", "Pakistan", "Bangladesh", "Brazi", "Russian Federation", "South Africa"]


plt.figure(figsize=(12,6))

for country in countries:
    country_data = df[df["Country Name"]==country]
    country_data = country_data[country_data["Year"]>2000]
    plt.plot(country_data["Year"],
             country_data["Value"],
             label=country)

plt.title("GDP Comparison - India vs China vs United States (2000 - Present)")
plt.xlabel("Year")
plt.ylabel("GDP(USD)")
plt.legend()
plt.grid(True)
plt.show()

for country in ["India","China","United States", "Brazil", "Russian Federation", "South Africa"]:
    data = df[df["Country Name"]==country]
    data = data[data["Year"]>2000]
    start = data["Value"].iloc[0]
    end = data["Value"].iloc[-1]
    growth = ((end - start)/start)*100
    print(f"{country}:{growth:.1f}% growth since 2000")