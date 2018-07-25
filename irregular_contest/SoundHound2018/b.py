S = input()
w = int(input())
ans = ''
for s in S[::w]:
    ans += s
print(ans)
