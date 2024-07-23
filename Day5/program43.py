#Write code to print all the capital letters in a given string
inp=input()
ans=""
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        ans+=i
print(ans) 