def f(max_digit=None, answer=None):
    n = int(input("Введите натуральное число: "))

    if n == 0:
        if answer is not None:
            print()
            print(f"Второй по величине элемент: {answer}")
        return

    if max_digit is None or n > max_digit:
        answer = max_digit
        max_digit = n
    elif (answer is None or n > answer) and (n != max_digit):
        answer = n

    f(max_digit, answer)


f()