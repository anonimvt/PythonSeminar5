def recursionsum(a, b):
    if b == 0:
        return a
    return 1 + recursionsum(a, b - 1)

print(recursionsum(3, 2))
 