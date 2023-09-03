def remove(string: str) -> str: # задание 1
    stop = ['Python', 'php', 'go', 'C']
    res = ''
    for i in stop:
        string = string.replace(i, '')
    return string


def num_filter(num: int, to_filter:list) -> list:   # задание 2
    return list(filter(lambda x: x % num == 0, to_filter))


def only_string(*args) -> tuple:    # задание 3
    return tuple(filter(lambda x: isinstance(x, str), args))


def match(list1: list, list2: list) -> list:    # задание 4
    res = []
    for i in list1:
        if i in res:
            pass
        elif i in list2:
            res.append(i)
        else:
            pass
    return res




print(remove('GoGogo s fgGos s go phpC C Py'))
print(num_filter(3, [3, 5, 6, 66, 22, 33, 3]))
print(only_string('5', 5, 'ddf', 63.9, 'jg'))
print(match([5, 5, 6, 7, 1, 2, 40, 11], [12, 5, 4, 5, 40, 3, 3, 3]))