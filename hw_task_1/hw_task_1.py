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
        print('YES')
    else:
        print('NO')


def positive(list1: list) -> int: # Задание 6
    j = 0
    s = 0
    for i in list1:
        if list1[j] >= 0:
            s += 1
        j += 1
    return s


def days(years: int, months: int) -> int: # Задание 7
    days_num = (years * 12 + months) * 29
    print(days_num)


def abriviate(string: str) -> str: # Задание 8
    letters = ''
    try:
        for i in range(len(string)):
            if i == 0:
                letters += string[i]
                continue
            if string[i - 1] == ' ':
                letters += string[i]
        print(letters)
    except TypeError:
        print('Wrong type!')


def factorial(number: int) -> int: # Задание 9
    res = 1
    for i in range(1, number + 1):
        res *= i
    return res


print(str_len('56'))
print(list_len_compare([5, 5, 5], ['y', 'u', 'p', 'i']))
print(list_append([5, 5, 5], ['y', 'u', 'p', 'i']))
in_range(-99.9)
print(question('test', 'testtest'))
print(positive([1, -1, 2, -5, 4.5]))
days(1, 7)
abriviate('j n jb')
print(factorial(6))