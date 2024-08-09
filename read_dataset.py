import pandas as pd
import mysql.connector as sql

# -----csv dan tsv
df_csv = pd.read_csv(' https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')
print(df_csv.head(3)) # Menampilkan 3 data teratas
df_tsv = pd.read_csv(' https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv', sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

# -----Excel-----
# # File xlsx dengan data di sheet "test"
# df_excel = pd.read_excel("https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx", sheet_name="test")
# print(df_excel.head(4)) # Menampilkan 4 data teratas

# -----JSON----
url = "https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json" # File JSON
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas

# ----SQL-----
# my_conn=sql.connect(
#   host="relational.fit.cvut.cz",
#   port=3306,
#   user="guest",
#   passwd='relational',
#   database='financial',
#   use_pure=True
# )
# my_query="SELECT * FROM loan"
# df_loan=pd.read_sql_query(my_query,my_conn) # atau
# df_loan=pd.read_sql(my_query,my_conn) 
# print(df_loan.head())

# -----Google BigQuery-----
# my_query="SELECT * FROM `bigquery-public-data.covid19_jhu_csse_eu.summary` LIMIT 1000"
# df_covid19_summary=pd.read_gbq(my_query,project_id="xxxxx") #=> project_id="XXXXXXXX" adalah ID dari Google BigQuery account.

# -----Head and Tail-----
# method .head yang diterapkan pada suatu variabel bertipe pandas dataframe/series. Method .head ditujukan untuk membatasi tampilan jumlah baris teratas dari dataset. Sementara itu, method .tail ditujukan untuk membatasi jumlah baris terbawah dari dataset.

