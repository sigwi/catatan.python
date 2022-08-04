print ("DICTIONARY")
d = {"key1":{"key2" : "item2"}, "kucing" : [3, "jerapah", "jangkrik"]}
print(d["key1"])
print(d["key1"]["key2"]) #memanggil isi
print(d["kucing"])
print(d["kucing"][2])
print("------------")
d = {"key1":"item1", "key2":{"key3" : "item3"}, "kucing" : [3, "jerapah", "jangkrik"]} #dictionary dalam dictionary
print(d)
print(d["key1"])
print(d["key2"]["key3"])
print(d["kucing"])
print(d["kucing"][2])
print('----------')
print ("TUPLE")
t = (1, [0, "test"], {"a1": True}); #tuple
print (t[2]["a1"]);
print(t[1][1]);
t[1][1]="akan"; #mengganti isi tuple
print (t[1][1]);
print(t[1]);
print("----------")
t = (1, [0, "test"], {"a1": True},(0, {"test2":2}, 2)); #tuple dalam tuple
print(t[3][1]["test2"]);
print("----------")
print ("SET") #Set tidak support indexing, tiap item unique, harus diubah ke list kalau mau indexing
s = {1 , 3 , 1 , 2 , 2 , 3}
print(s)
print(list(s)[2])
print("----------")
newList = [ 1 , 3 , " test1", " test2", 2 , 3 , "test1"]
s = set(newList) #list to set
print(s)
print(list(s)[3]) #set to list
print("----------")
hmmm = {1,2,2,2,2,6,3,3,5,5,7,8} #set, biasanya pakai {} (bracket) atau ([]) (kombinasi kurung dan square)
print(hmmm) #print set
s = list(hmmm) #set to list
s.sort(reverse=True) #ubah set ke list baru bisa diurutkan
print(s)
print(s[5])
print ("------------")
print ("LIST COMPREHENSION")
print ("versi satu")
listNum = [1 , 2 , 3 , 4 , 5]
print(listNum)
listNum = [isilist *2 for isilist in listNum]
print(listNum)
print ("---------")
print ("versi dua pakai fungsi")
def namafungsi(variabelnya) :
    return variabelnya * 3 #return dipakai kalau ingin hasilnya berupa nilai saja
listNum = [1 , 2 , 3 , 4 , 5]
listNum = [namafungsi(isilist)for isilist in listNum]
print(listNum)

print("LAMBDA EXPRESION")
def times2(num) :
    return num * 2;
lambda num: num * 2;

print ("MAP TANPA LAMBDA")
def namafungsi(num) :
    return num * 10
listNum = [1 , 2 , 3 , 4 , 5]
listNum = list(map(namafungsi, listNum))
print(listNum)

print ("MAP DENGAN LAMBDA")
listNum = [1 , 2 , 3 , 4 , 5]
listNum = list(map(lambda isilist: isilist * 2 , listNum))
print(listNum)

print ("FILTER TANPA LAMBDA")
def genap(num) :
    return num % 2 == 0
listNum = [1 , 2 , 3 , 4 , 5]
listNum = list(filter(genap, listNum))
print(listNum)
print ("FILTER DENGAN LAMBDA")
listNum = [1 , 2 , 3 , 4 , 5]
listNum = list(filter(lambda num : num % 2 == 0, listNum))
print(listNum)

