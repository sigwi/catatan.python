import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

x_5=np.array([[1.2,1.8,2.2,3.2,4,3.5]]).transpose() #kl mau tranpose braket kotak harus dobel
y_5=np.array([1.1,2.4,3.3,3.5,4.9,3.7]).reshape(6,1)

print('bentuk x:',x_5.shape)
print('bentuk x:',y_5.shape)

regr=linear_model.LinearRegression()
regr.fit(x_5,y_5)
print('theta 0:', regr.intercept_[0]) #Koefisien C
print('theta 1:', regr.coef_[0][0]) #Slope atau m

plt.scatter(x_5,y_5,s=50)
plt.plot(x_5,regr.predict(x_5))
plt.show()

y_hat=0.18876595744680857+1.1174468085106384*x_5
# print('y hat :\n', y_hat)
# print('sbg bahan perbandingan y :\n', y_5)

def mse(y,y_hat):
    mse_calc=(1/y.size)*sum((y-y_hat)**2) #ini rumus mse
    return mse_calc
print('mse manual adalah:', mse(y_5,y_hat))
print('mse dari package:', mean_squared_error(y_5,y_hat))
print('mse dari package dan regr.predict:', mean_squared_error(y_5,regr.predict(x_5)))


