import matplotlib.pyplot as plt
import numpy as np
# x = np.linspace(0, 5, 100) #(Titik mulai, titik akhir, increment)
# y = x ** 2
# y2 = np.sin(x) #default bentuk sudutnya radian
# print (x)
# print (y)
# print (y2)
#
# plt.plot(x,y,'g') #paling belakang kode warna
# plt.plot(x,y2)
# plt.xlabel('ini X (rad)')
# plt.ylabel('ini Y')
# plt.title('Percobaan Bikin Matplotlib')
# plt.show()

#Bikin data dulu
def sinGenerator (amplitudo, frekuensi, tAkhir, sudut):
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t + np.deg2rad(sudut))
    return t,y
#bikin plot
# t1,y1 = sinGenerator (1,1,5,0)
# plt.plot(t1,y1,'r')
#
# t2,y2 = sinGenerator (1,1,3,90)
# plt.plot(t2,y2,'g--')
#
# t3,y3 = sinGenerator (1,2,5,180)
# plt.plot(t3,y3,'b,')

t1,y1 = sinGenerator (1,1,5,0)
t2,y2 = sinGenerator (1,1,5,90)
t3,y3 = sinGenerator (1,1,5,180)

#dengan plot agar lebih rapi
plot1 = plt.plot(t1,y1)
plot2 = plt.plot(t2,y2)
plot3 = plt.plot(t3,y3)

#setting properties
plt.setp(plot1,color='r',linestyle='--',linewidth=2)
plt.setp(plot2,color='b',linestyle='-.',linewidth=1)
plt.setp(plot3,color='g',linestyle='-',linewidth=0.5)

#axis
plt.axis([-1,6,-1.5,1.5]) #utk set besarnya kotak cartesian

#show
plt.show()