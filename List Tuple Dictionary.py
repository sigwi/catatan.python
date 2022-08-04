jimi = ['jimi hendrix', 27]
page = ['jimi page', 666]
database = [jimi, page]
print (database)

print ("INDEXING")
name = "jimi hendrix"
print (name[5])
print (name[-1])
print ("SLICING")
name = "robert plant"
print (name[0:6])
print (name[0:6:3])

print (list("jimi hendrix"))

rentangbulan = int (input("Bulan apa (1-12)? "))

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if 1<= rentangbulan <=12:
    print ("Bulan", bulan[rentangbulan -1])
