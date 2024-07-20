#reverse the numbers of a list(important)
num = int(input())
#reversed_num = 0
rev=""
while num != 0:
    r = num % 10
    #digit=num%10
    #reversed_num = reversed_num * 10 + digit
    rev=rev+str(r)
    num= num// 10
ans=int(rev)
print(ans)
print(type(ans))
#print(reversed_num) 
#print(int(rev))
