def remove(string: str) -> str: # задание 1
    stop = ['Python', 'php', 'go', 'C']
    res = ''
    for i in stop:
        string = string.replace(i, '')
    return string


print(remove('GoGogo s fgGos s go phpC C Py'))


def num_filter(num: int, to_filter:list) -> list:   # задание 2
    return list(filter(lambda x: x % num == 0, to_filter))


print(num_filter(3, [3, 5, 6, 66, 22, 33, 3]))


def only_string(*args) -> tuple:    # задание 3
    return tuple(filter(lambda x: isinstance(x, str), args))


print(only_string('5', 5, 'ddf', 63.9, 'jg'))


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


print(match([5, 5, 6, 7, 1, 2, 40, 11], [12, 5, 4, 5, 40, 3, 3, 3]))


def ladder(num):    # задание 5
    global count
    for i in range(num, 0, -1):
        rest = num - i
        print('num = ', num)
        print('i = ', i)
        print('rest = ', rest)
        print('-' * i)
        if rest > 0:
            return ladder(rest)
        else:
            count += 1
            print()
            continue
    return count


count = 0
length = 0
print(ladder(6))


def decor(fun):     # задание 6
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        if not isinstance(result, int):
            raise Exception('Исключение')
        return result
    return wrapper


match_decor = decor(match)
# print(match_decor([5, 5, 6, 7, 1, 2, 40, 11], [12, 5, 4, 5, 40, 3, 3, 3]))

ladder_decor = decor(ladder)
# print(ladder_decor(6))


def decor_repeat(fun):     # задание 7
    def wrapper(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
        except:
            result = fun(*args, **kwargs)
        return result
    return wrapper


# match_decor_repeat = decor_repeat(match_decor)
# print(match_decor_repeat([5, 5, 6, 7, 1, 2, 40, 11], [12, 5, 4, 5, 40, 3, 3, 3]))

ladder_decor_repeat = decor_repeat(ladder)
print(ladder_decor_repeat(6))


def sort_chem(chem: list) -> list:     # задание 8
    chem = sorted(chem, key=lambda x: x[1])
    return chem


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(sort_chem(elements))
