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

- Social support
- Healthy life expectancy
- Perceptions of corruptions

Noted that the increase in social support and healthy life expectancy increase the birth rates. The 9 predictors in the model were able to explain 85.39% of the model variations in the test set. Furthermore, the errors (represented by RSE - Residuals squared errors) showed reduction from the train set to the test set.

Through the incorporation of the interaction terms and variable selection, the following variables show significant impacts on the response variable (birth rate):

- Healthy life expectancy
- Social support Healthy life expectancy
- Ladder score Healthy life expectancy
- Ladder score Social support
- Ladder score
- Social support

Noted that an increase in the interaction terms between social support and life expectancy, as well as happiness index (Ladder score) and life expectancy increase the birth rates, whereas each of these factors alone does not. In addition, the r_squared score, which represents how well these predictors were able to explain the model variations, increases to 86.24% in the test set with interaction term in comparison to 85.39%.

## Data Sources references

The following datasets were used for the analysis:

1. Birth rate by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/birth-rate-by-country

2. GDP ranked by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/countries/by-gdp

3. World Happiness Report 2023. Data for Figure 2.1. Sustainable Development Solutions Network. Retrieved via the following link: https://worldhappiness.report/ed/2023/#appendices-and-data

4. The Global Database of Inflation, updated to 2022. Headline Consumer price inflation, annual, The World Bank. Retrieved via the following link: https://www.worldbank.org/en/research/brief/inflation-database

5. Unemployment by Country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/unemployment-by-country
