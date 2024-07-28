import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# data=pd.read_csv('./COLLAR_5D1.csv',sep=',') # Data Colar
data=pd.read_csv('./ASSAY.csv',sep=',') # Data Colar
fig, ax = plt.subplots()
# ======mengganti jenis tulisn=====
# plt.rcParams['font.family']='Times New Roman' #mengganti font pada metplotlib

# =====Define bin edges=====
interval=0.1
bins = np.arange(data['Ni'].min(), data['Ni'].max(), interval)  # Bins from -4 to 4 with a width of 1

# =====show histogram====
# data.hist(column='Ni',edgecolor='#376190',bins=bins,color='#4F81BD',zorder=3) # Membuat histogram mennggunakan pandas
plt.hist(x='Ni', data=data,edgecolor='#376190',bins=bins,color='#4F81BD',zorder=3,align='right') #embuat histogram mennggunakan matplotlib
plt.grid(True,color='#DFE7DE')

ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2)) 
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))  
plt.xlabel('Ni',fontsize=14)
plt.ylabel('Count',fontsize=14)
plt.title('Hist dari matplotlib.pyplot', size=14)
plt.xlim(left=0)  # Mengatur batas kiri sumbu x
plt.tight_layout()
plt.show()