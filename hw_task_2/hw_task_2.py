def remove(string: str) -> str: # задание 1
    stop = ['Python', 'php', 'go', 'C']
    res = ''
    for i in stop:
        string = string.replace(i, '')
    return string








print(remove('GoGogo s fgGos s go phpC C Py'))