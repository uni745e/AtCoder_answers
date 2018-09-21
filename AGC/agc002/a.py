# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


a, b = inpl()

if a > 0 and b > 0:
    print('Positive')
elif a <= 0 and b >= 0:
    print('Zero')
else:
    if a % 2 + b % 2 == 1:
        print('Positive')
    else:
        print('Negative')
