#Reverse an array without using built-in functions
my_list=list(map(int,input().split()))
print("The array: ", my_list)
l = len(my_list)
for i in range(l // 2):
    my_list[i], my_list[l - i - 1] = my_list[l - i - 1], my_list[i]

print("The reversed array: ", my_list)