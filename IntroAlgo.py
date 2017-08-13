import time


def fib(n):
    if n <= 1:
        return n
    return n * fib(n - 1)

start = time.clock()
n = 500
print(fib(n))
end = time.clock()

print('Executed time: ', round((end - start), 5), '(s)')