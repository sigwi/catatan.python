import numpy as np

x=np.linspace(1,3,3) #(start,stop,jumlah)
y=np.linspace(5,7,3)
print(x,y)
a,b=np.meshgrid(x,y)
print(a)
print(a[2][2])
print(b)
print(b[2][2])

