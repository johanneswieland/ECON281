#%%
# packages inlcuding fred api
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from fredapi import Fred

# from FRED api import case shiller index and cpi
fred = Fred(api_key='8421e3d428af211481082f8111431c70')
csi = fred.get_series('CSUSHPINSA')
cpi = fred.get_series('CPIAUCNS')

# convert to dataframe
csi = pd.DataFrame(csi)
cpi = pd.DataFrame(cpi)

# merge the two dataframes
data = pd.merge(csi, cpi, left_index=True, right_index=True)
data.columns = ['csi', 'cpi']

# calculate the real house price index normalized to 100 in 1997
data['real_house_price'] = data['csi'] / data['cpi'] * 100
data['real_house_price'] = data['real_house_price'] / data['real_house_price'].loc['1997'].mean() * 100

# plot the real house price index from 1993 - 2023 and save in figures folder
plt.figure()
data['real_house_price'].loc['1992':].plot()
plt.title('Real House Price Index')
plt.savefig('figures/real_house_price.png')
# %%
