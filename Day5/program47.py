#patterns
#*****
#*****
#*****
#*****
#*****
n=int(input("Enter the number of rows"))
for i in range(1,1+n):
    for j in range(1,1+n):
        print("*",end=" ")
    print("\n") 
#    *  *
#  *     *
#  *  *  
n=int(input("Enter the number of rows"))
for i in range(10):
    for j in range(10):
        if(i==j):
          print(" ",end="")
        else:
            print("*",end="")  
    print() 