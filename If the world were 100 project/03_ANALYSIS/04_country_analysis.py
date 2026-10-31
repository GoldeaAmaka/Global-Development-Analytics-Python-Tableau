import pandas as pd

# Load the merged dataset containing individual countries
country_data = pd.read_csv("merged_data.csv")

# Keep the country information and indicators needed for Tableau
columns = [
    "Country Name",
    "Country Code",
    "Year",
    "Population",
    "Internet",
    "Electricity",
    "Urban_Population",
    "Age_0_14",
    "Age_15_64",
    "Age_65_Plus",
    "Life_Expectancy",
    "Fertility_Rate"
]

country_data = country_data[columns].copy()

# Sort the data by country and year
country_data = country_data.sort_values(
    by=["Country Name", "Year"]
).reset_index(drop=True)

# Save the country-level dataset for Tableau
country_data.to_csv(
    "../04_TABLEAU/world_100_countries.csv",
    index=False
)

# Confirm that the file has been saved
print("Country-level data saved successfully!")
print("Total records:", len(country_data))
print("Total countries:", country_data["Country Code"].nunique())
print(country_data.head())
