def fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:

        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def cacher(fn: callable):
    cachebox = {}
    def cache(n):
        if n in cachebox:
            return cachebox[n]
        else:
            fn_result = fn(n)
            cachebox[n] = fn_result
            return fn_result
    return cache

cached_func = cacher(fibonacci)

print(cached_func(10))
print(cached_func(7))
print(cached_func(7))
