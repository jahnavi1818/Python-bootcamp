#print lower triangular matrix
arr = [[4, 5, 6],
       [1, 2, 3],
       [2, 6, 7]]

print("The original matrix: ")
for row in arr:
   print(row)
print()

print("The lower triangular matrix: ")
for i in range(3):
   for j in range(3):
      if(i < j):
         print(end="  ")
      else:
         print(arr[i][j],end=" ")
   print(" ")