def pattern1():
    for x in range(5, 0, -1):  # x = row
        print("*" * x)


def pattern2():
    for x in range(5, 0, -1):
        for y in range(x):
            print("*", end=" ")
        print(" ")  # or print ('\n')
        # I think print(" ") is better :)


pattern1()
print("\n")
pattern2()
