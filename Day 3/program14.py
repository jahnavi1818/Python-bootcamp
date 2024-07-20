#Find the  missing number in an array
my_list=list(map(int,input().split()))
n=10
total=n*(n+1)//2
sum=0
for i in range(len(my_list)):
    sum=sum+my_list[i]
print(total-sum)        