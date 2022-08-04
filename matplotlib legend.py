import matplotlib.pyplot as plt
import numpy as np

def sinGenerator (amplitudo, frekuensi, tAkhir, sudut):
    t = np.arange(0,tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t + np.deg2rad(sudut))
    return t,y

t1,y1 = sinGenerator (1,1,5,0)
t2,y2 = sinGenerator (1,1,5,90)

#tipe pertama
# plt.plot(t1,y1,label='sin 0')
# plt.plot(t2,y2,label='sin 90')
# plt.legend()

#tipe kedua
# plt.plot(t1,y1,label='sin 0')
# plt.plot(t2,y2,label='sin 90')
# plt.legend(loc='upper center')

#tipe ketiga
# plt.plot(t1,y1,label='sin 0')
# plt.plot(t2,y2,label='sin 90')
# plt.legend(loc='upper center',bbox_to_anchor=(1,1)) #bbox (0,0) pojok kiri bawah (1,1) pojok kanan atas

#tipe keempat
# plt.figure(1) #nama pop up grafik
# ax=plt.subplot(111) #plotnya
#
# plt.plot(t1,y1)
# plt.plot(t2,y2)
#
# box=ax.get_position()
# ax.set_position([box.x0, box.y0, box.width*0.7, box.height]) #angka hasil = 1 dikali selera
# plt.legend(loc='upper center',bbox_to_anchor=(1.2,1)) #atur posisi legend
#------------tipe keempat diatas merupakan bentuk lain yg simpel--------------

plt.figure(1) #nama pop up grafik
ax=plt.subplot(111) #plotnya
    #plot ditengah fungsi ini
plot1 = plt.plot(t1,y1)
plot2 = plt.plot(t2,y2)
plt.setp(plot1,label='sin 0',color='r',linestyle='--',linewidth=2)
plt.setp(plot2,label='sin 90',color='b',linestyle='-.',linewidth=1)

box=ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.9]) #angka hasil box.width*0.8, box.height*0.9 = 1 dikali selera
plt.legend(loc='upper center',bbox_to_anchor=(1.2,1)) #atur posisi legend

# -------------------di bawah ini merupakan setting standar (judul, nama legend, nama garis, angka sumbu)---------------
#set judul dan nama sumbu
judul='Grafik Sinusoidal\n'
rumus=r'$ \mathcal{Y} = A.sin( \omega t + \theta ) $' +'\n'
plt.title(judul+rumus)
plt.xlabel('sudut (rad)')
plt.ylabel('daya (watt)')

#set text/setting nama2 di legend
plt.text(0,1, 'sin 90')
plt.text(1,1, r'$ Y = \mathcal{A}.Sin.\omega.t$')

#set ticks/setting angka2 yg muncul di sumbu
plt.yticks([-1,0,0.5,1])
plt.xticks([1,3,5])
#show
plt.show()