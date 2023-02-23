def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        n = a
        a = b
        b = n+b


gen = fib(10)

for n in gen:
    print(n)