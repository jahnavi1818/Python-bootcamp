#Check how many vowels are there in a string
str=input()
vowels="aieouAEIOU"
count=0
for char in str:
    if char in vowels:
        count+=1
print("the number of vowels:",count)        
    
    