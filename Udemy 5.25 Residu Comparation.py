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
features=data.drop(['PRICE', 'INDUS', 'AGE'], axis=1)

X_train,X_test,Y_train,Y_test=train_test_split(features, prices,test_size=0.2, random_state=10)

X_incl_const=sm.add_constant(X_train)
model=sm.OLS(Y_train,X_incl_const)
results=model.fit()

# print('residual :',Y_train-results.fittedvalues) #cara 1 ngitung residual
# print(results.resid) #cara 2 ngitung residual
corr=round(Y_train.corr(results.fittedvalues), 2) #fittedvalues adalah Y predicted value (setelah drop AGE & INDUS)
print('Nilai Corr (Y & Y dg drop INDUS, AGE):', round(corr, 2))
plt.figure(figsize=[10,4])
plt.subplot(1,2,1)
plt.scatter(x=Y_train,y=results.fittedvalues, alpha=0.2)
plt.title('Log Price')
plt.xlabel('real')
plt.ylabel('prediction')
plt.plot(Y_train,Y_train, color='red')
plt.subplot(1,2,2)
plt.scatter(x=np.e**Y_train,y=np.e**results.fittedvalues, alpha=0.2, color='purple')
plt.title('Real Price')
plt.xlabel('real')
plt.ylabel('prediction')
plt.plot(np.e**Y_train,np.e**Y_train, color='red')
plt.show()