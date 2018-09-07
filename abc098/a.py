# coding:utf-8


def inpl(): return list(map(int, input().split()))


a, b = inpl()
print(max(a + b, a - b, a * b))
