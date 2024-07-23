#ABC,4
#EFGH
str=(input("Enter the string:"))
n=int(input("Enter the skip value:"))
inp=str.upper()
empty=""
for i in inp:
    empty+=chr(ord(i)+n)
print(empty) 