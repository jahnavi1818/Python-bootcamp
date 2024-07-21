def findPeak(L):
    results = []
    for i in range(1, len(L) - 1):
        if L[i] > L[i-1] and L[i] > L[i+1]:    # check both sides for each
            results.append(L[i])               # ^ element of list excluding edge cases
    if L[0] > L[1]: results.append(L[0])       # check edge cases
    if L[-1] > L[-2]: results.append(L[-1])
    return results
my_list = list(map(int,input().split()))
print("Peak points are: ", findPeak(my_list))