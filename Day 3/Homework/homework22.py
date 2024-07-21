#check whether the number is palindrome or not using the while loop
n=int(input("enter number"))
org_num=n
rev=""
while(n>0):
    revnum=n%10
    rev=rev+str(revnum)
    n=n//10
if(org_num==int(rev)):
    print("palindrome")    
else:
    print("not palindrome")