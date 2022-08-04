import pandas as pd
import numpy as np
import datetime
d=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\departments.csv")
de=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\dept_emp.csv")
dm=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\dept_manager.csv")
e=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\employees.csv")
s=pd.read_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\salaries.csv")

# TASK 1
gab_1=pd.merge(e,dm,how='inner', on='emp_no')
gab_2=pd.merge(gab_1,d,how='inner', on='dept_no')
gab_3=pd.merge(gab_2,s,how='inner',on='emp_no')

kompak=pd.DataFrame((pd.DatetimeIndex(gab_3['from_date_y']).year,gab_3['dept_name'],gab_3['gender'],gab_3['salary']))
# print(kompak)
data=np.array(kompak).transpose()
# print(data)
ok=pd.DataFrame(data=data,columns=['Year','Department','Gender','Salary'])

ok.drop(ok.index[ok['Year']>2002],inplace=True) #ngedrop berdasar index
# print(ok.index[ok['Year']>2002]) #ini indexnya
# ok.to_csv("D:\LATIHAN PANDAS SUMBER DATA\SQL\Task 1 python 2002.csv", index=False)

# ok.sort_values(by=['Year','Department','Gender'], inplace=True)
# ok.set_index(['Year','Department','Gender'], inplace=True)

# ok.groupby(by=['Year','Department','Gender'],axis=0,level=2)
# ok.groupby(level=1)
# ok.groupby(level=2)
# ok['Salary'].mean()
# ok.groupby(level=2).mean()

# print(ok)
# print(ok.isnull().sum())