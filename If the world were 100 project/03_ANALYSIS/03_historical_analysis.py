"""
Analyse how the world's population indicators changed from 1990 to 2024.

This script calculates population-weighted global indicators for each year
and prepares the historical results for the Tableau dashboard.
"""

import pandas as pd

# Load the cleaned merged dataset
data = pd.read_csv("merged_data.csv")

# Create an empty list to store the results for each year
historical_results = []

""" Loop through every year from 1990 to 2024 """
for year in range(1990, 2025):
    year_data = data[data["Year"] == year].copy()

    # Calculate the total world population for this year
    total_population = year_data["Population"].sum()
    # Calculate the population aged 0–14 for this year
    total_age_0_14 = (
        year_data["Population"] * (year_data["Age_0_14"] / 100)
    ).sum()
    age_0_14_world_100 = (total_age_0_14 / total_population) * 100


    """ Calculate the population aged 15–64 for this year """
    total_age_15_64 = (
            year_data["Population"] * (year_data["Age_15_64"] / 100)
    ).sum()
    # Calculate how many people out of 100 are aged 15–64
    age_15_64_world_100 = (total_age_15_64 / total_population) * 100


    """"" Calculate the population aged 65+ for this year """""
    total_age_65_plus = (
        year_data["Population"] * (year_data["Age_65_Plus"] / 100)
    ).sum()
    # Calculate how many people out of 100 are aged 65+
    age_65_plus_world_100 = (total_age_65_plus / total_population) * 100


    """"" ---------------- INTERNET ACCESS ---------------- """""

    # Keep only countries with available Internet data
    internet_data = year_data[year_data["Internet"].notna()].copy()

    # Calculate the total number of Internet users
    total_internet_users = (
        internet_data["Population"] * (internet_data["Internet"] / 100)
    ).sum()

    # Calculate the population covered by available Internet data
    internet_population = internet_data["Population"].sum()

    # Calculate Internet users out of 100 people
    internet_world_100 = (
        total_internet_users / internet_population * 100
        if internet_population > 0 else float("nan")
    )

    """"" ---------------- ELECTRICITY ACCESS ---------------- """""

    # Keep only countries with available electricity data
    electricity_data = year_data[year_data["Electricity"].notna()].copy()

    # Calculate the total number of people with electricity access
    total_electricity_users = (
            electricity_data["Population"] * (electricity_data["Electricity"] / 100)
    ).sum()

    # Calculate the population covered by available electricity data
    electricity_population = electricity_data["Population"].sum()

    # Calculate how many people out of 100 have electricity access
    electricity_world_100 = (
        total_electricity_users / electricity_population * 100
        if electricity_population > 0 else float("nan")
    )

    """"" ---------------- URBAN POPULATION ---------------- """""

    # Calculate the total number of people living in urban areas
    total_urban_population = (
            year_data["Population"] * (year_data["Urban_Population"] / 100)
    ).sum()

    # Calculate how many people out of 100 live in urban areas
    urban_world_100 = (
        total_urban_population / total_population * 100
        if total_population > 0 else float("nan")
    )

    # ---------------- LIFE EXPECTANCY ----------------

    # Keep countries with available life expectancy data
    life_data = year_data[year_data["Life_Expectancy"].notna()].copy()

    # Calculate the population-weighted life expectancy
    life_population = life_data["Population"].sum()

    global_life_expectancy = (
        (life_data["Population"] * life_data["Life_Expectancy"]).sum()
        / life_population
        if life_population > 0 else float("nan")
    )

    """"" ---------------- FERTILITY RATE ---------------- """""

    # Keep countries with available fertility data
    fertility_data = year_data[year_data["Fertility_Rate"].notna()].copy()

    # Calculate the population-weighted fertility rate
    fertility_population = fertility_data["Population"].sum()

    global_fertility_rate = (
        (fertility_data["Population"] * fertility_data["Fertility_Rate"]).sum()
        / fertility_population
        if fertility_population > 0 else float("nan")
    )


    # Store the calculated results for each year
    historical_results.append({
        "Year": year,
        "Population": total_population,
        "Age_0_14": age_0_14_world_100,
        "Age_15_64": age_15_64_world_100,
        "Age_65_Plus": age_65_plus_world_100,
        "Internet": internet_world_100,
        "Electricity": electricity_world_100,
        "Urban_Population": urban_world_100,
        "Life_Expectancy": global_life_expectancy,
        "Fertility_Rate": global_fertility_rate
    })

# Convert the historical results into a DataFrame and Save the historical results for Tableau
historical_df = pd.DataFrame(historical_results)
historical_df.to_csv("../04_TABLEAU/world_100_historical.csv", index=False)
print("Historical data saved successfully!")

