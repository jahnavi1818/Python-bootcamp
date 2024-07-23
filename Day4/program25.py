#GCD of 2 nnumbers
#Eculidean Algorithm
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number: "))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)                                                                                                                                                                                                                                                           
