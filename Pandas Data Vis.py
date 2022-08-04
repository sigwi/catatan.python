import pandas as pd
import matplotlib.pyplot as plt
# plt.style.use('ggplot')

#-------CARA 1 MEMBUAT KOLOM TANPA NAMA MENJADI INDEX-----------
# df1=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\df1.csv")
# print(df1)
# df1.set_index(df1.iloc[:,0], inplace=True) #menjadikan kolom tanpa nama menjadi index
# print(df1)
# df1.drop(df1.columns[df1.columns.str.contains('unnamed',case=False)], axis=1,inplace=True) #menghapus kolom tanpa nama
# print(df1)
# df1.index.name="dates" #mengubah nama pada index
# print(df1)
#-------CARA 2 MEMBUAT KOLOM TANPA NAMA MENJADI INDEX, PAKAI (index_col=0) pada saat loading file--------
# df1=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\df1.csv", index_col=0)
# plt.style.use('ggplot')
# print(df1)
# df1['a'].hist()
# plt.show()

df2=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\df2.csv")
print(df2)
# df2.plot.area(alpha=0.8)
# df2.plot.bar()
# df2.plot.bar(stacked=True)
# df2.plot.line(y='b', figsize=(9,3),lw=1) #figsize adalah luas kotaknya, lw adalah tebal garis
# df2.plot.scatter(x='a',y='d') #sistem koordinat (x,y), ditentukan dulu mana yg jd x mana yg jd y
# df2.plot.scatter(x='a',y='d',c='c', cmap='coolwarm') #3 parameter, parameter ke3/c adalah warna
# df2.plot.scatter(x='a',y='d', s=df2['c']*1000) #parameter ke-s adalah besarnya bulatan
# df2.plot.box()
# df2.plot.hexbin(x='a',y='b',gridsize=10,cmap='Blues') #cmap-nya ditambah "s", warna+s
# df2['a'].plot.kde() #pake scipy
# df2.plot.density() #pake scipy
plt.show()

