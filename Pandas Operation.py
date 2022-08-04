import pandas as pd
import numpy as np
# df = pd.DataFrame ({'Col1':[1,2,3,4], 'Col2': [444,555,666,333], 'Col3': ['asd','sad','qwe','cwt']})
# print(df)
# print(df['Col2'].unique())
# print(df['Col2'].nunique()) #menghitung jumlh total item
# print(df['Col2'].value_counts()) #menghitung jumlah masing2 item
# newdf = df[(df['Col1']>1) & (df['Col2']==444)] #mencari kombinasi dg syarat tertentu, (Empty DataFrame) jika tidak ada
# print(newdf)
# newdf = df[(df['Col1']>1) & (df['Col2']==555)]
# print(newdf)

# #APPLY FUNCTION
def kali2 (x):
    return x*2
# print(df['Col1'].apply(kali2) #memasukkan col1 k rumus
# print(df['Col3'].apply(len)) #menghitung jumlah non huruf, integer tidak bisa pakai len
# print(df['Col1'].sum())
# del df['Col1'] #delete column, mirip ini -> print(df.drop('Col1', axis=1))
# print (df)

# print(df.columns) #tipe kolom
# print(df.index) #tipe index

# print(df.sort_values(by='Col2')) #shorting berdasar nilai, inplace = False by default

df = pd.DataFrame ({'Col1':[1,2,np.nan,np.nan], 'Col2': [444,555,np.nan,333], 'Col3': ['asd',np.nan,'crt','cwt']})
print(df.columns) #nama kolomnya apa
print(df.isnull().sum()) #jumlah data kosong per kolom
print(df.isnull().values.any()) #apakah ada data yang kosong? jawaban hanya 1 : true or flase saja
print(df.isnull().sum().sum()) #jumlah data kosong berapa? jawaban langsung total
print(df.shape)