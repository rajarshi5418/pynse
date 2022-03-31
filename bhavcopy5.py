# historicl bhavcopy of list list of  stock
import mplfinance as mpf
import talib
import matplotlib.pyplot as plt
from pynse import*
import pandas as pd
import datetime
import datetime
from datetime import timedelta

# datetime.date(2022, 2, 16)

nse = Nse()

data=nse.top_gainers(IndexSymbol.Nifty50)
# print(data.index.to_list())
data2=data.index.to_list()
print(data2)
trade_days=nse.trading_days()
print(trade_days)
for j in data2:
    # print(j)
    bhavcopy_list = pd.DataFrame()
    for i in trade_days:
        try:
            # print(i)
            # dt3=datetime.date.today()-timedelta(days=i)
            bhavcopy_full=nse.bhavcopy(series='all',req_date=i.date())
            # print(bhavcopy_full)
            bhavcopy_full=bhavcopy_full.reset_index(level=1)
            # print(bhavcopy_full)
            bhavcopy_eq=bhavcopy_full[bhavcopy_full['SERIES']=='EQ']
            # print(bhavcopy_eq)
            bhavcopy_eq=bhavcopy_eq[['DATE1','OPEN_PRICE','HIGH_PRICE','LOW_PRICE','CLOSE_PRICE','TTL_TRD_QNTY','NO_OF_TRADES','DELIV_QTY','DELIV_PER']]

            bhavcopy_eq=bhavcopy_eq[bhavcopy_eq.index.isin([j])]
            # print(bhavcopy_eq.sort_values('DELIV_PER',ascending=False))
            bhavcopy_list = pd.concat([bhavcopy_list,bhavcopy_eq])
        except KeyError:
            print("data not fetched")
    # print(bhavcopy_list.sort_values('DATE1',ascending=False))

    bhavcopy_list["DELIV_PER"] = bhavcopy_list.DELIV_PER.astype(float)
    bhavcopy_list["DELIV_QTY"] = bhavcopy_list.DELIV_QTY.astype(float)
    bhavcopy_list["ACTION"] = bhavcopy_list["TTL_TRD_QNTY"]/bhavcopy_list["NO_OF_TRADES"]

    # print(bhavcopy_list.info())
    avg=bhavcopy_list["DELIV_PER"].mean()
    # print("average delivery",avg)
    avg1=bhavcopy_list["ACTION"].mean()
    avg2=bhavcopy_list["TTL_TRD_QNTY"].mean()
    # print("Average action",avg1)

    val1=float(bhavcopy_list["DELIV_PER"].iloc[-1])
    val2=float(bhavcopy_list["ACTION"].iloc[-1])

    if val1>avg :
        if val2>avg1 :
            print(j)
            print("average delivery", avg)
            print("Average action", avg1)
            print("Average trade", avg2)
            print(bhavcopy_list)
            print("")

            data3 = bhavcopy_list["TTL_TRD_QNTY"].to_list()
            print(data3)




