# Codeforces 906 D

def build():
    num = m
    for i in range(n):
        mods.append(num)
        num = phi(num)


def phi(number):
    res = number
    if number % 2 == 0:
        while number % 2 == 0:
            number //= 2
        res -= res // 2
    for i in range(3, number + 1):
        if number % i == 0:
            while number % i == 0:
                number //= i
            res -= res // i
    return res


def chained_pow(w, level):
    if len(w) == 1:
        return w[0] % mods[level]
    else:
        return pow(w[0], chained_pow(w[1:], level+1), mods[level])


mods = []

_ = [int(x) for x in input().split()]
n = _[0]
m = _[1]
a = [int(x) for x in input().split()]

build()
q = int(input())
for __ in range(q):
    _q = [int(x) for x in input().split()]
    left = _q[0]
    right = _q[1]
    print(chained_pow(a[left-1:right], 0))
