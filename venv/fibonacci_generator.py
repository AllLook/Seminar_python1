def fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


print(list(fib(10)))
