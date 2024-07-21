#check whether the number is palindrome or not using the while loop
def palindrome(s):
    i = 0
    while i <= len(s) / 2:
        if s[i] != s[-i - 1]:
            return False
        i += 1
    return True