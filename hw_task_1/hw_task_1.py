def str_len(string):    # Задание 1
    if type(string) == str:
        return len(string)
    else:
        return 'Input must be string!'


def list_len_compare(list1, list2): # Задание 2
    if type(list1) != list or type(list2) != list:
        return 'Inputs must be lists!'

    if len(list1) > len(list2):
        return len(list1)
    else:
        return len(list2)


print(str_len('56'))
print(list_len_compare([5, 5, 5], ['y', 'u', 'p', 'i']))
