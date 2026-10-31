import pandas as pd

def clean_world_bank_data(folder_name, data_file):

    file_path = f"../01_RAW_DATA/{folder_name}/{data_file}"
    data = pd.read_csv(file_path, skiprows=4)
    data = data.loc[:, ~data.columns.str.startswith("Unnamed")]

    metadata_path = f"../01_RAW_DATA/{folder_name}/Metadata_Country_{data_file}"
    metadata = pd.read_csv(metadata_path)
    real_countries = metadata[metadata["Region"].notna()]
    valid_codes = real_countries["Country Code"]

    open_data = data[data["Country Code"].isin(valid_codes)]
    clean_data = open_data.reset_index(drop=True)
    year_columns = [str(year) for year in range(1990, 2026)]
    final_data = clean_data[["Country Name", "Country Code"] + year_columns]
    long_data = final_data.melt(
        id_vars=["Country Name", "Country Code"],
        var_name="Year",
        value_name=folder_name
    )
    long_data["Year"] = long_data["Year"].astype(int)
    long_data.to_csv(f"../02_CLEAN_DATA/{folder_name}_clean.csv", index=False)


clean_world_bank_data("Age_0_14","API_SP.POP.0014.TO.ZS_DS2_en_csv_v2_434264.csv")
clean_world_bank_data("Age_15_64", "API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_434276.csv")
clean_world_bank_data("Age_65_Plus", "API_SP.POP.65UP.TO.ZS_DS2_en_csv_v2_426759.csv")
clean_world_bank_data("Electricity", "API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_439770.csv")
clean_world_bank_data("Fertility_Rate", "API_SP.DYN.TFRT.IN_DS2_en_csv_v2_439874.csv")
clean_world_bank_data("Life_Expectancy", "API_SP.DYN.LE00.IN_DS2_en_csv_v2_438051.csv")
clean_world_bank_data("Urban_Population", "API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_426580.csv")

