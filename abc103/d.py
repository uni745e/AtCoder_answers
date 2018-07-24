#coding:utf-8

n,m = map(int, input().split())
itv = []
for i in range(m):
    si,ti = map(int, input().split())
    itv.append([ti, si])
itv.sort()

ans = 0
t = 0
for i in range(m):
    if itv[i][1] >= t:
        ans += 1
        t = itv[i][0]

print(ans)
