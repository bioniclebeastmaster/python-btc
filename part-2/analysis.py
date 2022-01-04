import pandas as pd
import numpy as np
from scipy import stats
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


plt.style.use("ggplot")

engine = create_engine("mysql+pymysql://btc_user:btc_db_user_pwd@localhost:3306/btc_db")

conn = engine.connect()

# using the close price to calculate moving average; could aslo use open, high or low instead
df = pd.read_sql("SELECT open_time, close from btcusdt_1m_klines", conn)
df.set_index("open_time", inplace=True)

# copying this data frame for using in next steps
df_out = df.copy()

# calculating z score for the close price column
df_out["z score"] = np.abs(stats.zscore(df_out["close"]))

# the maximum for 3 months of data from October to December is 2.15, which is less than 3,
# so we are not justified in removing records based on this
df_out["z score"].max()


# calculating simple moving average over 5 hour and 10 hours
df["MA 5 hour"] = df["close"].rolling(300).mean()
df["MA 10 hour"] = df["close"].rolling(600).mean()


# select 1 day to visualize
df_1_day = df.tail(1440)

plt.plot(df_1_day["close"], label="Close")
plt.plot(df_1_day["MA 5 hour"], label="MA 5 hour")
plt.plot(df_1_day["MA 10 hour"], label="MA 10 hour")
plt.legend(loc="best")
plt.xticks(rotation=45)
plt.title("BTC\nClose and Moving Averages")
plt.show()
