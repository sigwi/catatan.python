x = 0
while x < 10 :
    x += 1
    print ("nomor urut", x)

y = "nomor urut "
for item in range(0,22,2) :
    print (y + str(item))

z = "+"
for item in range(0,5) :
    z = z + "-"
    print (z)

z = ""
for item in range(5) :
    for item in range(5):
        z = z + "* "
    z = z + "-- "
print (z)

z = ""
for item in range(5) :
    for item in range(5):
        z = z + "* "
    z = z + "\n"
print (z)

