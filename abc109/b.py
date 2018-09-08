# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())

word = input()
S = [word]
judge = True
for _ in range(N - 1):
    t = word[-1]
    word = input()
    if word[0] != t or word in S:
        judge = False
        break
    S.append(word)

if judge:
    print('Yes')
else:
    print('No')