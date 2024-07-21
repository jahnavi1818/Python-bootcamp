#Find the sum of squares of even and odd digits(separate separate)
n=int(input("Enter n value"))
even_sum=0
odd_sum=0
while(n>0):
    digit=n%10
    if digit%2==0:
        even_sum+=digit**2
    else:
        odd_sum+=digit**2
        n=n//10
print(even_sum)
print(odd_sum)        
    