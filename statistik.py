import numpy as np
import pandas as pd

# Package Statistika di Python
# 1. numpy => untuk melakukan analisa data numerik dan perhitungan berbasis vektor atau matriks
# 2. pandas => untuk melakukan pengolahan data tabular
# 3. matplotlib => untuk melakukan ploting atau penggambaran grafik, dapat digunakan sebagai alat bantu dalam analisa data
# 4. statsmodels => untuk melakukan uji hipotesa, eksplorasi data maupun pemodelan statistika
# 5. scipy => untuk melakukan uji statistika, juga dapat digunakan untuk melakukan pemodelan statistika

data=pd.read_csv('./Assay.csv',sep=',')

# ===== Inspeksi data =====
# print(data) # => Melihat semua data
# print(data.head(10)) # => melihat 10 data pertama
# print(data.tail()) # => tail secara defaul menampilkan 5 data terakhir
# print(data.shape) # => melihat dimensi data (baris, colom) 
# print(data.shape[0]) # => mengambili jumlah atau count data
# print(data.columns) # => melih header setiap columns
# print(data.isna()) # => mengecek data yang hilang dalam cell jika true=kosong false=ada isi
# print(data.isna().sum()) # => menghitung data yang kosong pada setiap kolom
# print(data.max()) # => Mencari nilai max pada setiap kolom
# print(data[[data.columns[5],data.columns[6]]].max()) # => Mencari nilai max pada kolom index 6 dan 7
# print(data[[data.columns[5],data.columns[6]]].min()) # => Mencari nilai min pada kolom index 6 dan 7
# print(data.sum()) # => menghitung jumlah dari setiap kolom (akan error juka ada data berite non numerik)
# print(data.sum(numeric_only=True)) # => menghitung jumlah dari setiap kolom bertipe numerik
# print(data[['Ni','Fe']].sum()) # => menghitung jumlah dari setiap kolom
# print(data['Ni']) # => memilih kolom Ni saja
# print(data[:10]) # => mengambil data dari baris ke-0 sampai baris ke-(10-1) atau baris ke-9
# print(data.loc[[1,3,10]])# => mengambil data pada baris ke-2, ke-4 dan ke-11
# print(data['Ni'][:10]) # => Mengambil kolom 'Ni' dan ambil baris ke-1 sampai ke-9
# print(data['Ni'].loc[[1,3,10]]) # => Mengambil kolom 'Ni' dan ambil baris ke-1,3,9

# note: 
# jika terurut menggunakan data[1:10] 
# jika tidak terurut menggunakan data.loc[1,3,8] 

# =====Ukuran Pusat=====

# limonit=data[data['LAYER']=='LIM'] # => mengambil hanya data untuk Layer 'LIM'
# -----Mean-----
# print(limonit['Ni'].mean()) # => menghitung mean nilai Ni yang memiliki layer 'LIM' ( lib pandas)
# print(np.mean(limonit['Ni'])) # => menghitung mean nilai Ni yang memiliki layer 'LIM' ( lib numpy)
# -----Median----
# print(limonit['Ni'].median()) # => menghitung mean nilai Ni yang memiliki layer 'LIM' ( lib pandas)
# print(np.median(limonit['Ni'])) # => menghitung mean nilai Ni yang memiliki layer 'LIM' ( lib numpy)
# -----Modus-----
# print(data['LAYER'].value_counts()) # => Melihat jumlah data dari masing-masing Layer
# -----Kuantil-----
# print(data['Ni'].quantile(q=0.9)) # => Mencari nilai data urutan ke-90% (lib pandas)
# print(np.quantile(data['Ni'],q=0.9)) # => Mencari nilai data urutan ke-90%  (lib numpy)
# -----Agregasi data------
# print(data[['Ni','Fe'].agg([np.mean,np.median])) # => menghitung rerata dan median 'Ni' dan 'Fe'
# print(data[['Ni','Fe','LAYER']].groupby('LAYER').agg([np.mean,np.median])) # => # menghitung rerata dan median Ni dan Fe dari tiap LAYER

#=====Ukuran Sebaran Data=====
# Tipe Data Nominal dan Ordinal:
# 1. Proporsi Kategori (Categorical Proportion)
# 2. Persen Proporsi (Percent Proportion)
# 3. Rasio Variasi (Variation Ratio)
# Tipe Data Interval dan Rasio:
# 1. Rentang (Range)
# 2. Variansi (Variance)
# 3. Deviasi Baku (Standard Deviation)

# -----Proporsi Kategori-----
# print(data['LAYER'].value_counts()/data.shape[0]) # => cari proporsi tiap Produk
# -----Rentang (range)-----
# print(data['Ni'].max()-data['Ni'].min()) # => Cari nilai rentang dari kolom 'Ni'
# -----Variansi-----
# print(data['Ni'].var()) # => Variansi (lib pandas), Secara default pandas mengitung variansi sampel
# print(np.var(data['Ni'])) # => Variansi (lib numpy),Secara default pandas mengitung variansi populasi
# print(data['Ni'].var(ddof=0)) # => mengubah variansi pandas dari sampel menjadi populasi

