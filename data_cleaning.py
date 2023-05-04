import pandas as pd

# Data import: birth_rate, gdp by country, happiness_index and others,
# unemployment_rate

df_birth_rate = pd.read_csv("birth_rate.csv")
df_gdp = pd.read_csv("GDP.csv")
df_happiness_index = pd.read_excel("DataForFigure2.1WHR2023.xls")
df_unemployment_rate = pd.read_excel("imf-dm-export-20230502.xls")

# Preliminary variable selection and main data frame creation
# Ensuring all countries are available for joint
