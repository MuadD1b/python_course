def remove(string: str) -> str: # задание 1
    stop = ['Python', 'php', 'go', 'C']
    res = ''
    for i in stop:
        string = string.replace(i, '')
    return string


def num_filter(num: int, to_filter:list) -> list:   # задание 2
    return list(filter(lambda x: x % num == 0, to_filter))





print(remove('GoGogo s fgGos s go phpC C Py'))
print(num_filter(3, [3, 5, 6, 66, 22, 33, 3]))