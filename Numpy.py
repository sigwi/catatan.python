import numpy as np

#membuat vektor
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,3,4,5])
print(a)
print(b)
#array multidimensi/matrix
c = np.array([(1,2,3),(4,5,6)])
print(c)
#operasi aritmatika numpy
#list phyton
a = [1,2,3,4]
b = [5,6,7,8]
#list numpy
anp = np.array([(1,2,3,4), (4,3,2,1)])
bnp = np.array([(5,6,7,8), (8,7,6,5)])
print (a+b) #penjumlahan list biasa
print (anp+bnp) #penjumlahan numpy
#perkalian matrix (dot product)
a = np.array([(1,2),(3,4)])
b = np.ones((2,2))
c1 = np.dot(a,b)
c2 = a.dot(b)
print(c1)
print(c2)
#transpose matrix
a = np.array([(1,2,3),(4,5,6)])
print(a)
print(a.transpose())
print(np.transpose(a))
print(a.T)
#flatten array
#reshape
#resize
#invers
a = np.array([(1,-1),(1,1)])
a_inv = np.linalg.inv(a)
print(a)
print (a_inv)
print(np.dot(a,a_inv))
#determinan
det_a = np.linalg.det(a)
print(det_a)
print (a_inv.dot(det_a))
#persamaan linear
A = np.array([(1,2),(4,5)])
Y = np.array(([13,1]))
print ("A :")
print(A)
print ("Y :")
print(Y)
A_inv = np.linalg.inv(A)
print ("A inv :")
print(A_inv)
X1 = A_inv.dot(Y)
print ("X = A inv * Y maka X adalah :")
print(X1)
print ("cara lain :")
X2 = np.linalg.solve(A,Y)
print (X2)