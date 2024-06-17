# Note: here exp is a non-negative integer, and the base is an integer.

# While using "**" operator
def power_fun1(base, exponent):
    result = base ** exponent
    return result


# without using "**" operator
def power_fun2(base, exponent):
    count = exponent
    result = 1  # defult
    while count > 0:
        result *= base  # result = result * base
        count -= 1

    return result


print(power_fun1(4, 2))
print(power_fun2(4, 2))
