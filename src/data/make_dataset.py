# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
        Loads raw CSV, imputes missing values and stores in processed
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    # load file
    gas_src = pd.read_csv(input_filepath)
    
    # rename columns
    gas_src.columns = ['day','s1_deg_c','s2_deg_c','s1_wind','s2_wind','gas_demand']
    
    # parse and set date index
    gas_src['day'] = pd.to_datetime(gas_src['day'],format="%d/%m/%Y")
    gas_src = gas_src.set_index('day')

    # fill in missing dates
    alldays = pd.date_range(
        start = gas_src.first_valid_index(), 
        end = gas_src.last_valid_index() )
    gas_src = gas_src.reindex(alldays)

    # interpolate missing data
    gas_src = gas_src.apply(lambda x: x.interpolate(method='time'), axis=0)

    # save processed dataset read for forecasting
    gas_src.to_pickle(output_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
