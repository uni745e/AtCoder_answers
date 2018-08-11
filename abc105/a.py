#coding:utf-8
def inpl(): return list(map(int, input().split()))

n,k = inpl()

if n%k == 0:
    print(0)
else:
    print(1)
