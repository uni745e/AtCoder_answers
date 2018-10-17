# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


def move(x, y):
    command = ''
    if x > 0:
        command += 'R' * x
    else:
        command += 'L' * abs(x)
    if y > 0:
        command += 'U' * y
    else:
        command += 'D' * abs(y)
    command += 'RL' * ((max_length - abs(x) - abs(y)) // 2)
    return command


N = int(input())
point = []
max_length = 0
for i in range(N):
    x, y = inpl()
    max_length = max(max_length, abs(x) + abs(y))
    point.append([x, y])

tmp = sum(point[0]) % 2
judge = True
for p in point:
    if tmp ^ sum(p) % 2:
        judge = False

if judge:
    print(max_length)
    print(' '.join(['1'] * max_length))
    for x, y in point:
        print(move(x, y))
else:
    print(-1)
