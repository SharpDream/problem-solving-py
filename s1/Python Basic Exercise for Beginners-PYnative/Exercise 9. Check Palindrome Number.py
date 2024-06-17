# A palindrome number is a number that is the same after reverse.
# For example, 545, is the palindrome numbers

def pali(num):
    reversed_num = str(num)[::-1]

    if str(num) == reversed_num:
        return True
    else:
        return False


print(pali(12))
print(pali(121))
