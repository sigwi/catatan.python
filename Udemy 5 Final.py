from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

boston_dataset=load_boston() #(1) loading data
data=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
features=data.drop(['INDUS', 'AGE'], axis=1)
log_prices=np.log(boston_dataset.target) #1D
ylogmatrix=pd.DataFrame(log_prices, columns=['PRICES']) #dari 1D diubah jadi matrix

property_stats=np.ndarray(shape=(1,11)) #bikin frame/kerangka/ibaratnya kertas blank

print(features.mean()) #ini bentuknya series
property_stats=features.mean().values.reshape(1,11) #ini biar jadi matrix/array, pake reshape
RM_IDX=4
PTRATIO_IDX=8
CHAS_IDX=2
CRIME_IDX=0
ZN_IDX=1

regr=LinearRegression()
regr.fit(features, ylogmatrix)
fitted_vals=regr.predict(features) #mrediksi nilai y dari variabel independen
MSE=mean_squared_error(ylogmatrix, fitted_vals)
RMSE=np.sqrt(MSE)

def get_log_estimate (nr_rooms,students_per_classroom, next_to_river=False,high_confidence=True):
    property_stats[0][RM_IDX]=nr_rooms
    property_stats[0][PTRATIO_IDX]=students_per_classroom

    if next_to_river :
        property_stats[0][CHAS_IDX]=1
    else :
        property_stats[0][CHAS_IDX]=0
    log_estimate=regr.predict(property_stats)[0][0]
    if high_confidence:
        upper_bound = log_estimate + 2 * RMSE
        lower_bound = log_estimate - 2 * RMSE
        interval=95
    else:
        upper_bound = log_estimate + 2 * RMSE
        lower_bound = log_estimate - 2 * RMSE
        interval=68
    return log_estimate, upper_bound, lower_bound,interval
print(get_log_estimate(3,20,next_to_river=True,high_confidence=False))
