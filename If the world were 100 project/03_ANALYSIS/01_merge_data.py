import pandas as pd

#Pandas to access and read all our cleaned data
population = pd.read_csv("../02_CLEAN_DATA/population_clean.csv")
internet = pd.read_csv("../02_CLEAN_DATA/internet_clean.csv")
electricity = pd.read_csv("../02_CLEAN_DATA/Electricity_clean.csv")
urban_population = pd.read_csv("../02_CLEAN_DATA/Urban_Population_clean.csv")
age_0_14 = pd.read_csv("../02_CLEAN_DATA/Age_0_14_clean.csv")
age_15_64 = pd.read_csv("../02_CLEAN_DATA/Age_15_64_clean.csv")
age_65_plus = pd.read_csv("../02_CLEAN_DATA/Age_65_Plus_clean.csv")
life_expectancy = pd.read_csv("../02_CLEAN_DATA/Life_Expectancy_clean.csv")
fertility_rate = pd.read_csv("../02_CLEAN_DATA/Fertility_Rate_clean.csv")


#Merge all cleaned data into one Dataframe
merged_data = pd.merge(population, internet,
                       on=["Country Name", "Country Code", "Year"],
                       how="left")

merged_data_2 = pd.merge(merged_data, electricity,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_3 = pd.merge(merged_data_2,urban_population,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_4 = pd.merge(merged_data_3, age_0_14,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_5 = pd.merge(merged_data_4, age_15_64,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_6 = pd.merge(merged_data_5, age_65_plus,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_7 = pd.merge(merged_data_6, life_expectancy,
                on=["Country Name", "Country Code", "Year"],
                how="left")

merged_data_8 = pd.merge(merged_data_7, fertility_rate,
                on=["Country Name", "Country Code", "Year"],
                how="left")

#Data quality check on merged data
print(
    merged_data_8.groupby("Year")[
        ["Internet", "Electricity", "Life_Expectancy", "Fertility_Rate"]
    ].apply(lambda x: x.isna().sum())
)

missing_internet_2024 = merged_data_8[
    (merged_data_8["Year"] == 2024) &
    (merged_data_8["Internet"].isna())
]
print(missing_internet_2024[["Country Name", "Population"]])
missing_population = missing_internet_2024["Population"].sum()
print(missing_population)

total_population = merged_data_8[
    merged_data_8["Year"] == 2024
]["Population"].sum()
print(total_population)

missing_percentage = (missing_population / total_population) * 100
print(missing_percentage)

####Save the Dataframe in a csv file####
merged_data_8.to_csv("../03_ANALYSIS/merged_data.csv", index=False)