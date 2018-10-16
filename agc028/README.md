# AGC028
https://beta.atcoder.jp/contests/agc028/tasks

# A - Two abbreviations
文字列Xの長さLはlcm(N, M)の定数倍になる  
文字列Xのk * lcm(L/N, L/M) (k = 0 ~ gcd(N, M) - 1)番目の文字は  
S\[k * lcm(L/N, L/M) / (L/N)]と  
T\[k * lcm(L/N, L/M) / (L/M)]で使われる  
文字列S, Tで使われている文字が全て一致した場合、長さLの文字列Xが存在する.

# B - Removing Blocks
ブロックiの重さが足される回数を求めてやれば、
それを係数としてAiに掛けて、加算することで答えが求まる。

ブロックiを取り除く時、ブロックjと連結である確率P(i, j)は
1/(abs(i - j) + 1)である。これを各jについて求めておく。
これは1/1 + 1/2 + ... 1/Nのような形になるので、
1/kの累積和を求めておくことで、各jについてO(1)で求められる。    
N!通り繰り返した場合、ブロックi, jが連結となるパターンはN! * Σ P(i, j)となる。

割り算のmodを取るので1/1 ~ 1/Nは逆元を求めて、掛け算として解く。



# C


# D


# わかったこと
- 逆元計算
    - pow(k, MOD-2, MOD)をN回使うと計算時間がかかる
    - k!と1/k!のMODを取ったものを先に求めておくことで
    - １回のpow()で任意の1/kの逆元が求まる
    ```Python  
    # fact: k! (mod MOD)  
    # fact_inv: 1/k! (mod MOD)  
    # inv: 1/kの逆元
    inv = [1]
    for i in range(1, N):
        inv.append((fact[i - 1] * fact_inv[i]) % MOD)
    ```
- pow()
    - 繰り返し二乗法を使ってたけどデフォルトのほうが速そう  
    - O(log(N))で求まる
    - 逆元計算も可能: pow(n, MOD - 2, MOD)
