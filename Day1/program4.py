#Mr Z is selected for olympics is participated in swimming competition only one winner is selected among all the participants anyhow Mr.Z selcted
# whereas MR Y and MR X are friends of MR Z Mr X is participated in badminton and MR Y is participated in Table tennis
# according to the selection committie the requirements for badminton players are are height = 140 cm , weight factors of 2 and body fat is less than 12%
# according to the selection committee criteria for table tennis are height = minimum 118 cm to 148cm , 
#weight is the factors no. of medals won by Mr.Z bodyfat 14%. according to the previous history Z participated in 14 games out of which he is having success rate of 50%
# Write a program to check whether MR X & MR Y &MR Z will travel in a same plane or out.Write a program to check whther this people will meet each other not.


X_height= int(input("Height eligiblity for table tennis"))
X_weight=int(input("Weight eligiblity for table  tennis"))
X_bodyfat=int(input("bodyfat eligibilty for table tennis"))
Y_height= int(input("Height eligiblity for badminton "))
Y_weight=int(input("Weight eligiblity for badminton "))
Y_bodyfat=int(input("bodyfat eligibilty for badminton"))
zmedals=(50/100)*14
if(X_height>=140) and (X_weight%2==0) and (X_bodyfat<12):
       if(Y_height>=118 or Y_weight%2==0) and (Y_weight%zmedals==0 and Y_bodyfat==14):
              print("x,yx,z are travelling in same plane")
       else:
          print("only x,z are travelling in same plane")
else:
   print("only z is travelling in the plane")
