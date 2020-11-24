# Overview of work done - exploration

## Specifications

The task is to derive a forecasting model for out of sample predictions for year 2018

I note 2018 and 9 months of 2019 are actually included in the dataset.

The data contains a daily gas demand and weather information from two stations (assuming the naming is consistent)



## Assumptions

The cost/loss function is not specified - the default VARMAX minimising mean squared error is adopted.

The resolution of the desired predictions is not given - only that it's more than 1. 

The assumption is the temperature is the some form average daily temperature and the wind speed is the some form of averaged higher daily wind speed, and these are a heuristic for the level of wind energy that would be an alternative source  of power and also the temperature indicated the level of heating required. 

The temperatures range from -7.3 to 29.21 and the wind 1.8 to 22.1 m/s and the gas around 34 billion cubic metres a year which looks per [wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption) not far off the Netherlands, who are also using [wind power](https://en.wikipedia.org/wiki/Wind_power_by_country) and the temperatures seem plausible

## Imputation

There are missing dates and missing values for the dates that are there.





## Text editor examination

Initially the CSV raw data was examined with a text editor. Because the size is very small < 84kb, it's easy to review the file. Large files one would need to view on a sample basis.

There are 6 fields

**dy** a day in dd/mm/yyyy format

Running from the 1st of October 2013 up to 30th September 2019

**station_01_temperature_degrees_celcius** 

**station_02_temperature_degrees_celcius**

Note Celsius is misspelt Celcius

**station_01_wind_speed_m_per_s**

**station_02_wind_speed_m_per_s**

**gas_demand_mcm**

all of these look numeric and to two decimal places

The header is a single row and the fieldnames contiguous text

There are 2174 data entries

## Data Insights

Gas demand is strongly negatively correlated until the temperature reaches about 15 degrees C when the demand flattens out. The temperature doesn't get about 30 in the dataset, so there is no evidence for a suggested impact of high temperatures.

The relationship with wind is more complicated - below a window of around 13 m/s there is a much greater range of gas demand,  and above that it's a smaller range and higher. Possibly this is indicative of the turbines not working at higher speeds.

![](references/pairplot.png?raw=true)





Looking at the plain data plots highlights the winter summer seasonality, with corresponding winter demand

![data over time](references/seasonal.png?raw=true)





## Further work

More relevant data will improve the predictions - e.g. future predictions on the economy, and even from the weather stations selected ensuring that the data reflects more closely the impact on the use of gas as well as different models, such as recurrent neural networks.

There is scope to improve the handling of multiple seasonalities and also holidays, some of which will be particular  to the country in question

The imputation at the moment is using the time series interpolation with pandas

E.g. where there is a large range in the day, an average temperature may not indicate the energy needed for cooling during the lows and heating at the highs. Similarly there's only a range of winds when wind turbines are effective - averaging the max and min wind during the day would not be the best heuristic for the the available energy from wind turbines.

