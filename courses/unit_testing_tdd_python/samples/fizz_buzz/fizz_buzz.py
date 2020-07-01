def fizz_buzz(val: int):
    is_multi_3 = is_multiple(val, 3)
    is_multi_5 = is_multiple(val, 5)

    if is_multi_3 and is_multi_5:
        return "FizzBuzz"
    elif is_multi_3:
        return "Fizz"
    elif is_multi_5:
        return "Buzz"
    else:
        return str(val)


def is_multiple(x, y):
    return x % y == 0
