#Find the element present in K+N index 
#test case 1
#K is given by user ex:K=3 
#N=2
#The input paramters are 3 6 8 4 61 2  
#output is 2

#test case 2
#K=3
#N=4
#80 70 54 36 72
#Op:error

k = int(input())
n = int(input())
my_list=list(map(int,input().split()))
if (len(my_list) < (k+n)):
   print("Error")
else:
    for i in range(len(my_list)):
        print(my_list[k+n],end=" ")
        break  
