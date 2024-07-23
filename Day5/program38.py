#Print the non repeating characters in string or print the unique characters in a string

vowels="aieouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ans=""
str=input()
for i in str:
    if (i not in ans):
        ans+=i
print(ans)        