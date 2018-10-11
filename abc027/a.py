# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


l1, l2, l3 = inpl()

if l1 == l2:
    print(l3)
elif l1 == l3:
    print(l2)
else:
    print(l1)
