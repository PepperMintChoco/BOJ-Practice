'''
5543 - 상근날드
세 종류의 햄버거 가격을 세 줄에 걸쳐 입력받고
두 종류의 음료 가격을 두 줄에 걸쳐 입력받은 뒤
가장 싼 세트(햄버거 1개 + 음료 1개 - 50)의 가격을 출력해야 하는 문제
'''

import sys

berger = []
drink = []

for i in range(3):
    berger.append(int(sys.stdin.readline()))
for i in range(2):
    drink.append(int(sys.stdin.readline()))    

print(min(berger) + min(drink) - 50)

