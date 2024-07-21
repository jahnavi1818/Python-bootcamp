#Find the sum of squares of a given number
total = 0 
count = 1 
n = int(input("Enter the number of squares to compute: ")) 
while count <= n: 
    total += count ** 2 
    count += 1 
print(f"The sum of the squares of the first {n} numbers is: {total}")
