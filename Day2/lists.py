#declaring a list
my_list=[1,2,3,4]#we used static declaration
print(*my_list)

#for append
my_list=[1,2,3,4]#we used static declaration
my_list.append(9999)
print(*my_list)

#for insert
my_list=[1,2,3,4]#we used static declaration
my_list.insert(8000,9999)#for the index which is present it inserts at that partiular value for others it  inserts at last which is not present
print(*my_list)

#length of the list
my_list=[1,2,3,4]#we used static declaration
print(len(my_list))
print(*my_list)

#pop command
#pop the element at particular index value and it will default pop the last element
my_list=[1,2,3,4]#we used static declaration
my_list.pop(2) #that particular value is present in the list but it isnt showing in the output
print(*my_list)

#concatenation
my_list=[1,2,3,4]#we used static declaration
my_list_2=[5,6,7,8]
new_list = my_list + my_list_2
print(*new_list)

#count
my_list=[1,2,3,4]#we used static declaration
my_list_2=[5,6,7,8]
cnt=my_list.count(2)
print(cnt)

#sorting in asecdning order it is default
my_list=[5,2,3,4]
my_list.sort()
print(*my_list)
