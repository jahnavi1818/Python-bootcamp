#question-5
#Take the list from user integer list 
#1 append
#2 pop
#3 sort
#4 len of the list
my_list=list(map(int,input().split()))
choice=int(input())
if(choice == 1):
    print(my_list.append())
elif(choice == 2):
    print(my_list.pop())
elif(choice == 3):
    print(my_list.sort())
    print(*my_list)
elif(choice == 4):
    print(len(my_list))  