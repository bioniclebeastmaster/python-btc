from binance.client import Client
from binance import ThreadedWebsocketManager
import datetime
from sqlalchemy import MetaData, create_engine


def btc_process_1m_kline(msg):
    """Process incoming kline WebSocket messages. Only processes klines that are closed;
    converts epoch time to timestamp and writes the data to database"""
    btc_data = {}

    # check if message has errors; log the error if it happens
    if msg["e"] != "error":

        # check if kline is closed
        if msg["k"]["x"] == True:
            # process the message, convert epoch time to timestamp
            btc_data["open_time"] = datetime.datetime.fromtimestamp(
                msg["k"]["t"] / 1000.0
            )
            btc_data["open"] = msg["k"]["o"]
            btc_data["high"] = msg["k"]["c"]
            btc_data["low"] = msg["k"]["h"]
            btc_data["close"] = msg["k"]["l"]
            btc_data["volume"] = msg["k"]["v"]
            btc_data["close_time"] = datetime.datetime.fromtimestamp(
                msg["k"]["T"] / 1000.0
            )
            btc_data["quote_asset_volume"] = msg["k"]["q"]
            btc_data["number_of_trades"] = msg["k"]["n"]
            btc_data["taker_buy_base_asset_volume"] = msg["k"]["V"]
            btc_data["taker_buy_quote_asset_volume"] = msg["k"]["Q"]
            write_data_to_db(btc_data)
    else:
        print(msg)


def write_data_to_db(data_dict):
    table_name = "btcusdt_1m_klines"
    engine = create_engine(
        "mysql+pymysql://btc_user:btc_db_user_pwd@localhost:3306/btc_db"
    )
    # TODO: put the engine creation and connection in outer scope so that
    # a new session is not created each time a message is written
    with engine.begin() as connection:
        meta_data = MetaData(bind=engine)
        MetaData.reflect(meta_data)
        BTC_TABLE = meta_data.tables[table_name]
        connection.execute(BTC_TABLE.insert(), data_dict)


def main():
    # init and start the WebSocket
    bsm = ThreadedWebsocketManager()
    bsm.start()

    # subscribe to a stream and process the messages into the data base using the callback function
    bsm.start_kline_socket(
        callback=btc_process_1m_kline,
        symbol="BTCUSDT",
        interval=Client.KLINE_INTERVAL_1MINUTE,
    )


if __name__ == "__main__":
    main()
