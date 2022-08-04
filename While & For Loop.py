1a = 1
s = 2
print ("jika kondisi memenuhi fungsi while maka loop tetap jalan")
while a != 0:
    a = float (input ('a = '))
    s = s + a
    print("2 + a total = ", s)
print ("s total = ", s)

berhitung = range (1,11)
for fariabel in berhitung :
    print (fariabel)
berhitung = range (1,11)
for fariabel in berhitung :
    if fariabel == 5:
        break
    print (fariabel)
berhitung = range (1,11)
for fariabel in berhitung :
    if fariabel == 5:
        continue
    print (fariabel)
