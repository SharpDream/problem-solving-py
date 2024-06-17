def divide_five(given_list):
    print(f"Given list is {given_list}")
    print("Divisible by Five:")
    for num in given_list:
        if num % 5 == 0:
            print(num)
        else:
            pass


list1 = [10, 20, 33, 46, 55]
divide_five(list1)
