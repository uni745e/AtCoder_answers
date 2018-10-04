# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
number = {}
for i in range(N):
    a = input()
    if a not in number:
        number[a] = 1
    else:
        number[a] += 1

ans = 0
for a in number:
    if number[a] % 2 == 1:
        ans += 1

print(ans)
