# global_birth_rate_analysis

## Overview

An analysis on the effects of the following factors on birth rate:

- Economy: GDP per Capita, inflation
- Social: Happiness index, Social support score, life expectancy, freedom to make life choices, generosity,perception of corruption
- Jobs: Unemployment rate

Noted that interaction terms were considered for all variables in the original model. A variable selection process was conducted based on p-value, and incorporate only 6 variables in the interaction terms model due to the limited observations of the training set of (130 observations). This aims at limiting overfitting the model as well as ensuring the predictor to observations ratios of 1:15.

## Analysis

Please refer to birth_rate_analysis.ipynb for the analysis.

## Conclusion

With multiple linear regression without interaction terms, the following predictors have significant impacts on the response variable (birth rate):

- Happiness index
- Unemployment
- Inflation

Noted that the increase in social support and healthy life expectancy increase the birth rates. The 4 predictors in the model were able to explain 49.45% of the model variations in the test set.

Through the incorporation of the interaction terms and variable selection, the following variables show significant impacts on the response variable (birth rate):

- Happiness index
- GDP
- Unemployment rate
- Interaction term between GDP and happiness index

Noted that the r_squared score, which represents how well these predictors were able to explain the model variations, increases to 57.50% in the test set with interaction term in comparison to 49.45%. In addition, the interaction term model showed a decrease in the RSE (residuals squared errors), represented the errors not explained by the model, to RSE 7.63 in the test set from RSE 8.17 in the test set from the original model.

Further noted that the happiness index also includes insights from variables like: Freedom to make life choices, Healthy life expectancy, Perceptions of corruptions, and generosity. Due to high collinearity between these variables, only happiness index was included as predictor.

## Data Sources references

The following datasets were used for the analysis:

1. Birth rate by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/birth-rate-by-country

2. GDP ranked by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/countries/by-gdp

3. World Happiness Report 2023. Data for Figure 2.1. Sustainable Development Solutions Network. Retrieved via the following link: https://worldhappiness.report/ed/2023/#appendices-and-data

4. The Global Database of Inflation, updated to 2022. Headline Consumer price inflation, annual, The World Bank. Retrieved via the following link: https://www.worldbank.org/en/research/brief/inflation-database

5. Unemployment by Country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/unemployment-by-country
