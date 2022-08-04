import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return x**5-2*x**4+2
def dg(x):
    return 5*x**4-8*x**3

x_2=np.linspace(-1,2,1000)

def gradient_descent (derivative_func, initial_guess, multiplier, precision, max_iter=5):
    new_x=initial_guess
    x_list=[new_x]
    slope_list=[derivative_func(new_x)]
    for n in range (max_iter):
        previous_x=new_x
        gradient=derivative_func(previous_x)
        new_x=previous_x-multiplier*gradient
        print('x baru =', n,new_x)
        step_size=abs(previous_x-new_x)
        x_list.append(new_x) #setiap loop baru dari new_x ditambahkan ke x_list
        slope_list.append(derivative_func(new_x))
        if step_size<precision:
            break
    return new_x, x_list, slope_list #hasil dari fungsi
local_min, list_x, deriv_list = gradient_descent(derivative_func=dg, initial_guess=-0.5, multiplier=0.02, precision=0.01) #hasil return diatas urutannya sama, kemudian isi variabel dalam fungsi urutannya jg sama
print('our local minimum', local_min)
print('cost at this poin is', g(local_min))
print('number of steps', len(list_x))

plt.figure(figsize=[10,4]) #=====>  (1)
plt.subplot(1,2,1) #=====> isinya (row,column,index) (2)
plt.plot(x_2,g(x_2), alpha=0.5)
# values=np.array(x_list)
plt.scatter(list_x,g(np.array(list_x)),color='red', s=50, alpha=0.5, cmap='coolwarm')
rumus1=r'$g=x^4-4x^2+5$'
plt.title('GRAFIKNYA\n'+ rumus1 )
plt.xlabel(r'$x$')
plt.ylabel(r'$g(x)$')

plt.subplot(1,2,2) #=====> (3)
rumus2=r'$dg=4x^3-8x$'
plt.plot(x_2,dg(x_2),color='skyblue', alpha=0.5)

plt.scatter(list_x, deriv_list,color='red', s=50, alpha=0.5, cmap='coolwarm')
plt.title('TURUNANNYA\n'+ rumus2)
plt.xlabel(r'$x$')
plt.ylabel(r'$d(g(x))$')
plt.show()