import pandas as pd
import statsmodels.api as sm

data = pd.read_csv("./ASSAY.CSV", sep=',')

# =====Regresi Linier Sederhana=====

# -----Variabel bebas-----
nilai_x=data[['Ni']]
# -----Variabel tak bebas-----
nilai_y=data[['Fe']]
# -----Membuta model regresi liner-----
model_regresi=sm.OLS(endog=nilai_y,exog=nilai_x).fit()
# -----Cetak laporan dari variabel model regresi----
print(model_regresi.summary())

# =====Penjelasan hasil report model regresi=====
# Nilai coef pada hasil summary di atas adalah besaran slope dari model, pada model ini slope untuk variabel Pendapatan. Selain itu terdapat beberapa nilai yang menyertainya yaitu std err yang merupakan nilai kesalahan baku (standard error) dari koefisien tersebut, t-statistics yang merupakan nilai yang diperoleh dengan membagi nilai koefisien dengan nilai kesalahan baku. 
# Terakhir adalah p-value yang dapat digunakan untuk memastikan bahwa koefisien signifikan atau tidak untuk menjelaskan variasi pada model.
# Nilai koefisien dapat menggambarkan seberapa besar efek suatu variabel bebas dengan variabel tak bebas. Selain itu dapat menunjukkan arah dari hubungan tersebut. Jika koefisien bernilai positif maka variabel tak bebas akan naik jika nilai pada variabel bebas naik. Namun jika koefisien bernilai negatif maka variabel tak bebas akan turun jika nilai pada variabel bebas naik.
# Nilai const atau konstan adalah nilai intercept pada model dimana jika nilai koefisien sama dengan nol, maka nilai variabel tak bebas akan sama dengan nilai konstan.
# Untuk memastikan bahwa koefisien suatu variabel bebas memiliki pengaruh yang signifikan, kita dapat menggunakan p-value. Jika p-value memiliki nilai kurang dari level signifikansi tertentu, maka dapat dikatakan bahwa koefisien memiliki efek yang signifikan terhadap model. Dalam hasil summary di atas, diperoleh bahwa p-value sebesar 0.000.
# Jika kita menggunakan angka signifikansi : a=17.377
# Maka p-value < a sehingga koefisien yang diperoleh signifikan untuk model ini.


# =====R-Squared (R pangkat 2)=====
# R-squared adalah salah satu ukuran yang digunakan untuk menilai seberapa baik variabel independen yang digunakan untuk menjelaskan variasi pada variabel dependen. Semakin besar nilainya atau semakin mendekati 1, semakin baik modelnya.
# Pada hasil summary di atas diperoleh bahwa nilai R pangkat 2= 0.719
# yang berarti persentase perubahan variabel tak bebas 'Fe' yang dijelaskan oleh variabel bebas 'Ni' sebesar 71.9%. Dan sekitar 28,1% sisanya dipengaruhi oleh faktor-faktor lainnya yang tidak termasuk di dalam model.

# =====Uji Asumsi Klasik=====
# Hal yang harus diperhatikan dalam regresi linier adalah apakah residual dari model berdistribusi normal atau tidak atau apakah terdapat homoskedastisitas atau tidak dan faktor-faktor lainnya.
# -----Residual Harus Berdistribusi Normal-----
# Agar model regresi valid, maka resiudal dari model harus berdistribusi normal. Hal ini dapat kita baca dari hasil summary dari model, yaitu skew. Semakin nilainya mendekati nol maka distribusi residual mendekati normal. Pada contoh sebelumnya kita memperoleh nilai skew sebesar 0.251 yang berarti distribusi dari residual cukup normal.
# -----Homoskedastisitas-----
# Selain distribusi dari residual harus mendekati atau berdistribusi normal, homoskedastisitas adalah salah satu syarat yang harus dipenuhi agar model yang dibuat valid. Homoskedastisitas adalah kondisi dimana variansi dari error seragam. Ketika yang terjadi justru variansinya semakin membasar atau mengecil maka yang terjadi adalah heteroskedastisitas. 
# Kita dapat mengamati ini dari nilai Durbin-Watson. Jika nilai Durbin-Watson di antara nilai 1 dan 2 maka dapat dipastikan bahwa terdapat homoskedastisitas pada model.
# Pada contoh sebelumnya kita memperoleh nilai Durbin-Watson sebesar 0.494 yang berarti terdapat homoskedastisitas pada model sehingga model valid untuk digunakan.