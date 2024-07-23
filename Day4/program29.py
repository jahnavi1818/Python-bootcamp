#Write a print all the prime numbers in given range
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
count=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)    
            