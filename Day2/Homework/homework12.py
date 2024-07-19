#write a program to find the prime number using the sqrt method
n= int(input())
flag = 0
if (n>1):
  for k in range(2,int.sqrt(n)+1):
    if(n%k) == 0:
       flag == 1
    break 
if (flag == 0):
  print(n," is a prime number ")
else:
  print(n," is not a prime number")
