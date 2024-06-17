# For example,
# If the given int is 7536,
# the output shall be “6 3 5 7“,
# with a space separating the digits

def rev_int(num):
    num_str = str(num)

    reversed_str = num_str[::-1]

    new_num = " ".join(reversed_str)

    return new_num


print(rev_int(1234))
