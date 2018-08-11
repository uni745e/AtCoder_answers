#coding:utf-8

def inpl(): return list(map(int, input().split()))


n = int(input())
ans = 'No'

for i in range(n//4+1):
    if (n - i*4)%7 == 0:
        ans = 'Yes'
        break
print(ans)
