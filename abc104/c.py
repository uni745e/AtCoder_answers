# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


D, G = inpl()
P, C = [], []
for i in range(D):
    p, c = inpl()
    P.append(p)
    C.append(c + 100 * (i + 1) * p)

ans = INF
for i in range(2 ** D):
    point = 0
    cnt = 0
    rest_max = 0
    for shift in range(D):
        if i >> shift & 1:
            cnt += P[shift]
            point += C[shift]
        else:
            rest_max = shift

    if point < G:
        for j in range(P[rest_max]):
            if point >= G:
                break
            cnt += 1
            point += (rest_max + 1) * 100
        else:
            continue

    ans = min(ans, cnt)

print(ans)
