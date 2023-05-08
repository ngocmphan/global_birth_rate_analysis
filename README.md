# global_birth_rate_analysis

## Overview

An analysis on the effects of the following factors on birth rate:

- Economy: GDP per Capita, inflation
- Social: Happiness index, Social support score, life expectancy, freedom to make life choices, generosity,perception of corruption
- Jobs: Unemployment rate

Due to collinearity, the original model only includes gdpPerCapita, happiness index, inflation, and unemployment rate. In addition, interaction terms were considered for all variables in the original model. A variable selection process was conducted based on p-value, and incorporate only 5 variables in the interaction terms model due to the limited observations of the training set of (130 observations). This aims at limiting overfitting the model as well as ensuring the predictor to observations ratios of 1:15.

## Analysis

Please refer to birth_rate_analysis.ipynb for the analysis.

## Conclusion

With multiple linear regression without interaction terms, out of four predictors, the following predictors have significant impacts on the response variable (birth rate):

- Happiness index
- Unemployment
- Inflation

The 4 predictors in the model were able to explain 52.06% of the model variations in the test set.

Through the incorporation of the interaction terms and variable selection, out of the five predictors, the following variables show significant impacts on the response variable (birth rate):

- Happiness index
- GDP
- Unemployment rate
- Interaction term between GDP and happiness index

(The only predictor that does not have significant impact was the interaction term between GDP and unemployment rate)

Noted that the r_squared score, which represents how well these predictors were able to explain the model variations, increases to 64.00% in the test set with interaction term in comparison to 52.06% for the model without the interaction terms. This indicates that the interaction terms have impacts on the birth rates. In addition, the interaction term model showed a decrease in the RSE (residuals squared errors), represented the errors not explained by the model, to RSE 6.59 in the test set from RSE 7.47 in the test set from the original model.

Noted that happiness index also includes measurements of the following: Freedom to make life choices, social support, healthy life expectancy, perceptions of corruptions, and generosity. Due to high collinearity between this predictors, only happiness index was included in the model.

Based on the results. An interesting insight is that the coefficient for happiness index in both models is negative, indicating high happiness index negatively affect the birth rate. Taken into account the high correlation between happiness index and freedom to make life choices, and other social aspects, there is a possibility that high level of social support and freedom to make life choices criteria from the specific country encourages individuals to live the life that they prefer, with or without children, thus affecting the birth rates. Furthermore, unemployment rate and inflation rates are also predictors that negatively affect the birth rates in the models.

## Data Sources references

The following datasets were used for the analysis:

1. Birth rate by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/birth-rate-by-country

2. GDP ranked by country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/countries/by-gdp

3. World Happiness Report 2023. Data for Figure 2.1. Sustainable Development Solutions Network. Retrieved via the following link: https://worldhappiness.report/ed/2023/#appendices-and-data

4. The Global Database of Inflation, updated to 2022. Headline Consumer price inflation, annual, The World Bank. Retrieved via the following link: https://www.worldbank.org/en/research/brief/inflation-database

5. Unemployment by Country 2023. World Population Review. Retrieved via the following link: https://worldpopulationreview.com/country-rankings/unemployment-by-country
