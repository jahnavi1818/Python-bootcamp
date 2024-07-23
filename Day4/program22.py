#peak element(important code)
my_list=list(map(int,input("Enter list elements").split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]<my_list[i+1]:
        count=i
        break #for the first peak element
print(my_list[count])  


         
         
           
        
