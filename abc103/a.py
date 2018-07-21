#coding:utf-8
A = list(map(int, input().split()))
A.sort()
cost = 0
prev = A[0]
for a in A:
    cost += abs(a - prev)
    prev = a

print(cost)
