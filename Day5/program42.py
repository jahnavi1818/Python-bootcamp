#sum of ascii values
inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)        