import numpy as np
import matplotlib.pyplot as plt
from math import log

def f(x,y):
    r=3**(-x**2-y**2)
    return  1/(r+1)
def fpx(x,y): #turunan parsial
    r=3**(-x**2-y**2)
    return 2*x*log(3)*r/(r+1)**2
def fpy(x,y): #turunan parsial
    r=3**(-x**2-y**2)
    return 2*y*log(3)*r/(r+1)**2
x_4=np.linspace(-2,2,200)
y_4=np.linspace(-2,2,200)
x_4,y_4=np.meshgrid(x_4,y_4) #jadi kayak matrix/2dimension

multiplier=0.1
max_iter=500
params=np.array([1.8,1]) #ini adalah tebakan titik pertama, shape nya adalah (2,) 1Dimension(1row doang) yaitu tuple
                        #() ini tuple, ([]) ini list
values_array=params.reshape(1,2) #setelah reshape jadi (1,2) 2Dimension(1row,1column)
for n in range (max_iter):
    gradient_x= fpx(params[0],params[1]) #turunan ini nilainya nanti masuk ke gradients>params
    gradient_y = fpy(params[0],params[1])
    gradients=np.array([gradient_x,gradient_y])
    params=params-multiplier*gradients
    values_array=np.append(values_array, params.reshape(1,2), axis=0) #pakai np karena multidimensi/2kolom n bbrp row
                                                                    #menambah nilai utk dijadikan axis di graph
                                                                    #setelah diappend bentuknya akanseperti ini
                                                                    #([[row0col0,r1c0,r2c0,..],[row0col1,r1c1,r2c1],..)
fig=plt.figure(figsize=[8,5]) #seting ukuran grafik
ax=fig.gca(projection='3d') #seting axis
ax.plot_surface(x_4,y_4,f(x_4,y_4), cmap='winter', alpha=0.6) #cmap=plasma,viridis, inferno, magma, summer, winter, spring, autumn, cool
ax.scatter(values_array[:,0],values_array[:,1],f(values_array[:,0],values_array[:,1]),color='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)-Cost')

judul1= r'$(x,y)=\frac{1}{3^{-x^2-y^2}+1}$'+'\n'
judul2= r'$(x,y)=\frac{1}{r+1}$'+'\n'
judul3= "Dimana :" r'$r={3^{-x^2-y^2}}$'
plt.title(judul1+judul2+judul3)
plt.show()
print('value in gradient array', gradients)
print('minimum occurs at x value of:', params[0])
print('minimum occurs at y value of:', params[1])
print('the cost is:', f(params[0],params[1]))