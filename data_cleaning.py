import pandas as pd

# Data import: birth_rate, gdp by country, happiness_index and others,
# unemployment_rate

df_birth_rate = pd.read_csv("birth_rate.csv")
df_gdp = pd.read_csv("GDP.csv")
df_happiness_index = pd.read_excel("DataForFigure2.1WHR2023.xls")
df_unemployment_rate = pd.read_excel("imf-dm-export-20230502.xls")

# Preliminary variable selection and main data frame creation
# Ensuring all countries are available for joint


def data_frame_check(df):
    print(df.info())
    print(df.head(5))


data_frame_check(df_birth_rate)
data_frame_check(df_gdp)
data_frame_check(df_happiness_index)
data_frame_check(df_unemployment_rate)

country_birth_rate = len(df_birth_rate["country"].unique())

country_gdp = len(df_gdp["country"].unique())

country_happiness_index = len(df_happiness_index["Country name"].unique())

country_unemployment_rate = len(
    df_unemployment_rate["Unemployment rate (Percent)"].unique()
)

print(
    country_birth_rate, country_gdp, country_happiness_index, country_unemployment_rate
)

# Note that the countries lists between the datasets are not the same:
# Require identification of countries in scope for all datasets
