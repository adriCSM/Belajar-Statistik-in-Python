import pandas as pd

df=pd.DataFrame([1,2,3,4,5,6])

df.to_csv('csv1.csv',index=False) #=> untuk export dataframe kembali ke csv
df.to_csv("tsv1.tsv", index=False, sep='\t') #=> untuk export dataframe kembali ke tsv

df.to_clipboard() #=> menjadi bahan copy jadi nanti bisa tinggal klik paste di excel atau google sheets
df.to_excel("xlsx1.xlsx", index=False) #=> menjadi file excel

df.to_gbq("temp.test", project_id="XXXXXX", if_exists="fail")

# note:
# temp: nama dataset,
# test: nama table
# if_exists: ketika tabel dengan dataset.table_name yang sama sudah ada, apa action yang ingin dilakukan
# ("fail": tidak melakukan apa-apa,
#  "replace': membuang tabel yang sudah ada dan mengganti yang baru,
#  "append": menambah baris di tabel tersebut dengan data yang baru
# )