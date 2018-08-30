# coding:utf-8


def inpl(): return list(map(int, input().split()))


a, b = inpl()

if b != 100:  # 9900の次は10100
    print(100 ** a * b)
else:
    print(100 ** a * (b + 1))
