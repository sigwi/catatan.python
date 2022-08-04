menu_item = 0
namelist = []
while menu_item !=9:
    print ("--------------------------------------------------")
    print ("1. mencetak list")
    print ("2. menambahkan nama kedalam list")
    print ("3. menghapus nama dari list")
    print ("4. mengubah data dalam list")
    print ("9. keluar")
    print ("--------------------------------------------------")
    menu_item = int(input("masukkan pilihan :"))
    if menu_item == 1:
        current = 0
        if len(namelist)>0:
            while current < len(namelist):
                print (current,".", namelist[current])
                current = current + 1
        else:
            print ("list kosong")
    elif menu_item==2:
        name = input ("masukan nama :")
        namelist.append(name)
    elif menu_item==3:
        del_name = input ("nama yg ingin di hapus :")
        if del_name in namelist:
            item_number = namelist.index (del_name)
            del namelist[item_number]
        else :
            print (del_name, "tidak ditemukan")
    elif menu_item ==4:
        old_name = input ("nama apa saja yg ingin diubah?")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("nama baru :")
            namelist[item_number]=new_name
        else:
            print(old_name, "tidak ditemukan")
print ("selamat tinggal")