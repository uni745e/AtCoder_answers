# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


S = input()
S_li = list(S)
direction = ('N', 'W', 'S', 'E')
judge = []
for di in direction:
    if di in S_li:
        judge.append(1)
    else:
        judge.append(0)


if judge[0] ^ judge[2] == 1:
    print('No')
elif judge[1] ^ judge[3] == 1:
    print('No')
else:
    print('Yes')
