#Prime number or not
a=int(input("Enter a number:"))
r=a**0.5
count=0
if(a==1):
    print("Not a prime number")
elif(a==2):
     print("Prime number") 
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break 
if(count == 0):
    print("Prime number")
elif(count>0):
    print("Not a prime number")    
        
    