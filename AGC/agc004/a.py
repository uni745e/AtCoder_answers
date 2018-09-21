# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


box = inpl()
box.sort()

if box[0] % 2 == 0 or box[1] % 2 == 0 or box[2] % 2 == 0:
    print(0)
else:
    print(box[0] * box[1])
