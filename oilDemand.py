import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel("D:\Oil Demand\Population & GDP.xlsx", "tableau")
target=df['Oil Demand (kBpd)']
variabel=df[['GDP (Trillion)', 'Population (Billion)']]

X_train,X_test,Y_train,Y_test=train_test_split(variabel, target,test_size=0.3, random_state=10)

regr=LinearRegression()
regr.fit(X_train,Y_train)

print('Intercept :', regr.intercept_)
print(pd.DataFrame(data=regr.coef_,index=X_train.columns, columns=['Coefficient']))
print('Train R-squared :', regr.score(X_train,Y_train))
print('Test R-squared :', regr.score(X_test,Y_test))

X_incl_const=sm.add_constant(X_train)
model=sm.OLS(Y_train,X_incl_const)
results=model.fit()

corr=round(Y_train.corr(results.fittedvalues), 2)
print('Correlation:', round(corr, 2))
print('By Sigit Wiendarto')

plt.scatter(x=Y_train,y=results.fittedvalues, label='Oil Demand',alpha=0.5, color='purple')
plt.title('Real data vs Model of oil demand (1960-2020)')
plt.xlabel('Real Historical Data')
plt.ylabel('Model')
plt.plot(Y_train,Y_train, color='green', alpha=0.5, label='Perfect Fit')
plt.legend()
plt.show()