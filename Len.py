list_a = [1,23,12]
list_length = len (list_a)
print (list_length)
print("---------------------------")
new_list = ['page', 'plant', 'jones', 'bonzo', 'hendrix', 'gaye']
print (new_list)
print("---------------------------")
new_list.append('jackson')
print (new_list)
print("---------------------------")
new_list.insert(0,'osborne')
print (new_list)
print("---------------------------")
del new_list[0]
print (new_list)
print("---------------------------")
new_list.remove('gaye')
print (new_list)
print("---------------------------")
new_list.pop()
print (new_list)
print("---------------------------")
new_list1=new_list.copy()
print (new_list)
print("---------------------------")
new_list.extend(new_list1)
print(new_list)
print("---------------------------")
new_list.clear()
print(new_list)
print("---------------------------")
