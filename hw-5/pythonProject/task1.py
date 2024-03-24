def caching_fibbonachi(n, cache={}):

    def fibonachi(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonachi(n - 1) + fibonachi(n - 2)
        return cache[n]

    return fibonachi(n)

f3 = caching_fibbonachi(3)
print(f"f3: {f3}")

f5 = caching_fibbonachi(15)
print(f"f5: {f5}")

f4 = caching_fibbonachi(6)
print(f"f4: {f4}")
