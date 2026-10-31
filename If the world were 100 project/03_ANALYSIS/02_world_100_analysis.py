import pandas as pd


"""
Analyse the 2024 World Bank data for the 'If the World Were 100 People' project.

This script calculates population-weighted global indicators for the World View
and prepares results for the interactive Tableau dashboard.
"""

# -------------------- LOAD DATA --------------------

# Load the cleaned merged dataset
data = pd.read_csv("merged_data.csv")

# Select 2024 data for the main World of 100 analysis
world_data = data[data["Year"] == 2024].copy()


# -------------------- TOTAL WORLD POPULATION --------------------

# Calculate the total population represented in the 2024 dataset
total_population = world_data["Population"].sum()

print("Total world population:", total_population)


# -------------------- AGE 0-14 --------------------

# Calculate the actual number of people aged 0-14 in each country
world_data["Age_0_14_People"] = (
    world_data["Population"] * (world_data["Age_0_14"] / 100)
)

# Add all countries together to get the world total aged 0-14
total_age_0_14 = world_data["Age_0_14_People"].sum()

# Calculate how many people out of 100 would be aged 0-14
age_0_14_world_100 = (total_age_0_14 / total_population) * 100

print("Total people aged 0-14:", total_age_0_14)
print("People aged 0-14 out of 100:", age_0_14_world_100)


# -------------------- AGE 15-64 --------------------

# Calculate the actual number of people aged 15-64 in each country
world_data["Age_15_64_People"] = (
    world_data["Population"] * (world_data["Age_15_64"] / 100)
)

# Add all countries together to get the world total aged 15-64
total_age_15_64 = world_data["Age_15_64_People"].sum()

# Calculate how many people out of 100 would be aged 15-64
age_15_64_world_100 = (total_age_15_64 / total_population) * 100

print("Total people aged 15-64:", total_age_15_64)
print("People aged 15-64 out of 100:", age_15_64_world_100)


# -------------------- AGE 65+ --------------------
# Calculate the actual number of people aged 65+ in each country
world_data["Age_65_Plus_People"] = (
    world_data["Population"] * (world_data["Age_65_Plus"] / 100)
)
# Add all countries together to get the world total aged 65+
total_age_65_plus = world_data["Age_65_Plus_People"].sum()
print("Total people aged 65+:", total_age_65_plus)

# Calculate how many people out of 100 would be aged 65+
age_65_plus_world_100 = (total_age_65_plus / total_population) * 100
print("People aged 65+ out of 100:", age_65_plus_world_100)

# -------------------- AGE GROUP CHECK --------------------

# Check that the three age groups together represent approximately 100 people
age_group_total = age_0_14_world_100 + age_15_64_world_100 + age_65_plus_world_100
print("Total of all age groups out of 100:", age_group_total)



# -------------------- INTERNET ACCESS --------------------

# Keep only countries that have Internet data for 2024
internet_data = world_data[world_data["Internet"].notna()].copy()
# Calculate the actual number of Internet users in each country
internet_data["Internet_People"] = (
    internet_data["Population"] * (internet_data["Internet"] / 100)
)

# Add Internet users from all countries together
total_internet_users = internet_data["Internet_People"].sum()
print("Total Internet users:", total_internet_users)

# Calculate the total population covered by the available Internet data
internet_population = internet_data["Population"].sum()
print("Population covered by Internet data:", internet_population)

# Calculate how many people out of 100 would use the Internet in percentage
internet_world_100 = (total_internet_users / internet_population) * 100
print("Internet users out of 100:", internet_world_100)

# -------------------- ELECTRICITY ACCESS --------------------

# Keep only countries that have Electricity data for 2024
electricity_data = world_data[world_data["Electricity"].notna()].copy()

# Calculate the actual number of people with electricity access in each country
electricity_data["Electricity_People"] = (
    electricity_data["Population"] * (electricity_data["Electricity"] / 100)
)

# Add people with electricity access from all countries together
total_electricity_people = electricity_data["Electricity_People"].sum()

# Calculate the population covered by the available Electricity data
electricity_population = electricity_data["Population"].sum()

# Calculate how many people out of 100 would have electricity access
electricity_world_100 = (total_electricity_people / electricity_population) * 100

print("Total people with electricity access:", total_electricity_people)
print("Population covered by Electricity data:", electricity_population)
print("People with electricity out of 100:", electricity_world_100)


# -------------------- URBAN POPULATION --------------------

# Calculate the actual number of people living in urban areas in each country
world_data["Urban_People"] = (
    world_data["Population"] * (world_data["Urban_Population"] / 100)
)

# Add the urban population from all countries together
total_urban_people = world_data["Urban_People"].sum()

# Calculate how many people out of 100 would live in urban areas
urban_world_100 = (total_urban_people / total_population) * 100

print("Total people living in urban areas:", total_urban_people)
print("People living in urban areas out of 100:", urban_world_100)


# -------------------- LIFE EXPECTANCY --------------------

# Multiply each country's life expectancy by its population
world_data["Life_Expectancy_Weighted"] = (
    world_data["Population"] * world_data["Life_Expectancy"]
)

# Add all population-weighted life expectancy values together
total_life_expectancy_weighted = world_data["Life_Expectancy_Weighted"].sum()

# Calculate the population-weighted global life expectancy
global_life_expectancy = total_life_expectancy_weighted / total_population

print("Population-weighted global life expectancy:", global_life_expectancy)


# -------------------- FERTILITY RATE --------------------

# Multiply each country's fertility rate by its population
world_data["Fertility_Weighted"] = (
    world_data["Population"] * world_data["Fertility_Rate"]
)

# Add all population-weighted fertility values together
total_fertility_weighted = world_data["Fertility_Weighted"].sum()

# Calculate the population-weighted global fertility rate
global_fertility_rate = total_fertility_weighted / total_population

print("Population-weighted global fertility rate:", global_fertility_rate)


# -------------------- CREATE 2024 WORLD VIEW RESULTS --------------------

world_100_results = pd.DataFrame({
    "Indicator": [
        "Age 0-14",
        "Age 15-64",
        "Age 65+",
        "Internet Users",
        "Electricity Access",
        "Urban Population",
        "Life Expectancy",
        "Fertility Rate"
    ],
    "Value": [
        age_0_14_world_100,
        age_15_64_world_100,
        age_65_plus_world_100,
        internet_world_100,
        electricity_world_100,
        urban_world_100,
        global_life_expectancy,
        global_fertility_rate
    ]
})

print(world_100_results)

# Save the 2024 World View results for Tableau
world_100_results.to_csv("../04_TABLEAU/world_100_2024.csv", index=False)