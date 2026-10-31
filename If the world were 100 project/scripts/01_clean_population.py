import pandas as pd

file_path = "../01_RAW_DATA/Population/API_SP.POP.TOTL_DS2_en_csv_v2_416239.csv"
population = pd.read_csv(file_path, skiprows=4)
population = population.drop(columns=["Unnamed: 70"])


metadata_path = "../01_RAW_DATA/Population/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_416239.csv"
countries = pd.read_csv(metadata_path)
real_countries = countries[countries["Region"].notna()]
valid_codes = real_countries["Country Code"]
population = population[population["Country Code"].isin(valid_codes)]
population = population.reset_index(drop=True)


year_columns = [str(year) for year in range(1990, 2026)]
population = population[["Country Name", "Country Code"] + year_columns]
population = population.melt(
    id_vars=["Country Name", "Country Code"],
    var_name="Year",
    value_name="Population"
)
population["Year"] = population["Year"].astype(int)
population.to_csv("../02_CLEAN_DATA/population_clean.csv", index=False)