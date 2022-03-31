# bhavcopy of all the stocks for a particular date
# import pandas as pd
import pynse
from pynse import*
import datetime
import logging
from IPython.display import display

# logging.basicConfig(level=logging.debug())

nse = pynse.Nse()

# print(nse.bhavcopy(req_date=datetime.date(2022, 2, 17)))
# bhav=nse.bhavcopy(req_date=datetime.date(2022,3,7))
bhav=nse.bhavcopy()


for i in range(len(bhav)):
    bhav['ACTION']=(bhav['TTL_TRD_QNTY'])/(bhav['NO_OF_TRADES'])

    # print(bhav.iloc[i])
bhav.style.background_gradient()
# print(bhav)

for i in range(len(bhav)):
    print(bhav.iloc[i]["DELIV_PER"])