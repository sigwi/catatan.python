import numpy as np

a=np.array([1])
b=np.array([0])
for i in range (3):
    a=a+1
    print('a =',a)
    b=np.append(a,b,axis=0)
    print('b =',b)
print(a)
print(b)

