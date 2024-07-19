#1)using for loop print 1 to 100 numbers
#2)using for loop append 1 to 100 numbers in aa empty list
#3)find the sum of all the numbers in a list
for i in range(1,101):#1
    print(i,end=" ")
    
empty_list=[]#2
for i in range(101):
    empty_list.append(i)
    print(i,end=" ")    
    
lst1=list(map(int,input("enter numbers").split(" ")))#3
sum=0
for i in range(len(lst1)):
    sum+=sum+lst1[i]
print(sum)    