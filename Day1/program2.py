#X GOES TO MARKET HE WILL BUY 10 APPLES , 2 DOZEN BANANAS , 8 ORANGES 
# THE COST OF EACH APPLE is 15 AND COST OF ONE BANANA IS 4  AND COST OF ONE ORANGE IS 5 
# SHE GAVE 700 RUPPEES TO X IF HE IS LEFT OVER WITH SOME  MONEY THE VENDOR DIDNT FOOL HIM
#IF HE IS TELLS TO GIVE MORE MONEY THEN THE VENDOR CHEATED HIM

apples = int(input("No. of apples to buy"))
bananas = int(input("No. of bananas to buy"))
oranges = int(input("No. of oranges to buy"))
costa = 15*apples
costb = 4*bananas
costo = 5*oranges
sum = costa + costb + costo
print(sum)
if(sum > 700):
   print("The kid got cheated by the vendor")
else:
   print("The kid didnot get cheated by the vendor")  

cost_of_apple= 15
cost_of_banana= 8  
cost_of_orange= 5 
print("Enter the no. of apples")
no_of_apples=int(input())
print("Enter the no. of bananas")
no_of_bananas=int(input())
print("Enter the no. of oranges")
no_of_orange=int(input())
print("Enter the amount given by the mother")
amount_given = int(input())
sum = (no_of_apples*cost_of_apple + no_of_bananas*cost_of_banana + no_of_orange*cost_of_orange )
if (sum>700):
   print("He didnt get cheated")
else:
   print("He got cheated")
