x = 50
y = 40
def contoh():
    print (x+y)
contoh ()

def namaku (nama):
    print (nama + ' page')
namaku ('>')
namaku ('<')
namaku ('-')

def namaku (nama):
    print (nama + ' page')
    print ("++++++++")
print ("--------")
namaku ('jo')
namaku ('ro')
namaku ('yo')

def data (x,y):
    print (x + ' tanggal lahir ' + y)
print ("---------")
data ('jo', '1969')
data ('ro', '1789')
data ('yo', '1634')

def total (x,y):
    z = x+y
    print (z)
print (total(x,y))

def bh (x) :
    if (x<2):
        return 1
    else :
        return (x*tiga())
def tiga ():
    return 5
print (bh (2))

def kali (x=2, y=3):
    return x*y
print (kali(x=7))

angkanya = [1, 20, 45, 58, 65]
angkanya.sort()
print (angkanya)

angkanya.sort(reverse=True)
print (angkanya)

namanya = ['rza', 'wutang', 'clan', 'skreli']
namanya.sort()
print (namanya)

namanya.sort(reverse=True)
print (namanya)
