import matplotlib.pyplot as plt
import numpy as np

def sinGenerator (amplitudo, frekuensi, tAkhir, sudut):
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t + np.deg2rad(sudut))
    return t,y

amplitudo = 1
frekuensi = 1
tAkhir = 7
sudut = 0

t,y = sinGenerator(amplitudo, frekuensi, tAkhir, sudut)
#plot
plt.plot(t,y,label='sin 0') #label disini adalah nama legend-nya
plt.legend(loc='lower right', bbox_to_anchor=(1,1)) #bbox (0,0) pojok kiri bawah (1,1) pojok kanan atas

#set label dan title
judul='Grafik Sinusoidal\n'
rumus=r'$ \mathcal{Y} = \mathcal{A}.sin( \omega t + \theta ) $' +'\n'
parameter = r'$ A = $' + str(amplitudo) + r'$ \mathit {cm},  $' + '\n' #mathit = italic
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit {Hz},  $' + '\n'
parameter3 = r'$ \theta = $' +str(sudut) + r'$ ^{o} $'

plt.title(judul+rumus+parameter+parameter2+parameter3)

plt.xlabel('sudut (rad)')
plt.ylabel(r'$ \mathcal{daya (watt)} $')
#show
plt.show()