#taking the list as dynamic
my_list=list(map(int,input().split())) #split is for default spacing # we can use anytype of datatype
print(*my_list)
#input.split() user will give the input from the ternimal it will take default space separated it will tae integer type inputs 
#map is used to take more than one input and list is used for type casting.

my_list=list(map(int,input().split("@")))
print(*my_list)

dy_in=list(map(int,input("given integer values").split("")))
print(*dy_in)
dy_in1=list(map(int,input("given integer values").split("")))
print(*dy_in1)
