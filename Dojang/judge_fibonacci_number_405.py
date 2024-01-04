# 코딩도장 p.405 심사문제


def fib(n, i=0, j=1) :
    if not n :
        return i
    return fib(n-1, j, i+j)

n=int(input())
print(fib(n))