import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\Cuaca.csv", parse_dates=["date"])
# print(df)
df.set_index('date', inplace=True) #menetapkan tanggal sebagai index
print(df)
# print(df.isna()) #cek ada yg kosong atau tidak
# print(df['wind speed'].isna()) #cek apakah ada yang kosong (spesifik per kolom tertentu) : boolean
# print(df.fillna("xxx")) #isi data kosong
# print(df.fillna({"wind speed":0,"temperature":0,"Status":"windy"})) #isi data kosong sesuai kolom utk multiple kolom
# print(df['Status'].fillna('new')) #utk isi kolom tertentu, dan ditunjukkan kolom itu saja bila di run
# print(df.fillna(method="ffill")) #mengisi nilai bawahnya, kalau "bfill" kebalikan
# print(df.fillna(method="ffill", axis="columns")) #kl ini ngisi ke kanan, "columns" bisa diganti "1". kl "bfill" kekiri
# print(df.fillna(df.mean())) #yg kosong diisi rata2, hanya utk integer bukan string
# print(df.fillna(df.mean()["temperature"])) #diisi dengan rata2 kolom yang disebutkan
#INTERPOLATION
# tgl=df["date"]
# ws=df["wind speed"]
# t=df["temperature"]
# print(df.interpolate())
# plt.plot(tgl,t)
# plt.plot(tgl,ws)
df.interpolate().plot(title="Linear",grid=1) #linear interpolation
# df.interpolate(method="time").plot(title="Time",grid=1) #time interpolation, lebih smooth garisnya drpd linear
# df.interpolate(method='polynomial',order=2).plot(title="Polynomial",grid=1) #perlu pip SciPy utk metode polinomial
plt.show()