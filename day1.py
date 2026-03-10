import pandas as pd

data = {
    "Country": ["India", "USA","China","UK","Germany"],
    "gdp_trillion":[3.5, 25.4, 17.9, 3.1, 4.2],
    "inflation_pct":[5.1, 3.2, 2.1, 6.7, 5.9],
    "unemployment_pct":[7.8, 3.7, 5.2, 4.2, 3.0]
}
df = pd.DataFrame(data)
print(df)

sorted_df = df.sort_values("gdp_trillion",ascending=False)
print(sorted_df)

high_inflation = df[df["inflation_pct"]>5]
print(high_inflation)

df["is_developed"] =["No","Yes","No","Yes","Yes"]
print(df)
