'''
11943 - 파일 옮기기
첫 번째 바구니에는 사과 A개와 오렌지 B개가,
두 번째 바구니에는 사과 C개와 오렌지 D개가 있다고 할 때
사과와 오렌지를 옮기는 최소 횟수를 출력해야 하는 문제

A+D와 C+B를 계산하고 둘 중 작은 값을 출력하면 된다.

제목은 파일 옮기기인데 문제에서는 웬 과일 이야기..? 싶었는데
출제자의 단순한 말장난(파 -> 과)이었던 것 같다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

if a+d < b+c:
    print(a+d)
else:
    print(b+c)
