#Replace the elements in array with average of max and min elements
#sample inputs
#13 2 67 20 68
#68+2=70 average = 35
#35 35 35 35 35 

my_list=list(map(float,input().split()))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i] < min):
        min=my_list[i]
for i in range(len(my_list)):
    if(my_list[i] > max):
     max=my_list[i]
average=(min+max)//2
for i in range(len(my_list)):
    my_list[i]= average
print(*my_list,end=" ")