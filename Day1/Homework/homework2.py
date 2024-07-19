#Check whether the number is prime or not 
n= int(input())
flag = 0
if (n>1):
  for k in range(2,int.sqrt(n)+1):
    if(n%k) == 0:
       flag == 1
    if (flag == 0):
     print(n," is a prime number ")
else:
  print(n," is not a prime number")

