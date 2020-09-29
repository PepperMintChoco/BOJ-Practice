'''
2752 - 세수정렬
세 수를 입력받고, 오름차순으로 정렬해야 하는 문제
'''

import sys

n = map(int, sys.stdin.readline().split())

print(*sorted(n))
