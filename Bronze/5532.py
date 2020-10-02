'''
5532 - 방학 숙제
방학 기간 L일 동안 수학 B페이지, 국어 A페이지를 풀어야 하는데
하루에 국어는 최대 C페이지, 수학은 최대 D페이지 풀 수 있다고 할 때
방학동안 숙제를 하지 않고 놀 수 있는 최대 날의 수를 출력해야 하는 문제

하루동안 국어나 수학을 최대 페이지만큼 푼 날이 많을 수록 숙제를 빨리 끝낼 수 있으므로
과목 별 (총 페이지 / 하루동안 최대로 풀 수 있는 페이지)를 계산 후 올림을 해준다.
방학 기간에서 ceil(a/c), ceil(b/d) 중 큰 값을 뺀 결과를 출력하면 된다.
'''

import math, sys

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

print(l - max(math.ceil(a / c), math.ceil(b / d)))
