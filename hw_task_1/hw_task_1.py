def str_len(string):    # Задание 1
    if type(string) == str:
        return len(string)
    else:
        return 'Input must be string!'

print(str_len('56'))