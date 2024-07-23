#Print rhombus pattern
rows = 4
for i in range (1,rows + 1):
    for j in range (1,rows - i + 1):
        print (end=" ")
    for j in range (1,rows + 1):
       print ("*",end=" ")
    print()
    
#or 

num = int(input("Enter the number:"))

for i in range(0, num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()
    
#or    
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")