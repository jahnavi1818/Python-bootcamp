#find the minimum element in the given list
my_list=list(map(int,input().split()))
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i] < min):
        min=my_list[i]
print(min)  