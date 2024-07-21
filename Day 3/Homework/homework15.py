# Find the sum of all the elements in an array
my_list=list(map(int,input().split()));     
sum = 0;    
     
#Loop through the array to calculate sum of elements    
for i in range(0, len(my_list)):    
   sum = sum + my_list[i];    
     
print("Sum of all the elements of an array: " + str(sum))