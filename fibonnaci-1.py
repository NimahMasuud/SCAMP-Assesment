def fib(num):
    x = 0
    y = 1
    i = 0
    while i < int(num):
        z = x + y
        print(x)
        x = y
        y = z

        i += 1

n = input('Enter number of Sequence: ')
fib(n)