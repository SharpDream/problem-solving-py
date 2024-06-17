def list_check(given_list):

    print(f"Given list: {given_list}")

    if given_list[0] == given_list[-1]:
        return True
    elif given_list[0] != given_list[-1]:
        return False
    else:
        print("Error")


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(list_check(numbers_x))
print(list_check(numbers_y))
