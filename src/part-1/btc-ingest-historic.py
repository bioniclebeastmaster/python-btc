from sqlalchemy import create_engine
import pandas as pd
import configparser


def read_csv():
    df = pd.read_csv(
        "/home/marina/python_projects/python-btc-project/src/data/BTCUSDT-1m-2021-12.csv",
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
    table_name = "btcusdt_1m_klines"

    engine = create_engine(
        "mysql+pymysql://btc_user:btc_db_user_pwd@localhost:3306/btc_db",
        pool_recycle=3600,
    )

    with engine.begin() as connection:
        df.to_sql(table_name, connection, if_exists="append", index=False)


def main():
    try:
        df = read_csv()
        write_df_to_db(df)
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
