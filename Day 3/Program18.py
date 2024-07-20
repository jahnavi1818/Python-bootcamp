#Find the sum of  squares of a digit in a given number
Number = int(input("Please Enter any Number: "))
Sum = 0
while(Number > 0):
    r = Number % 10
    Sum = Sum + r**2
    Number = Number //10
print("\n Sum of squares of a digit in a given number = %d" %Sum)