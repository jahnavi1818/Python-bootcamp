#sum of elements of even value
Number = int(input("Please Enter any Number: "))
Sum = 0
while(Number > 0):
    r = Number % 10
    if(r%2==0):
      Sum = Sum + r
Number = Number //10
print(Sum)