#8)Given an space separated interger list find the average of elements in the even index
my_list=list(map(int,input().split(" ")))
total=0
length=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
        total+=my_list[i]
        #count+=1
average=total/length
print(average)