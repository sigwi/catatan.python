import numpy as np
import pandas as pd
import matplotlib as plt

a = np.array([1,2])

b = a.reshape(1,2)

print(a.shape)
print(b.shape)
for n in range (2):
    a=a+np.array([1,2])
    # tebakan = tebakan + np.array(tebakan[1],tebakan[0])
    print('a =', a)
    b=np.append(b, a.reshape(1,2), axis=0) #axis yg menentukan jadi baris atau kolom
    print('b =', b)
#==========V2============
# c = np.array([1,2])
# d = c
# # print(nilai.shape)
# for n in range (2):
#     c=c+c
#     # tebakan = tebakan + np.array(tebakan[1],tebakan[0])
#     print('c', c)
#     d=np.append(d, c, axis=0)
#     print('d dalam loop', d)
# print('d luar loop',d)
#n============ested loop practice============
# for i in range (3):
#     for j in range(3):
#         print(f'ini adalah i ke {i} dan j ke {j}') #pakai f sebelum tanda petik string
