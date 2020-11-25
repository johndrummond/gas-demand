Estimation of gas demand
==============================

This project is a gas demand prediction time series test with weather from [emailed specification](references/Problem_Specification.md) and [dataset](data/raw/weather_and_gas_demand_historic_actuals.csv)

Predictions were made for year 2018 initially on a daily frequency

## To Use

### Exploration and cleansing

Read the  [commentary on exploring the data](references/Work_Done_Summary.md) 

Review the [data exploration notebook](notebooks/Exploratory_Analysis.ipynb) 

### Prediction

There is a markdown  [commentary on the prediction](references/Forecasting.md)

And a [notebook exploring the prediction](notebooks/forecasting.ipynb) 

### Running locally

Clone the repository locally. Note this was developed on Ubuntu 20 using Windows WSL and should work on any Linux

This command from the project root will convert the initial CSV file into the processed data file, imputing missing values:

`python src/data/make_dataset.py data/raw/weather_and_gas_demand_historic_actuals.csv data/processed/gas_demand.pkl`

The  notebooks could be run through the local Jupyter server.











Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
