import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# =====survey Tingi badan====
# # Baca data survei_tinggi_badan.txt dengan numpy loadtxt
tinggi_badan=np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt",skiprows=1)

# desc_stat=stats.describe(tinggi_badan)
# print("Statistik deskriptif tinggi badan:\n", desc_stat)

# -----Histogram Data Survei-----
# # Buat figure sebagai canvas dengan ukuran 8 in x 6 in
# fig, ax = plt.subplots(figsize=(8, 6))
# # plotkan histogram untuk frekuensi 
# sns.histplot(x=tinggi_badan, binwidth=1, binrange=(tinggi_badan.min()-0.5, tinggi_badan.max()+0.5), ec="w", ax=ax)
# # buat sumbu berikutnya agar frekuensi relatif dapat dijadikann pada satu plot
# ax1 = ax.twinx()
# # plotkan histogram untuk frekuensi relatif
# sns.histplot(x=tinggi_badan, stat="probability", binwidth=1, binrange=(tinggi_badan.min()-0.5, tinggi_badan.max()+0.5), kde=True, ec="w", ax=ax1)
# # set label
# ax.set_xlabel("Tinggi badan (cm)", fontsize=12)
# ax.set_ylabel("Frekuensi", fontsize=12)
# ax1.set_ylabel("Frekuensi relatif\n(Probabilitas)", fontsize=12)
# ax1.grid(axis="y")
# plt.tight_layout()
# plt.show()

# -----Histogram Kumulatif Data Survei-----
# # Buat figure sebagai canvas dengan ukuran 8 in x 6 in
# fig, ax = plt.subplots(figsize=(8, 6))
# # plotkan histogram untuk frekuensi 
# sns.histplot(x=tinggi_badan, binwidth=1, binrange=(tinggi_badan.min()-0.5, tinggi_badan.max()+0.5), cumulative=True, ec="w", ax=ax)
# # buat sumbu berikutnya agar frekuensi relatif dapat dijadikann pada satu plot
# ax1 = ax.twinx()
# # plotkan histogram untuk frekuensi relatif
# sns.histplot(x=tinggi_badan, stat="probability", binwidth=1, binrange=(tinggi_badan.min()-0.5, tinggi_badan.max()+0.5), cumulative=True, kde=True, ec="w", ax=ax1)
# # set label
# ax.set_xlabel("Tinggi badan (cm)", fontsize=12) 
# ax.set_ylabel("Frekuensi kumulatif", fontsize=12)
# ax1.set_ylabel("Probabilitas kumulatif", fontsize=12)
# ax1.grid(axis="y")
# plt.tight_layout()
# plt.show()

# -----Visualisasi Empirical CDF Data Survei-----
# # Buat figure sebagai canvas dengan ukuran 8 in x 6 in
# fig, ax = plt.subplots(figsize=(8, 6))
# # plotkan ecdf
# sns.ecdfplot(x=tinggi_badan, ax=ax)
# # plotkan ecdf komplemen
# sns.ecdfplot(x=tinggi_badan, complementary=True, ax=ax)
# # set label
# ax.set_xlabel("Tinggi badan (cm)", fontsize=12)
# ax.set_ylabel("Probabilitas kumulatif", fontsize=12)
# ax.grid(axis="y")
# plt.legend(["ecdf", "ecdf komplemen"], fontsize=12)
# plt.tight_layout()
# plt.show()

# -----Menampilkan Dua Kurva: PDF dan CDF-----