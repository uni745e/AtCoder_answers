# coding:utf-8

import math


def inpl(): return list(map(int, input().split()))


n = int(input())

print(math.ceil(n/2) * math.floor((n/2)))
