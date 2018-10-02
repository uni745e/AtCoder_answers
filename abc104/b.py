# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


S = input()
ans = 'AC'
if S[0] != 'A': ans = 'WA'

cnt = 0
for s in S[2:-1]:
    if s == 'C':
        cnt += 1
    else:
        if s.isupper():
            ans = 'WA'

if cnt != 1: ans = 'WA'
if S[-1].isupper(): ans = 'WA'
if S[1].isupper(): ans = 'WA'
print(ans)
