# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


x1, y1, x2, y2 = inpl()

diff_y = y2 - y1
diff_x = x2 - x1
ans1 = [x2 - diff_y, y2 + diff_x]
ans2 = [ans1[0] - diff_x, ans1[1] - diff_y]
ans = ans1 + ans2
print(' '.join(map(str, ans)))
