#Write a code to find LCM
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number: "))
Lcm=0
while b!=0:
    a,b=b,a%b
Lcm=(a*b)//a    
print("LCM of 2 numbers is:",Lcm)                                                                                                                                                                                                                                                           
