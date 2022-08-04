import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return x**4-4*x**2+5
def dg(x):
    return 4*x**3-8*x

def gradient_descent (derivative_func, initial_guess, multiplier, precision, max_iter):
    new_x=initial_guess
    x_list=[new_x]
    slope_list=[derivative_func(new_x)]
    for n in range (max_iter):
        previous_x=new_x
        gradient=derivative_func(previous_x)
        new_x=previous_x-multiplier*gradient #loopBaru
        print('x baru =', n,new_x)
        step_size=abs(previous_x-new_x)
        x_list.append(new_x) #setiap loopBaru dari new_x ditambahkan ke x_list
        slope_list.append(derivative_func(new_x))
        if step_size<precision:
            break
    return new_x, x_list, slope_list #hasil dari fungsi, ini bentuknya tuple
n=100

low_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.0005,precision=0.0001, max_iter=n)
mid_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.001,precision=0.0001, max_iter=n)
high_gamma = gradient_descent(derivative_func=dg, initial_guess=3, multiplier=0.002,precision=0.0001, max_iter=n)

plt.figure(figsize=[8,4])

plt.xlim(0,n)
plt.ylim(0,50)

plt.title('Effect of learning rate' )
plt.xlabel('Number of iteration n')
plt.ylabel('Cost/Y dari nilai X yg terus konvergen')
#v==========value for chart===============
# 1. Y axis value
low_value=np.array(low_gamma[1])
# 2. X axis value
iteration_list = list(range(0,n+1))
#low gamma
plt.plot(iteration_list,g(low_value),color='lightgreen', alpha=0.5)
plt.scatter(iteration_list,g(low_value),color='lightgreen', s=10, alpha=0.5, cmap='coolwarm')
#mid gamma
mid_value=np.array(mid_gamma[1])
plt.plot(iteration_list,g(mid_value),color='skyblue', alpha=0.5)
plt.scatter(iteration_list,g(mid_value),color='skyblue', s=10, alpha=0.5, cmap='coolwarm')
#high gamma
high_value=np.array(high_gamma[1])
plt.plot(iteration_list,g(high_value),color='hotpink', alpha=0.5)
plt.scatter(iteration_list,g(high_value),color='hotpink', s=10, alpha=0.5, cmap='coolwarm')

plt.show()