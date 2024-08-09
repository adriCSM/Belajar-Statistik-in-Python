import pandas as pd
import numpy as np

assay=pd.read_csv('./ASSAY.csv',delimiter=',')
data=assay[assay.columns[:9]]

# -----DataFrame & Series---
number_list = pd.Series([1,2,3,4,5,6]) #=> Series
matrix = [[1,2,3],
          ['a','b','c'],
          [3,4,5],
          ['d',4,6]] #=> dataframe
print(number_list)
print(matrix)

# -----method info
print(data.info()) # => untuk mengecek kolom apa yang membentuk dataframe itu, data types, berapa yang non null, dll. Method ini tidak dapat digunakan pada series, hanya pada dataframe saja.

# -----attribute .shape
print(data.shape) # => digunakan untuk mengetahui berapa baris dan kolom, hasilnya dalam format tuple (baris, kolom)

# -----Attribute .dtypes
print(data.dtypes) #=> untuk mengetahui tipe data di tiap kolom. Tipe data object: kombinasi untuk berbagai tipe data (number & text, etc)

# -----Method .astype(nama_tipe_data)
print(f"astype:{number_list.astype('str')}")# =>untuk convert tipe data

# -----Attribute .copy()-----
data_assay=data.copy()# => melakukan duplikat, untuk disimpan di variable yang berbeda
print(data_assay)

# -----Attribute .to_list()-----
print(number_list.to_list()) #=> untuk mengubah series menjadi list dan tidak dapat digunakan untuk dataframe

# ----- Attribute .unique()-----
print(f"test:{number_list.unique()}") #=>menghasilkan nilai unik dari suatu kolom, hasilnya dalam bentuk numpy array.

# -----Attribute .index-----
print(number_list.index) #=> untuk mencari index/key dari Series atau Dataframe

# -----Attribute .columns-----
print(data.columns) #=> untuk mengetahui apa saja kolom yang tersedia di dataframe tersebut (hanya digunakan untuk dataframe saja)

# -----Attribute .loc-----
print(number_list.loc[:3]) #=> digunakan slice dataframe atau series berdasarkan nama kolom dan/atau nama index.

# -----Attribute .iloc-----
print(number_list.iloc[:2]) #=> untuk slice dataframe atau series berdasarkan index kolom dan/atau index

# -----Creating Series & Dataframe from List-----

ex_list = ['a',1,3,5,'c','d']
ex_series = pd.Series(ex_list) #=> Creating series from list
print(ex_series)

ex_list_of_list = [[1,'a','b','c'],
                   [2.5,'d','e','f'],
		           [5,'g','h','i'],
		           [7.5,'j',10.5,'l']]
index = ['dq','lab','kar','lan']
cols = ['float','char','obj','char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols) #=> Creating dataframe from list of list
print(ex_df)

# -----Creating Series & Dataframe from Dictionary-----
dict_series = {'1':'a',
			   '2':'b',
			   '3':'c'}
ex_series = pd.Series(dict_series) # Creating series from dictionary
print(ex_series)

df_series = {'1':['a','b','c'],
             '2':['b','c','d'],
             '4':[2,3,'z']}
ex_df = pd.DataFrame(df_series) # Creating dataframe from dictionary
print(ex_df)

# -----Creating Series & Dataframe from Numpy Array-----
# Creating series from numpy array (1D)
arr_series = np.array([1,2,3,4,5,6,6,7])
ex_series = pd.Series(arr_series)
print(ex_series)
# Creating dataframe from numpy array (2D)
arr_df = np.array([[1,2,3,5],
                   [5,6,7,8],
                   ['a','b','c',10]])
ex_df = pd.DataFrame(arr_df)
print(ex_df)

# -----Indexing----
#=> Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t") 
print("Index: ",df.index) #=> Index dari df
print("Columns: ",df.columns) #=> Column dari df

# Set multi index df
df_x = df.set_index([ 'order_id', 'customer_id', 'product_id', 'order_date']) 
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level) # Print nama dan level dari multi index

 # Baca file sample_tsv.tsv untuk 10 baris pertama saja 
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t",nrows=10) #=> Baca file TSV sample_tsv.tsv
# Cetak data frame awal
print("Dataframe awal:\n", df) 
df.index = ["Pesanan ke-" + str(i) for i in range(1, 11)] # Set index baru
print("Dataframe dengan index baru:\n", df) # Cetak data frame dengan index baru

# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))

# -----Slicing -----
# slicing adalah cara untuk melakukan filter ke dataframe/series berdasarkan kriteria tertentu dari nilai kolomnya ataupun kriteria index-nya.

# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == 18055 ) &(df["product_id"].isin(["P0029","P0040", "P0041", "P0116","P0117"]))]
print("Slice langsung berdasarkan kolom:\n", df_slice)