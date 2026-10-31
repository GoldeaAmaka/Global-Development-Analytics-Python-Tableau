import pandas as pd

def clean_world_bank_data(folder_name):
    age_0_14 = pd.read_csv(f"../02_CLEAN_DATA/{folder_name}_clean.csv")
    print("SHAPE:")
    print(age_0_14.shape)

    print("\nMISSING VALUES:")
    print(age_0_14.isna().sum())

    print("\nDUPLICATES:")
    print(age_0_14.duplicated().sum())

    print("\nDUPLICATE COUNTRY-YEARS:")
    print(age_0_14.duplicated(subset=["Country Code", "Year"]).sum())

    print("\nDATA TYPES:")
    print(age_0_14.dtypes)

    print("\nYEAR RANGE:")
    print(age_0_14["Year"].min())
    print(age_0_14["Year"].max())

    print("\nNUMBER OF COUNTRIES:")
    print(age_0_14["Country Code"].nunique())

    print("\nVALUE SUMMARY:")
    print(age_0_14[folder_name].describe())

    print("\nMISSING VALUES BY YEAR:")
    print(age_0_14.groupby("Year")[folder_name].apply(lambda x: x.isna().sum()))


    available_data = age_0_14.dropna(subset=[folder_name])
    print("\nLATEST YEAR WITH DATA:")
    print(available_data["Year"].max())

    print("\n2024 data check:")
    data_2024 = age_0_14[age_0_14["Year"] == 2024]
    print(data_2024[folder_name].notna().sum())

    data_2023 = age_0_14[age_0_14["Year"] == 2023]
    print("2023 data check:")
    print(data_2023[folder_name].notna().sum())



clean_world_bank_data("Age_0_14")
clean_world_bank_data("Age_15_64")
clean_world_bank_data("Age_65_Plus")
clean_world_bank_data("Electricity")
clean_world_bank_data("Fertility_Rate")
clean_world_bank_data("Life_Expectancy")
clean_world_bank_data("Urban_Population")
clean_world_bank_data("Internet")
clean_world_bank_data("Population")



