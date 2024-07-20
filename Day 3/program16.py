#find unique values in the list
my_list=list(map(int,input().split()))     
print("Unique elements in given array: ")
for i in range(0, len(my_list)):    
    for j in range(i+1, len(my_list)):    
        if(my_list[i] != my_list[j]):    
          print(my_list[j])    
