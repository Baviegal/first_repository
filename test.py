def some_func(num: int | float =0, num2: int | float = 0):
    return num + num2


print(some_func(1, 1.2))


def second_some_func(line: str, line2: str):
    return line + ' ' + line2


print(second_some_func('abc', 'def')
      
