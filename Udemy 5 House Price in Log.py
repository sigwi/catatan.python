from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston_dataset=load_boston()
data=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
data ['PRICE'] = boston_dataset.target

prices=np.log(data['PRICE'])
features=data.drop('PRICE', axis=1)
X_train,X_test,Y_train,Y_test=train_test_split(features, prices,test_size=0.2, random_state=10)

regr=LinearRegression()
regr.fit(X_train,Y_train)

print('Intercept atau Coefficient:', regr.intercept_)
CoefHargaRumah=pd.DataFrame(data=regr.coef_,index=X_train.columns, columns=['Koefisien']) #langsung print ini jg bisa
print(CoefHargaRumah)

print('R-squared dari Train :', regr.score(X_train,Y_train))
print('R-squared dari Test :', regr.score(X_test,Y_test))

#=============Utk cari nilai sebenarnya maka reverse Log==================
#misal utk ROOM :
room=np.e**0.073404
print('Koefisien real RM :', room)
#============Reverse log nya dibikin tabel (langsung semua muncul)===============
#--->dibikin rumus soalnya kl langsung kl minus malah dibagi
ylog=regr.coef_
newy=()
for i in range (ylog.size):
    if ylog[i] > 0 :
        y=np.e**ylog[i]
    else :
        y=np.e**abs(ylog[i])*-1
    newy=np.append(arr=newy, values=y)

reverselogkoef=pd.DataFrame(data=newy, index=X_train.columns, columns=['Koef Rev Log']) #kekurangan, minus msh salah
print(reverselogkoef)
#tes
print('B',np.e**0.000516)
print('LSTAT', np.e**abs(-0.031390)*-1)
