#write a program to print all the count of consonants
str=input()
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count=0
for char in str:
    if char in consonants:
        count+=1
print("the number of consonants",count)        