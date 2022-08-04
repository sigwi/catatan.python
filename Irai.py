import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

df=pd.read_excel("D:\LATIHAN PANDAS SUMBER DATA\Tes Irai.xlsx", "CPO2")
supply=df['Total Supply mmTon']
features=df[['World GDP Quadrillion', 'Population Billion']]
X_train,X_test,Y_train,Y_test=train_test_split(features, supply,test_size=0.2, random_state=10)
regr=LinearRegression()
regr.fit(X_train,Y_train)
print('Intercept :', regr.intercept_)
print(pd.DataFrame(data=regr.coef_,index=X_train.columns, columns=['Koefisien']))
print('R-squared dari Train :', regr.score(X_train,Y_train))
print('R-squared dari Test :', regr.score(X_test,Y_test))

X_incl_const=sm.add_constant(X_train)
model=sm.OLS(Y_train,X_incl_const)
results=model.fit()

corr=round(Y_train.corr(results.fittedvalues), 2)
print('Correlation:', round(corr, 2))
print('Tes irai Sigit Wiendarto')

plt.scatter(x=Y_train,y=results.fittedvalues, color='blue', alpha=0.4, label='Supply')
plt.title('Real Supply vs Prediction Supply of CPO\n'+'By Sigit Wiendarto')
plt.xlabel('Real (Million Metric Ton)')
plt.ylabel('Prediction (Million Metric Ton)')
plt.plot(Y_train,Y_train, color='purple', alpha=0.5, label='Perfect Fit')
plt.legend()

plt.show()

# df1=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\Thai GDP.csv", skiprows=3, sep=',', header=None, engine='python', error_bad_lines=False)
# df1.rename(columns=df1.iloc[0], inplace=True)
# df1.drop(df1.index[0], inplace=True)
# # df1.set_index(df1.iloc[:,0], inplace=True)
# # df1.reset_index(drop=True, inplace=True)
# df1.drop(['Country Name', 'Country Code'], axis=1, inplace=True)
# print(df1.loc[106,])

# df=pd.read_excel("D:\LATIHAN PANDAS SUMBER DATA\Tes Irai.xlsx", "GDP2")
# print(df.describe())
# x=df['Year']
# y1=df["Thailand"]
# y2=df["Indonesia"]
# plt.plot(x,y1, color='blue', alpha=0.8, label='Thailand')
# plt.xlabel('Year')
# plt.ylabel('in billions')
# plt.plot(x,y2,color='red', alpha=0.8, label='Indonesia')
# plt.legend(loc='upper left',bbox_to_anchor=(1,1))

