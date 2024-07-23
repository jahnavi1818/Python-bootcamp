#To print the sum of digits in the string
a=input()
sum=0
for i in a:
    if(ord(i) >= 48 and ord(i) <= 57):
        sum = sum +int(i)
print("the sum is: " + str(sum))        

#or

vowels="aieouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
check = "0123456789"
ans=0
inp  = input()
for i in inp :
    if(i in check):
        ans+=int(i)
                       
print(ans)