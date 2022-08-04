from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

boston_dataset=load_boston() #(1) loading data
data=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
data ['PRICE'] = boston_dataset.target
prices=np.log(data['PRICE'])
features=data.drop('PRICE', axis=1)
X_train,X_test,Y_train,Y_test=train_test_split(features, prices,test_size=0.2, random_state=10) #(2) Split
regr=LinearRegression() #(3) Run Regression
regr.fit(X_train,Y_train)

# print('Intercept :', regr.intercept_)
CoefHargaRumah=pd.DataFrame(data=regr.coef_,index=X_train.columns, columns=['Koefisien']) #langsung print ini jg bisa
print(CoefHargaRumah)

#=============hitung P-values============ nilai dibawah 0.05 ok
X_incl_const=sm.add_constant(X_train) #biar tie out sm scikit dikasih intercept
# X_incl_const=X_incl_const.drop(['INDUS','AGE'], axis=1) #p values besar, coba di drop utk lihat pengaruh k bic & R-squared
model=sm.OLS(Y_train,X_incl_const) #Ordinary Least Square (target value, features)
results=model.fit()
# print(pd.DataFrame({'coef':results.params, 'p-values':round(results.pvalues, 3)}))
#=============VIF============== nilai dibawah 10 ok
    #--bentuk 1--
vif=[]
for i in range (X_incl_const.shape[1]):
    vif.append(variance_inflation_factor(exog=X_incl_const.values,exog_idx=i))
    #--bentuk 2--
# vif=[variance_inflation_factor(exog=X_incl_const.values,exog_idx=i) for i in range (X_incl_const.shape[1])]
# print(pd.DataFrame({'coef_name' : X_incl_const.columns, 'vif' : np.around(vif, 2)}))
#============bic (Baysian Information Criterion)=============== Makin kecil makin bagus, utk mengukur model
#setelah model ketemu koef, p values (<0.05), vif(<10). Independen variable coba di drop berdasar nilai p & vif, & diukur pakai bic & R-squared
print(pd.DataFrame({'coef':results.params, 'p-values':round(results.pvalues, 3), 'vif': np.around(vif,2)}))
print('R squared :', results.rsquared) #ambil dari sm.OLS bisa (sm), g perlu regr (scikit)
print('bic :', results.bic)


