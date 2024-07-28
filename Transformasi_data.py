import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv('./COLLAR_5D1.csv',sep=',')
import matplotlib.pyplot as plt
# ===========Transformasi Data dan Kaitannya dengan Distribusi Data (mengubanya menjadi mendekati distribusi normal)================

#----------Menampuilak histogram seluruh kolom
# data.hist()
# plt.title('Histogram seluruh kolom', size=14)
# plt.tight_layout()
# plt.show()

#----------Menampuilak histogram  kolom Depth
# data['Depth'].hist()
# plt.title('Histogram Depth', size=14)
# plt.tight_layout()
# plt.show()

# -----------histogram Depth memiliki skewnes negative => maka dilakukan transformasi menggunakan akar lima
# np.power(data['Depth'], 1/5).hist()
# plt.title('Histogram pendapatan - transformasi menggunakan akar lima', size=14)
# plt.tight_layout()
# plt.show()

# ----------simpan hasil transformasi
pendapatan_akar_lima = np.power(data['Depth'], 1/5)

# ----------membuat qqplot pendapatan - transformasi menggunakan akar lima
# plt.figure()
# stats.probplot(pendapatan_akar_lima, plot=plt)
# plt.title('qqplot Depth - transformasi menggunakan akar lima', size=14)
# plt.tight_layout()
# plt.show()

# ------------membuat qqplot pendapatan
# plt.figure()
# stats.probplot(data['Depth'], plot=plt)
# plt.title('qqplot Depth', size=14)
# plt.tight_layout()
# plt.show()

#============================Transformasi dengan Box-Cox (cara cepat)===============
hasil, _ = stats.boxcox(data['Depth'])

# -------------Menampilkan Histogram dari variabel hasil
# plt.hist(hasil)
# plt.title('Histogram Depth Transformation', size=14)
# plt.tight_layout()
# plt.show()

# -------------Menampilan QQPlot hasil Transformasi
# stats.probplot(hasil, plot=plt)
# plt.title('qqplot', size=14)
# plt.tight_layout()
# plt.show()