# SoundHound2018
https://beta.atcoder.jp/contests/soundhound2018-summer-qual

## B
スライス記法を用いてw番目の文字を呼び出す  
```
for s in S[::w]:
	ans += s
```

## C
確率と期待値の問題  
1. iとi+1番目の差の絶対値がdになる確率を考える
2. 1を満たす組み合わせの個数を考える  
3. 長さがmの場合、判定はm-1回行われる

d=0なら  
E = n*(m-1)/n**2 = (m-1)/n

d≠1なら  
E = 2(n-d)*(m-1)/n**2  

## D
