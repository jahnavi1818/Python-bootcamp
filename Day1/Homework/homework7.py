#Find the sum of the first ten natural numbers

print("The first 10 natural numbers are: \n")
sum = 0
for i in range(1, 11):
    sum = sum + i
    print(i)
print("The sum is : ", sum)