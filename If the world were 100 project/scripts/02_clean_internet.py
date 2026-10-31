import pandas as pd

file_path = "../01_RAW_DATA/Internet/API_IT.NET.USER.ZS_DS2_en_csv_v2_433461.csv"
internet = pd.read_csv(file_path, skiprows=4)
internet=internet.drop(columns=["Unnamed: 70"])

metadata_path = "../01_RAW_DATA/Internet/Metadata_Country_API_IT.NET.USER.ZS_DS2_en_csv_v2_433461.csv"
countries = pd.read_csv(metadata_path)
real_countries = countries[countries["Region"].notna()]
real_countries = real_countries.drop(columns=["Unnamed: 5"])
valid_codes = real_countries["Country Code"]

internet_countries = internet[internet["Country Code"].isin(valid_codes)]
internet_countries = internet_countries.reset_index(drop=True)
year_columns = [str(year) for year in range(1990, 2026)]
internet_countries = internet_countries[["Country Name","Country Code"] + year_columns]
internet_countries = internet_countries.melt(
    id_vars=["Country Name", "Country Code"],
    var_name="Year",
    value_name="Internet"
)
internet_countries["Year"] = internet_countries["Year"].astype(int)
internet_countries.to_csv("../02_CLEAN_DATA/internet_clean.csv", index=False)