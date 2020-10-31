'''
9735 - 삼차 방정식 풀기
삼차 방정식 Ax^3 + Bx^2 + Cx + D = 0 가 있을 때,
A, B, C, D가 주어지면 모든 실수 해를 출력해야 하는 문제
단, 위의 방정식은 정수 해를 적어도 한 개 가진다

모든 해의 범위는 (-1000000 ~ 1000000)이고, 적어도 한 개의 정수 해를 가진다고 했으므로
먼저 반복문을 통해 위 방정식을 만족하는 정수 해 x1을 찾는다.
x1을 찾으면, 조립제법에 의해 위 방정식은
(x - (x1))(x^2 + ((x1)*A + B)*x + ((x1^2)A + (x1)*B + C)) = 0 으로 인수분해될 수 있다.

일차식*이차식의 꼴로 인수분해가 되었으므로
뒤의 이차식의 계수를 순서대로 new_a, new_b, new_c로 둔다.

discriminant() 함수에 new_a, new_b, new_c를 전달하고
판별식을 통해 실근을 가지는 지, 중근을 가지는 지, 허근을 가지는 지 확인한다.

허근을 가질 경우 실근 하나만 출력한다.

실근이나 중근을 가질 경우
quardatitc() 함수에서 근의 공식을 활용하여 해를 구한 뒤 res에 추가한다.
리스트 res를 set으로 바꾼 뒤 다시 list로 바꾸는 과정에서 중복을 제거하고, 오름차순으로 정렬한다.
마지막으로 모든 실수 해를 출력한다.

'''

import math, sys

def discriminant(a, b, c):
    dis = b**2 - 4*a*c

    if dis > 0:
        return 'realnum'
    elif dis == 0:
        return 'mulroot'
    else:
        return 'imagnum'

def quardatic(a, b, c):
    root = math.sqrt(b**2 - 4*a*c)
    return ((-b + root) / (2*a)), ((-b - root) / (2*a))

t = int(sys.stdin.readline()) # test case

for i in range(t):
    res = []
    x1 = 0
    a, b, c, d = map(int, sys.stdin.readline().split())

    for j in range(-1000000, 1000001):
        if (a*(j**3) + b*(j**2) + c*j + d == 0):
            x1 = float(j)
            break

    new_a, new_b, new_c = a, (x1*a + b), (x1**2*a + x1*b + c)

    state = discriminant(new_a, new_b, new_c)

    if state == 'imagnum':
        print('%.4f'%x1)
        continue
    else:
        x2, x3 = quardatic(new_a, new_b, new_c)
        res.append(x1)
        res.append(x2)
        res.append(x3)
        res = list(set(res))
        res.sort()
        if len(res) == 1:
            print('%.4f'%res[0])
        elif len(res) == 2:
            print('%.4f'%res[0], '%.4f'%res[1])
        else:
            print('%.4f'%res[0], '%.4f'%res[1], '%.4f'%res[2])
