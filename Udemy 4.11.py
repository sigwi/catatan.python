import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D #kalau jupiter pakai, phycarm kok engga y
from sympy import symbols, diff

def f(x,y):
    r=3**(-x**2-y**2)
    return  1/(r+1)
x_4=np.linspace(-2,2,200)
y_4=np.linspace(-2,2,200)
# print(x_4,y_4)
x_4,y_4=np.meshgrid(x_4,y_4) #jadi kayak matrix
# print(x_4,y_4)

#generate graph
fig=plt.figure(figsize=[8,5]) #seting ukuran grafik
ax=fig.gca(projection='3d') #seting axis
ax.plot_surface(x_4,y_4,f(x_4,y_4), cmap='winter', alpha=0.6) #cmap=plasma,viridis, inferno, magma, summer, winter, spring, autumn, cool

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)-Cost')

judul1= r'$(x,y)=\frac{1}{3^{-x^2-y^2}+1}$'+'\n'
judul2= r'$(x,y)=\frac{1}{r+1}$'+'\n'
judul3= "Dimana :" r'$r={3^{-x^2-y^2}}$'
plt.title(judul1+judul2+judul3)
# plt.show()

#========================BAB 4.12========================
a,b=symbols('x,y')
print('Nilai f(x,y) :', f(a,b))
print(' Nilai turunan parsial thd X :', diff(f(a,b), a))
print(' Nilai f(x,y) pada x=1.8 & y=1 :', f(a,b).evalf(subs={a:1.8,b:1}))

#=======================BAB 4.13========================
multiplier=0.1
max_iter=200
params=np.array([1.8,1])

for n in range (max_iter):
    gradient_x=diff(f(a,b), a).evalf(subs={a:params[0],b:params[1]})
    gradient_y = diff(f(a, b), b).evalf(subs={a: params[0], b: params[1]})
    gradients=np.array([gradient_x,gradient_y])
    params=params-multiplier*gradients
    print(n, params)

print('value in gradient array', gradients)
print('minimum occurs at x value of:', params[0])
print('minimum occurs at y value of:', params[1])
print('the cost is:', f(params[0],params[1]))

