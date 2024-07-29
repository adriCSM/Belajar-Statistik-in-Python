import pandas as pd

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