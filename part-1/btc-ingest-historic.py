from sqlalchemy import create_engine
import pandas as pd
import configparser
import argparse
from pathlib import Path


config_obj = configparser.ConfigParser()
config_obj.read("config.ini")

# getting the connection string and ticker info from config file
db_str = config_obj["mysql"]["connection_str"]
btc_info = config_obj["btc"]


def read_csv(file_path):
    df = pd.read_csv(
        file_path,
        usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        names=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base_asset_volume",
            "taker_buy_quote_asset_volume",
        ],
        parse_dates=[0, 6],
        date_parser=lambda epoch: pd.to_datetime(epoch, unit="ms"),
    )
    return df


def write_df_to_db(df):
    table_name = btc_info["table_name"]

    engine = create_engine(
        db_str,
        pool_recycle=3600,
    )

    with engine.begin() as connection:
        df.to_sql(table_name, connection, if_exists="append", index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_dir",
        type=Path,
        default=Path(__file__).absolute().parent.parent / "data",
        help="Path to the data directory. Default path is the data folder of the project root.",
    )

    p = parser.parse_args()
    print(p.data_dir, type(p.data_dir))

    # iterate over the files in the data directory and process them into the database
    for f in p.data_dir.iterdir():
        print(f)
        df = read_csv(f)
        write_df_to_db(df)


if __name__ == "__main__":
    main()
