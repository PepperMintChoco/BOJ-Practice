'''
6778 - Which Alien?
'TroyMartian'은 최소 3개의 안테나와 최대 4개의 눈을 가지고 있고
'VladSaturnian'은 최대 6개의 안테나와 최소 2개의 눈을 가지고 있고
'GraemeMercurian'은 최대 2개의 안테나와 최대 3개의 눈을 가지고 있다
목격자가 본 어떤 Alien의 안테나 수와 눈의 수가 두 줄에 걸쳐 주어졌을 때,
답이 될 수 있는 Alien의 이름을 모두 출력해야 하는 문제
'''

import sys

antenna = int(sys.stdin.readline())
eye = int(sys.stdin.readline())

if antenna >= 3 and eye <= 4:
    print('TroyMartian')
if antenna <= 6 and eye >= 2:
    print('VladSaturnian')
if antenna <= 2 and eye <= 3:
    print('GraemeMercurian')
