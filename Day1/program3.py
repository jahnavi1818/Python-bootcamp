#Check whether the numbers are even positive or negative and odd negative or positive
a=int(input())
if (a%2==0) and (a>0):
   print("The number is even number and positive") 
elif(a%2==0) and (a<0):
   print("The number is even number and negative")     
elif(a%3==0) and (a>0):
   print("The number is odd number and positive") 
elif(a%3==0) and (a<0):
   print("The number is odd number and negative")   
