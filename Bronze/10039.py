'''
10039 - 평균 점수
다섯 명의 학생 점수를 입력받아 평균을 출력해야 하는 문제
단, 점수가 40점 미만인 학생의 점수는 40점으로 바꾼 뒤 계산해야 한다
'''

import sys

score = []

for i in range(5):
    score.append(int(sys.stdin.readline()))

for i in range(5):
    if score[i] < 40:
        score[i] = 40

print(sum(score)//5)
