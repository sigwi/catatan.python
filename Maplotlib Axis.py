import matplotlib.pyplot as plt
import numpy as np
#rumus sinus pakai derajat
x = np.linspace(0,360,1000)
y = np.sin(np.deg2rad(x))
y2 = np.cos(np.deg2rad(x))

#set plot reposisi
plt.figure(1) #nama pop up grafik
ax=plt.subplot(111) #plotnya
    #plot ditengah fungsi ini
plot1 = plt.plot(x,y)
plot2 = plt.plot(x,y2)
plt.setp(plot1,label=r'$sin \theta$',color='r',linestyle='--',linewidth=1)
plt.setp(plot2,label=r'$cos \theta$',color='b',linestyle='-.',linewidth=0.5)

box=ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height*0.9]) #angka hasil box.width*0.8, box.height*0.9 = 1 dikali selera
plt.legend(loc='upper center',bbox_to_anchor=(1.2,1)) #atur posisi legend

#set label dan title
judul='Trigonometri\n'
plt.title(judul)
plt.xlabel('sudut')
plt.ylabel('daya (watt)')

#set ticks/bentuk angka sumbu
plt.yticks([-1,0,0.5,1])
plt.xticks([0,90,180,270,360],[r'${0}^o$',r'${90}^o$',r'${180}^o$',r'$270}^o$',r'${360}^o$'])

#set spines
bx=plt.gca()
# bx.spines['left'].set_position(('data',180))
# bx.spines['bottom'].set_position(('data',0))
bx.spines['right'].set_color('none')
bx.spines['top'].set_color('none')


plt.show()