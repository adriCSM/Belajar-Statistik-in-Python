import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv("./ASSAY.CSV", sep=',')
plt.clf()

ni=data[data.columns[4:9]]


# =====Matrix korelasi=====
# # mengatur ukuran gambar/plot
# # plt.rcParams['figure.dpi'] = 100
# # plt.matshow(ni.corr()) # => matshow untuk membuat visualisasi matrix (tanpa label/nilai)
# sns.heatmap(ni.corr(),annot=True) # => matshow untuk membuat visualisasi matrix (dengan label/nilai)
# # annot=True digunakan untuk menampilkan nilai korelasi di dalam heatmap
# plt.title('Plot correlation matriks Ni', size=14)
# plt.tight_layout()
# plt.show()

# =====Grouped Box Plot====
# ni.boxplot(rot=90) # => boxplot biasa tanpa pengelompokkan
# data[data.columns[4:9]].boxplot(by='LAYER') # => box plot dengan pengelompokkan dilakukan oleh kolom 'LAYER'
# plt.title('Boxplot tanpa pengelompokkan', size=14)
# plt.tight_layout()
# plt.show()

# =====Grouped Histogram====
# data[data['LAYER']=='LIM'].hist()
# plt.title('Limonit',size=14)
# data[data['LAYER']=='SAP'].hist()
# plt.title('Saprolit',size=14)
# data[data['LAYER']=='BRK'].hist()
# plt.title('Bedrock',size=14)
# plt.tight_layout()
# plt.show()

# =====Hex Bin Plot====
# ni.plot.hexbin(x='Ni', y='Fe', gridsize=25, rot=90)
# plt.ylabel(ni.columns[2])
# plt.xlabel(ni.columns[1])
# plt.tight_layout()
# plt.show()

# =====Scatter Matrix Plot====
# _, ax = plt.subplots(1, 1, figsize=(10,10)) # => Membuat subplots dengan ukuran 1 baris dan 1 kolom dengan ukuran plot 10x10.
# scatter_matrix(ni, ax=ax)
# plt.show()

# ===== Density diagonal Plot====
# _, ax = plt.subplots(1, 1, figsize=(10,10)) # => Membuat subplots dengan ukuran 1 baris dan 1 kolom dengan ukuran plot 10x10.
# scatter_matrix(ni,diagonal='kde', ax=ax) # => 'kde' (kernel density estimation)
# plt.show()