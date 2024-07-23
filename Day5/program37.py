#print all vowels followed by consonants
vowels="aieouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ans=""
inp  = input()
for i in inp :
    if (i in vowels):
        ans+=i
        
for i in inp: 
    if i in consonants:
        ans+=i
                       
print(ans)
    