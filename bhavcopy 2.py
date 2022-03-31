import mplfinance as mpf
import talib
import matplotlib.pyplot as plt
from pynse import*
import datetime

nse = Nse()

bhavcopy_full=nse.bhavcopy(series='all')
# print(bhavcopy_full)
bhavcopy_full=bhavcopy_full.reset_index(level=1)
# print(bhavcopy_full)
bhavcopy_eq=bhavcopy_full[bhavcopy_full['SERIES']=='EQ']

print(bhavcopy_eq)

bhavcopy_eq=bhavcopy_eq[['OPEN_PRICE','HIGH_PRICE','LOW_PRICE','CLOSE_PRICE','TTL_TRD_QNTY','DELIV_QTY','DELIV_PER']]
# bhavcopy_eq.sort_values('DELIV_PER', ascending=False)

nifty_50_list=nse.symbols[IndexSymbol.Nifty50.name]

print(nifty_50_list)
print(len(nifty_50_list))

bhavcopy_eq=bhavcopy_eq[bhavcopy_eq.index.isin(nifty_50_list)]
print(bhavcopy_eq.sort_values('DELIV_PER',ascending=False))





# for i in range(len(bhavcopy_eq)):
#     print(bhavcopy_eq.iloc[1])