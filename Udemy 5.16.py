from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston_dataset=load_boston()
data=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
data ['PRICE'] = boston_dataset.target #menambah PRICE ke data dari target
#----------------------------------------MULAI PREDICT RUMUS HARGA RUMAH------------------------------------------------
#============split data set, training & tes==============
prices=data['PRICE'] #ini jadi Y nya
features=data.drop('PRICE', axis=1) #karena features termasuk prices, maka di drop karena pake prices diatas. Ini jadi X nya
X_train,X_test,Y_train,Y_test=train_test_split(features, prices,
                                               test_size=0.2, random_state=10) #test_size= features train - features tes
                                                                            #random_states= jenis kocokan, bisa 1 or 0 jg
#============mulai analisa multivariable regression buat ktm tethas train==============
regr=LinearRegression()
regr.fit(X_train,Y_train)

print('Intercept or Coefficient:', regr.intercept_)
# print('Slope (m):', regr.coef_)

    #====biar coefficient rapi dibikin seperti ini====
CoefHargaRumah=pd.DataFrame(data=regr.coef_,index=X_train.columns, columns=['Koefisien']) #langsung print ini jg bisa
print(CoefHargaRumah)
    #====Menghitung R-Squared======
print('R-squared dari Train :', regr.score(X_train,Y_train)) #R-square mendekati 1 semakin benar, 0 byk error
print('R-squared dari Test :', regr.score(X_test,Y_test))
#----------------------------------------OK SIP SELESAI PREDICT RUMUS HARGA RUMAH---------------------------------------
#========4.20 NGE LOG IN HARGA=========
Y_log = np.log(data['PRICE'])
# print(Y_log.head())
# sns.distplot(Y_log)
# plt.title(f'Log price w/ Skew{Y_log.skew()}')
# plt.show()
    #=====Membandingkan LSTAT & PRICE======
sns.lmplot(x='LSTAT',y='PRICE', data=data, scatter_kws={'alpha':0.5}, line_kws={'color':'red', 'alpha':0.5})
    #=====Dengan harga log=====
transformed_data=features #ambil variabel yg sudah dikurangi harga
transformed_data['LOG_PRICE'] = Y_log #pakai harga LOG
sns.lmplot(x='LSTAT',y='LOG_PRICE', data=transformed_data, scatter_kws={'alpha':0.5}, line_kws={'color':'green'})
plt.show()