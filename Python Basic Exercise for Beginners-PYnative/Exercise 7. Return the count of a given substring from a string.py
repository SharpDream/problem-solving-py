def str_count(string, target):
    str_list = string.split()

    count = str_list.count(target)

    return count


str_x = "Emma is good developer. Emma is a writer"
print(str_count(str_x, "Emma"))
