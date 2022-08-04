import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2+x+1
x_1=np.linspace(start=-3,stop=3,num=500)

# plt.plot(x_1,f(x_1))
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')

def df(x):
    return 2*x+1

# plt.plot(x_1,d(x_1))

#============BIKIN GRAFIK JEJERAN=============
# plt.figure(figsize=[10,4]) #=====>  (1)
# plt.subplot(1,2,1) #=====> isinya (row,column,index) (2)
# plt.plot(x_1,f(x_1))
# rumus1=r'$y=x^2+x+1$'
# plt.title('GRAFIKNYA\n'+ rumus1 )
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')
#
# plt.subplot(1,2,2) #=====> (3)
# rumus2=r'$dy=2x+1$'
# plt.plot(x_1,df(x_1))
# plt.title('TURUNANNYA\n'+ rumus2)
# plt.xlabel(r'$x$')
# plt.ylabel(r'$d(f(x))$')
# plt.show()

new_x=3
previous_x=0 #attempt value, only matter in the loop
step_multiplier=0.1
precision=0.0001
x_list=[new_x]
slope_list=[df(new_x)]
for n in range (30):
    previous_x=new_x
    gradient=df(previous_x)
    new_x=previous_x-step_multiplier*gradient
    # print('x baru =', n,new_x)
    step_size=abs(previous_x-new_x)
    x_list.append(new_x)
    slope_list.append(df(new_x))
    if step_size<precision:
        print('loop ran this many times', n)
        break
print('lokal minimum terjadi pada', new_x)
print('df(x) di titik ini adalah', df(new_x))
print('nilai y atau cost di titik ini adalah', f(new_x))

#==========Bikin graph isinya 2===========
plt.figure(figsize=[10,4]) #=====>  (1)
plt.subplot(1,2,1) #=====> isinya (row,column,index) (2)
plt.plot(x_1,f(x_1), alpha=0.5)
values=np.array(x_list)
plt.scatter(x_list,f(values),color='red', s=50, alpha=0.5, cmap='coolwarm')
rumus1=r'$y=x^2+x+1$'
plt.title('GRAFIKNYA\n'+ rumus1 )
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

plt.subplot(1,2,2) #=====> (3)
rumus2=r'$dy=2x+1$'
plt.plot(x_1,df(x_1),color='skyblue', alpha=0.5)

plt.scatter(x_list,slope_list,color='red', s=50, alpha=0.5, cmap='coolwarm')
plt.title('TURUNANNYA\n'+ rumus2)
plt.xlabel(r'$x$')
plt.ylabel(r'$d(f(x))$')
plt.show()