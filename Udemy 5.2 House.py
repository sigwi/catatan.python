from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

boston_dataset=load_boston()
data=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)

# print(dir(boston_dataset)) #ngecek nama kolom
# print(data.shape) #hitung berapa baris dan kolom
# print(boston_dataset.DESCR) #ngecek description
# print(data.count()) #hitung berapa baris
data ['PRICE'] = boston_dataset.target
# print(data ['PRICE'])
# print(data.head())
# print(data.describe())
# print(data['PRICE'].corr(data['RM'])) #mencari korelasi antara jumlah kamar & harga
# print(data.corr()) #semua
# plt.hist(data ['PRICE'], bins=50, ec='black', color='#2196f3') #fungsi bins = membagi data/bins. Warna ambil dr materialpallete.com
# plt.xlabel('Harga in 1000')
# plt.ylabel('Jumlah Rumah')

# plt.hist(data['RM'])

#============4.11 Data Corelation Visualization============
# mask=np.zeros_like(data.corr())
# triangle_indices=np.triu_indices_from(mask)
# mask[triangle_indices]=True
# plt.figure(figsize=(10,5))
# # pal = sns.color_palette("RdBu") #blm bisa, jgn dipakai
# sns.heatmap(data.corr(), mask=mask, annot=True) #mask bikin duplikat ilang, annot=nilai ditayangkan d kotak

#============4.12============
# nox_dis_corr=round(data['NOX'].corr(data['DIS']), 2)
# plt.scatter(x=data['DIS'], y=data['NOX'], color='blue', alpha=0.5)
# plt.title(f'NOX vs DIS (correlation ={nox_dis_corr})')
# plt.xlabel('Distance')
# plt.ylabel('Polusi NOX')

#===========4.14===========
# tax_rad_corr=round(data['TAX'].corr(data['RAD']), 2)
# sns.set()
# sns.set_context('talk')
# sns.set_style('whitegrid')
# sns.jointplot(x=data['TAX'], y=data['RAD'], color='indigo', joint_kws={'alpha':0.5})
# plt.title(f'NOX vs DIS (correlation ={tax_rad_corr})')
#========================
# sns.lmplot(x='TAX', y='RAD', data=data, size=5) #menggambar garis
#========================
# sns.pairplot(data) #ini run semua, berat
# sns.pairplot(data, kind='reg', plot_kws={'line_kws':{'color':'cyan'}}) #kind=tambah garis. plot_kws=warna garis

# plt.show()