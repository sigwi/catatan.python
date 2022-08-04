angka = 123
idle = "Integrated Development and Learning Environment"
jumlah = angka + 5
print ("123 + 5 adalah", jumlah)
print ("kepanjangan IDLE adalah", idle)

print ("good \nmorning")
print ("selamat ", end='')
print ("pagi!")
supp = input ("how are you today? ")
print ("nice!", supp)

print ("BEKERJA DENGAN NUMBER")
base_number = 0b10101000
print ("100 binary", base_number)
base_number = 0o1001110011
print ("100 octal", base_number)
base_number = 0x100111111
print ("100 hexadicimal", base_number)

float_number = 255
print ("angka float :", float_number)
float_number = 2.55e2
print ("angka float :", float_number)
float_number = 2.55e-2
print ("angka float :", float_number)

print ("MENGUBAH STRING MENJADI ANGKA DAN SEBALIKNYA")
huruf_a = ord ("a")
print ("huruf a diwakili oleh angka", huruf_a)
angka = int("25")
print ("50 + 25 =", 50 + angka)
teks = str(25)
print ("variable teks bertipe data", type (teks))
print ("OPERATOR LOGIKA")
a = True
b = True
c = False
d = False

print (a and b)
print (a or c)
print (a and c)
print (c and d)
print (c or d)

print (r"FUNCTION")

def morningg (name) :
    print ("Selamat pagi", name)
    print ("semoga harimu menyenangkan!")

morningg ("Ilham")
morningg ("Bintang")
morningg ("Hendsy")

def morningg (name="sobat missqueen") :
    print ("Selamat pagi", name)
    print ("semoga harimu menyenangkan!")

morningg ("Ilham")
morningg ()

def hitungbmi (umur, berat, tinggi) :
    print ("umur :", umur)
    print ("berat :", berat)
    print ("tinggi :", tinggi)
    print ("BMI :", berat / (tinggi * tinggi))

hitungbmi (33, 65, 1.73)
hitungbmi (20, 65, 1.69)
hitungbmi (29, 65, 1.78)
hitungbmi (berat=65, umur=29, tinggi=1.78)

def morningg (*VarArgs):
    print ("Hallo")
    print ("selamat pagi ", end = '')
    for Arg in VarArgs :
        print (Arg, end = '')
morningg ("Joko ", "Erli ", "Budi ")

def hitungbmi (berat, tinggi):
    return berat/(tinggi*tinggi)
print ("BMI anda adalah :", hitungbmi (65, 1.73), hitungbmi (60, 1.73), hitungbmi (64, 1.73))

print ("VARIABEL LOKAL DAN BEBAS")
a = 5
def fungsilokal (a):
        print ("fungsi lokal adalah a :", a)
fungsilokal ("17")
print ("fungsi bebas a :", a)

print ("INPUT")
angka = input ("masukkan angka :")
angka = int (angka) + 10
print (angka)

angka = input ("masukkan angka, float dpt menghitung pecahan :")
angka = float (angka) + 10
print (angka)
