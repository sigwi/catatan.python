import pandas as pd
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam', 'Amy','Rick','James','Batman','Joker'],
        'Sales':[200,350,100,400,200,320]}

df = pd.DataFrame(data)
print(df)

#nge grup in
by_comp = df.groupby("Company")
# a = by_comp.mean()
# print(a)
b = df.groupby('Company').mean() #bentuk lain yg lebih ringkas daripada diatas
print(b)

#deskripsi mean std max etc
a = by_comp.describe()
print(a)

#transpose
a = by_comp.describe().transpose()
print(a)
a = by_comp.describe().transpose()["GOOG"] #transpose spesifik
print(a)
# pd.merge
