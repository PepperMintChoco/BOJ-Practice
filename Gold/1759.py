'''
1759 - 암호 만들기
암호는 서로 다른 L개의 알파벳 소문자들로 구성되어 있으며 최소 한 개의 모음과 최소 두 개의 자음이 있다고 한다.
C개의 문자들이 주어졌을 때, 가능성이 있는 암호를 모두 출력해야 하는 문제

combinations으로 모든 조합을 만든 뒤 조건에 맞는 암호만 출력하면 된다.
'''

import sys
from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, sys.stdin.readline().split())

lst = list(map(str, sys.stdin.readline().split()))

lst.sort()

for i in combinations(lst, l):
    cnt = 0
    for j in i:
        if j in vowel:
            cnt += 1
    if 1 <= cnt <= l-2:
        print(*i, sep = '')
