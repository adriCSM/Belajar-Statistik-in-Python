import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/transaksi_retail_dqlab_v2.tsv", delimiter="\t")
assay=pd.read_csv('./ASSAY.csv',delimiter=',')
data=assay[assay.columns[:9]]

# =====Mengelompokkan Data======
# print(data['Ni'].groupby(data['LAYER']).sum())

# =====Mengubah tanggal=====
# df['Bulan'] = df['Tanggal'].apply(
# 	lambda x: datetime.datetime.strptime(x,"%d-%m-%Y").strftime("%m-%Y")
# ) # => # membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"

# print(df.groupby(["Bulan","Nama Produk"])["Jumlah"].sum()) # => # menghitung jumlah item penjualan per produk per bulan

# =====Grafik Scatter Plot=====
# plt.scatter(data['Ni'],data['Fe'],alpha=0.2) # => alpha=0.2 yaitu opacity=0.2
# plt.xlabel('Ni', fontsize=12)
# plt.ylabel('Fe', fontsize=12)
# plt.tight_layout()
# plt.show()

# =====Grafik Histogram=====
# plt.figure(figsize=(8,6))
# plt.hist(data["Ni"])
# plt.grid(color="gray", linestyle="-", linewidth=0.5)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# =====Line Chart=====
# plt.plot(data["Ni"],data['Fe'])
# plt.title("Ni dan Fe",pad=10,fontsize=12,color="blue")
# plt.xlabel("Ni",fontsize=11)
# plt.ylabel("Fe",fontsize=11)
# plt.grid(color="gray",linestyle="-",linewidth=0.5)
# plt.tight_layout()
# plt.show()

# =====Membuat Tabel Frekuensi=====
df["Bulan"] = df["Tanggal"].apply(
	lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
) # => membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"

df["Total"] = df["Harga"] * df["Jumlah"] # => Menghitung total harga untuk setiap row

print(df.groupby(["Bulan", "Nama Produk"])["Total"].sum()) # => menghitung total penjualan per produk per bulan