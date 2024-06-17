# Given two list of numbers,
# write a program to create a new list such that
# the new list should contain odd numbers from the first list
# and even numbers from the second list.
# Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = []

# for loop for odd nums in list1
for odd in list1:
    if odd % 2 == 1:
        new_list.append(odd)

# for loop for even nums in list2
for even in list2:
    if even % 2 == 0:
        new_list.append(even)

print(new_list)
