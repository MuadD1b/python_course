def str_len(string: str) -> int:    # Задание 1
    if type(string) == str:
        return len(string)
    else:
        return 'Input must be string!'


def list_len_compare(list1: list, list2: list) -> int: # Задание 2
    if type(list1) != list or type(list2) != list:
        return 'Inputs must be lists!'

    if len(list1) > len(list2):
        return len(list1)
    else:
        return len(list2)


def list_append(list1: list, value: any) -> list: # Задание 3
    if type(list1) != list:
        return 'Input 1 must be lists!'
    else:
        list1.append(value)
        return list1


def in_range(number: float): # Задание 4
    if number > -100 and number < 100:
        return '+'
    else:
        return '-'


def question(string1: str, string2: str) -> str: # Задание 5
    if string1 in string2:
        return 'YES'
    else:
        return 'NO'




print(str_len('56'))
print(list_len_compare([5, 5, 5], ['y', 'u', 'p', 'i']))
print(list_append([5, 5, 5], ['y', 'u', 'p', 'i']))
print(in_range(-99.9))
print(question('test', 'testtest'))