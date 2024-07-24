#oops concept
#defining class and objects
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
    
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.sub(2,5))    

#Variables
#class variable and instance variable
class Myclass:
    cls_var="i m class variable"
    def add(a,b):
        ins_var_add ="i m instance variable"
        return a+b
    def sub(a,b):
        #print(ins_var_add)
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
    
obj1=Myclass  
print(obj1.add(2,5)) 
    
    
#inheritance
class Animal:
    def Speak():
        return "Animal is speaking"
#single inh #Multilevel
class Dog(Animal):
    def Bark():
        return "Bow...." 
class Puppy(Dog): 
    def puppy_speak():
        return "I m Puppy"
obj1=Animal 
obj2=Dog
obj3=Puppy
print(obj1.Speak())
print(obj2.Bark())   
print(obj3.Puppy_speak())  

#Multiple
class Father:
    def Father_speak():
        return "Father class"
class Mother:
    def Mother_speak():
        return"Mother Speak"
class kid(Father,Mother):
    def kid_speak():
        return "Im kid.I m having properties of Mother Class and Father Class"
obj1=kid
print(obj1.Father_speak()) 
print(obj1.Mother_speak())
print(obj1.kid_speak())     

#Polymorphism
#method_over_riding
class Animal:
    def Speak():
        return "Speaking...."
class Dog(Animal):
    def Speak():
        return"Dog is speaking...." 
class puppy(Dog):
    def Speak():
        return"Puppy is speaking..."
obj3=puppy
print(obj3.Speak())


def run():
    return"Running...."           
def run():
    return "Hello"
print(run())




class cal:
    def add(self,args):
        return sum(args)
    
class cal:
    def add(a,b,c):
        return a+b+c
    def add(a,b,c,d):
        return a+b+c+d 
    def add(a,b,c,d,e):
        return a+b+c+d+e
    def add(self,args):
        sum=0
        for i in args:
            sum+=i
            return sum
            
    
obj1=cal
print(obj1.self)
print(obj1.add(1,2,3))    
print(obj1.add(1,2,3)) 
print(obj1.add(1,2,3))             


class cla:
    def add(self,*args):
        sum=0
        for i in args:
            sum+=i
        return sum(args)
    
#take input
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
