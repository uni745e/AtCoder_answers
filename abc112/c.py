# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


def solve():
    for cx in range(101):
        for cy in range(101):
            # max(h)を使って仮の頂点の高さChを決める
            # hは負の値にならないので
            # h[i] = 0を使うと頂点の高さが元より低くなってしまう
            ch = D[0][0] + abs(D[0][1] - cx) + abs(D[0][2] - cy)
            for h, x, y in D:
                if h != max(ch - (abs(x - cx) + abs(y - cy)), 0):
                    break
            else:
                return cx, cy, ch


if __name__ == '__main__':
    N = int(input())
    D = []
    for i in range(N):
        x, y, h = inpl()
        D.append([h, x, y])
    D.sort()  # hに対してソート
    D.reverse()
    ans = solve()
    print(' '.join(map(str, ans)))
