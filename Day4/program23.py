#print all the peak elements
my_list=list(map(int,input("Enter list elements").split()))
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        print(my_list[i],end=" ") 