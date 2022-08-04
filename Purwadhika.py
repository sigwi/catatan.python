nama= 'andi'
print(type(nama))
usia= 22
usia= 32
print(type(usia))
jomblo = True
print (type(jomblo))


import math
print(math.pi);
print(math.pow(8,2));
print(math.fabs(-8.2));
print(math.sqrt(64));
# aritmatik
usiaBudi = 3
usiaBudi *= 4
#usiaBudi = usiaBudi * 3
print (usiaBudi)

import math
print(round(4.5))
print(round(4.4))
print(math.floor (4.7))
print(math.ceil (4.4))

x = "Halo World"
print(len(x))
print(x.index("d"))
print(x.split())
print(x.lower())
print(x.upper())
print(x.capitalize())

usia = 20
nama = 'asu'
print(usia + usia)
print(nama + ' '+ nama)
print(nama + ' '+ str(usia))

usiaandi = 20
usiaandi %=8
print (usiaandi)

kamp = int(input("Masukkan angka ?"))
kamp %= 2
if kamp == 0 :
    print("angka genap");
else :
    print("angka ganjil");

masa = float(input("masa = "))
tinggi = float(input("tinggi = "))
x = masa / tinggi**2
print (x)
if (x < 18) :
    print ("masa kurang")
elif (x >= 18 and x <= 24.9) :
    print ("bb ideal")
else :
    print ("over")
