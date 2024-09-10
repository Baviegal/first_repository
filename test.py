def some_func(num: int | float =0, num2: int | float = 0):
    return num + num2


print(some_func(1, 1.2))
