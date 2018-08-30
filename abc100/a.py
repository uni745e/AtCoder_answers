# coding:utf-8


def inpl(): return list(map(int, input().split()))


a, b = inpl()

if a > 8 or b > 8:
    print(':(')
else:
    print('Yay!')