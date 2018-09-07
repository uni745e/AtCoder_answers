# coding:utf-8

INF = float('inf')


N = int(input())
S = input()

ans = 0
for i in range(1, N - 1):
    str_list = []
    score = 0

    for x in S[:i]:
        if x not in str_list: str_list.append(x)

    for xi in str_list:
        if xi in S[i:]: score += 1

    ans = max(ans, score)

print(ans)
