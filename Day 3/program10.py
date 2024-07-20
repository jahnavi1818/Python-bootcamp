#print the element in a particular index 
#test case
#K=3
#3 6 8 4 61 2   
#op:4

#test case
#k=8
#80 70 54 36 72
#op:36

#test case
#K=20
#70 54 36 72 76 9999 0089  k=20 len = 7 indx =6
#1  2   3  4  5  6    7 

k = int(input())
my_list=list(map(int,input().split()))
if (len(my_list) > (k)):
      print(my_list[k],end=" ")
else: 
    for i in range(len(my_list)):
        index=k%len(my_list)
        print(my_list[index])    
    

#my_list=list(map(int,input().split()))
#k = int(input()) 
#index=k%len(my_list)
#print(my_list[index])   