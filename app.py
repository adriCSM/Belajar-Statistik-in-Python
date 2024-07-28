import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv('./COLLAR_5D1.csv',sep=',')
import matplotlib.pyplot as plt
# plt.rcParams['font.family']='Times New Roman' #mengganti font pada metplotlib

# =========================Transformasi Data Kategorik ke Dalam Angka==========
