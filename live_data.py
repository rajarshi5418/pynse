# fetch live stock data
from pynse import*
import pandas as pd

nse = Nse()

data = nse.get_quote("SBIN")
print(type(data))

# print(data.keys())
for i in data.keys():
    print(i,data[i])