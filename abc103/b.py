#coding:utf-8

s = input()
t = input()

ans = 'No'
if s == t: ans = 'Yes'

for i in range(1,len(s)):
    s_roteted = s[-i:] + s[:-i]
    if s_roteted == t : ans = 'Yes'
    if ans == 'Yes': break

print(ans)
