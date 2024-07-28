import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv('./COLLAR_5D1.csv',sep=',')
import matplotlib.pyplot as plt
# plt.rcParams['font.family']='Times New Roman' #mengganti font pada metplotlib



# ===============================Membuat Scatter Plot==============================
plt.clf()
# data.plot.scatter(x='X', y='Y') #menagnmbil data untuk ditampilkan pada scatter plot
# plt.title('plot scatter dari pandas', size=14) #menampikan title scatter plot
# plt.xlabel('Koordinat X') #memberi name label x
# plt.ylabel('Koordinat Y') #memberi name label y
# plt.tight_layout() #untuk menampilkan scater plot full tanpa ada layer y terpotong
# plt.show() #menampilan diagram scatter plot menggunakan module matplotlib



# =================================Membuat Histogram==============
# data.hist(column='Depth') # Membuat histogram mennggunakan pandas
# plt.hist(x='Depth', data=data,bins=20,) #embuat histogram mennggunakan matplotlib
# plt.xlabel('Depth')
# plt.title('Hist dari matplotlib.pyplot', size=14)
# plt.tight_layout()
# plt.show()

# ================================Membuat box plot====================
# data.boxplot(column='Depth') #pandas
# plt.boxplot(x = 'Depth', data=data) #matplotlib
# plt.xlabel('Depth')
# plt.tight_layout()
# plt.show()


# ===================================Membuat bar=======================
# hitung frekuensi dari masing-masing nilai pada kolom 'Depth'
# class_freq = data['Depth'].value_counts()
# class_freq.plot.bar() #pandas
# plt.bar(x=class_freq.index, height=class_freq.values) #matplotlib
# plt.title('bar dari Depth', size=14)
# plt.tight_layout()
# plt.show()

# =====================================Membuat pie chart=======================
# class_freq = data['Depth'].value_counts()
# class_freq.plot.pie() #pandas
# plt.pie(class_freq.values, labels=class_freq.index) #matplotlib
# plt.title('plt.pie dari Depth', size=14)
# plt.tight_layout()
# plt.show()