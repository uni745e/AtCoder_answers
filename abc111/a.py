# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
N = str(N)
ans = ''
for n in N:
    if n == '1':
        ans += '9'
    else:
        ans += '1'
print(ans)
