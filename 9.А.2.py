def f(x, z):
    if x < z:
        return x
    else:
        return f(x - z, z)





a, b = int(input()), int(input())
print(f(a, b))
