import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

x_5=np.array([[1.2,1.8,2.2,3.2,4,3.5]]).transpose() #kl mau tranpose braket kotak harus dobel
y_5=np.array([1.1,2.4,3.3,3.5,4.9,3.7]).reshape(6,1) #d reshape n transpose biar bentuknya sama dengan data d bawah

def mse(y,y_hat):
    mse_calc = (1 / y.size) * sum((y - y_hat) ** 2) #ini rumus mse
    return mse_calc

nr_thetas=100 #jumlah theta
th_0=np.linspace(-1,3,nr_thetas)
th_1=np.linspace(-1,3,nr_thetas)
plot_t0,plot_t1=np.meshgrid(th_0,th_1) #meshgrid keluar jd tupel, ini yg dipakai di grafik, bukan th_, krn bentuk
                                    # #konfigurasi index ke 0 jd baris utk yg pertama, kolom utk yg kedua

plot_cost=np.zeros((nr_thetas, nr_thetas)) #ini diisi dari yg d dalam loop
for i in range (nr_thetas): #ini namanya nested loop
    for j in range (nr_thetas):
        y_hat=plot_t0[i][j]+plot_t1[i][j]*x_5 #tujuan [i][j] atau [j][i]  mainin urutan saja dg memanfaatkan loc, hasil sama
        plot_cost[i][j]=mse(y_5,y_hat) #tadi di 0 kan dulu baru diisi nilainya MSE disini
                                    #bisa pakai fungsi atau langsung pakai 'mean_squared_error' dari sklearn
                                    #isi plot cost adalah hasil hitungan mse, sesuai koordinat ij
        # print(f'i:{i}, j:{j}')
# print('plot cost', plot_cost) #disini plot cost sudah tidak 0 lg
print('shape of th_0:', plot_t0.shape)
print('shape of th_1:', plot_t1.shape)
print('shape of plot_cost:', plot_cost.shape)

fig=plt.figure(figsize=[8,5]) #seting ukuran grafik
ax=fig.gca(projection='3d') #seting axis

ax.set_xlabel(r'$ \Theta 0$')
ax.set_ylabel(r'$ \Theta 1$')
ax.set_zlabel('Besar Error (MSE)')

judul= r'$ MSE = \frac{1}{n} \Sigma (\Theta 0 + \Theta 1.x)^2$'
judul1='Besar Error'
plt.title(judul1+'\n'+judul)

ax.plot_surface(plot_t0,plot_t1,plot_cost, cmap='rainbow', alpha=0.5) #ini yg dipakai plotting


#==============4.22==============
def grad (x,y,tethas): #turunan parsial untuk ngisi tethas melalui for loop, tethas ini adlh GradDescent
    n=y.size
    tetha0_slope = (-2 / n) * sum(y - tethas[0] - tethas[1] * x)
    tetha1_slope = (-2 / n) * sum((y - tethas[0] - tethas[1] * x)*x)
    # return np.array([tetha0_slope,tetha1_slope])
    return np.append(arr=tetha0_slope, values=tetha1_slope)
    # return np.concatenate((tetha0_slope, tetha1_slope), axis=0)

multiplier=0.01
tethas = np.array([2.9,2.9]) #titik awal iterasi, nanti dikurangi hasil dari fungsi GRAD
plot_vals=tethas.reshape(1,2) #tadinya berbentuk 1D
mse_vals=mse(y_5,tethas[0]+tethas[1]*x_5)

for i in range (500):
    tethas = tethas-multiplier*grad(x_5,y_5,tethas) #hasil penurunan dikalikan multiplier sebagai pengurang tethas
                                                    #sehingga hasilnya akan konvergen d suatu titik
    plot_vals=np.concatenate((plot_vals,tethas.reshape(1,2)), axis=0) #buat nambahi data
    mse_vals=np.append(arr=mse_vals, values=mse(y_5,tethas[0]+tethas[1]*x_5)) #buat nambahi data

print('Nilai tetha 0 :', tethas[0])
print('Nilai tetha 1 :', tethas[1])
print('Nilai MSE:',mean_squared_error(y_5, tethas[0]+tethas[1]*x_5))
# print('mse val',mse_vals)
# print(plot_vals)
ax.scatter(plot_vals[:,0],plot_vals[:,1],mse_vals) #turunan parsial digunakan untuk mencari axis dari tethas,
                                                #sementara di grafik nilai Z diperoleh dari memasukkan tethas k MSE
plt.show()