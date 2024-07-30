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
print(number_list.loc[:3]) #=> igunakan slice dataframe atau series berdasarkan nama kolom dan/atau nama index.

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
