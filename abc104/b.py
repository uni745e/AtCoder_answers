#coding:utf-8

s = input()
ans = 'AC'
if s[0] != 'A': ans = 'WA'

num_c = 0
for c in s[2:-1]:
    if c == 'C':
        num_c += 1
    else:
        if c.isupper():
            ans = 'WA'
if num_c != 1: ans = 'WA'

if s[-1].isupper(): ans = 'WA'
if s[1].isupper(): ans = 'WA'
print(ans)
