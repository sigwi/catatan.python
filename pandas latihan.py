import pandas as pd
import numpy as np

# Latihan SERIES
# labels = ['a','b','c','d']
# my_list = [10,23,20,39]
arr = np.array ([10,23,20,39])
# d = {'a':10, 'b':23, 'c':20, 'd':39}
# x = pd.Series(data=my_list)
# x = pd.Series(data=my_list,index=labels) #kiri datanya, kanan index
# x = pd.Series(my_list, labels)
x = pd.Series(arr) #data harus 1 dimensi, tidak bisa lebih
# x = pd.Series(arr,labels)
# x = pd.Series(d)
# x = pd.Series(data=labels)
print(x)
# x = pd.Series([sum,print,len])
# print(x)
# ser1=pd.Series([1,2,4],index=['USA', 'JPN', 'SING'])
# print(ser1)
# ser2=pd.Series([1,2,5],index=['USA', 'JPN', 'INA'])
# print(ser1+ser2)
# print(ser2['JPN'])
# print(ser2[['JPN','USA']])

#Membuat DATA FRAME
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,5),index='A B C D E'.split(),columns='V W X Y Z'.split())

#Indexing/memanggil data berdasar nama kolom
# print(df)
# print(df['W'])
# print(df[['W', 'Z']])
# print(df.W)
# type(df['W'])

#menambah kolom, menghapus kolom/baris
# df['New'] = df['W'] + df ['Z']
# print(df)
# df.drop('New',axis=1,inplace=True) #axis= 0/'index' (untuk baris), 1/'labels' (untuk kolom)
# df.drop('W',axis=1,inplace=True)
# print(df)
# df.drop('D',axis=0,inplace=True)
# print(df)

#menambah index baru dengan nama sesuai selera
newstates='CA NY LA IN DX'.split()
print(newstates)
df['States']=newstates
print(df)
df.set_index('States',inplace=True) #inplace untuk mengganti secara permanen
print(df)
