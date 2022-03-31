import pynse
from pynse import*
import datetime
import logging

# logging.basicConfig(level=logging.debug())

nse = pynse.Nse()

# print(nse.market_status())
print(nse.info('HINDUNILVR'))

print(nse.get_quote('HINDUNILVR'))
data=nse.get_quote('HINDUNILVR')
close=data["close"]
print("entry",close*1.01)
print("stop loss",close*1.03)
print("exit",(close*.94))



# #
# print(nse.get_quote('SBIN', segment= Segment.FUT))
# #
# print(nse.get_quote('NIFTY', segment= Segment.OPT, strike=15200))
#
# print(nse.expiry_list)
#
# print(nse.strike_list)
#
# print(nse.bhavcopy(req_date=datetime.date(2022, 3, 7)))
#
# print(nse.bhavcopy_fno(req_date=datetime.date(2022, 3, 7)))
#
# print(nse.pre_open())
#
# print(nse.option_chain('INFY',datetime.date(2022, 2, 24)))
#
# print(nse.fii_dii())
# #
# infy=nse.get_hist('INFY',datetime.date(2021, 2, 24),datetime.date(2022, 3, 7))
# print(infy)
# # infy.close.plot()
#
# # print(nse.get_indices(IndexSymbol.NiftyBank))
# data=nse.get_indices(IndexSymbol.NiftyBank)
# # for i in range(20):
#     print(data1.iloc[i])

# print(nse.top_losers(IndexSymbol.Nifty50).head(5))
# list_index=dir(IndexSymbol)
# for i in list_index:
#     print(i)
#     index = eval("IndexSymbol"+"."+i)
#     try:
#         data=nse.top_gainers(index).head(10)
#         print(data['pChange'])
#         # print(data.columns)
#     except ValueError:
#         print ("sorry")
#

# print(nse.top_losers(IndexSymbol.Nifty50).head(5))
# list_index=dir(IndexSymbol)
# for i in list_index:
#     # print(i)
#     dict_index={}
#     index = eval("IndexSymbol"+"."+i)
#
#     try:
#         data=nse.get_indices(index)
#         # val1=data.index.values
#         # val2=data["percentChange"]
#         # # dict_index[val1]=val2
#         print(data["percentChange"])
#
#         # print(data.columns)
#     except ValueError :
#         print ("sorry")
# #




# trade_days=nse.trading_days()
# # for i in trade_days:
# #     print(datetime.date(i))
# print(trade_days)
# print(type(trade_days))
# print(nse.fii_dii())
# val=nse.fii_dii()
# print(val)
# # trade_days=nse.trading_days()
# for i in trade_days:

# cagr=((130000/70000)**(1/2)-1)*100
#
# print(cagr)
#
#

# import mplfinance as mpf
# from mplfinance.original_flavor import candlestick_ohlc
# data.index = pd.to_datetime(data.index)
# mpf.plot(data, type='candle', volume=True)
