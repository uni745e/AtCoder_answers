#coding:utf-8

d,g = map(int, input().split())
P = []
C = []
sums = []
for i in range(d):
    p,c = map(int, input().split())
    P.append(p)
    # C.append(c)
    sums.append(p * 100 * (i+1) + c)

ans = 1e9
for mask in range(1 << d):
    score = 0
    num = 0
    rest_max = -1
    for i in range(d):
        if mask >> i & 1:
            score += sums[i]
            num += P[i]
        else:
            rest_max = i
    if score < g:
        tmp = 100 * (rest_max + 1)
        need = (g - score + tmp - 1) // tmp
        if need >= P[rest_max]: continue
        num += need
    ans = min(ans, num)

print(ans)
