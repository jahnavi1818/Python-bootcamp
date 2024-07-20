#Find the duplicates in an array
my_list=list(map(int,input().split()))     
print("Duplicate elements in given array: ")     
for i in range(0, len(my_list)):    
    for j in range(i+1, len(my_list)):    
        if(my_list[i] == my_list[j]):    
          print(my_list[j])    
