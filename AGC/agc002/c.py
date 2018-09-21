# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, L = inpl()
A = inpl()

tmp = 0
connect = False
knot = None
for i in range(N):
    if A[i] >= L:
        knots = i
        break

if knot is None:
    for i in range(N - 1):
        if sum(A[i:i + 2]) >= L:
            knot = i
            connect = True
            break

if knot is None:
    print('Impossible')
else:
    print('Possible')
    for i in range(N - 1):
        if i == knot:
            break
        else:
            print(i + 1)

    for i in range(N - 1)[::-1]:
        if i == knot:
            break
        else:
            print(i + 1)
    if connect:
        print(knot + 1)
