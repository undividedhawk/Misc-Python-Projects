t = int(input())
# uses memoization to decrease time complexity of fibonacci sequence

def fibonacci(n, cache={}):


    if n == 1:
        return 1
    elif n == 2:
        return 1
    if n in cache:
        return cache[n]
    else:
        return cache.setdefault(n, fibonacci(n-1) + fibonacci(n-2))

while t > 0:
    n = int(input())
    fibonacci(n)
    print(fibonacci(n))
    t = t - 1
