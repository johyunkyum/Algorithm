import math
import sys
from lib2to3.pytree import Base


q1 = """2
-5 1 12 1
7
1 1 8
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
-5 1 5 1
1
0 0 2"""

q2 = """3
-5 1 5 1
3
0 0 2
-6 1 2
6 2 2
2 3 13 2
8
-3 -1 1
2 2 3
2 3 1
0 1 7
-4 5 1
12 1 1
12 1 2
12 1 3
102 16 19 -108
12
-107 175 135
-38 -115 42
140 23 70
148 -2 39
-198 -49 89
172 -151 39
-179 -52 43
148 42 150
176 0 10
153 68 120
-56 109 16
-187 -174 8"""

a1 = """3
0"""
a2 = """2
5
3"""


def solution(question):
    """
        내부에 점이 존재하면 Count + 1
    """
    q = question.split('\n')
    case_len = int(q.pop(0))

    for case in range(case_len):
        print(f'Test Case #{case}')
        x1, y1, x2, y2 = map(lambda x: int(x), q.pop(0).split())

        print(f'x1 : {x1}, y1 : {y1}')
        print(f'x2 : {x2}, y2 : {y2}')

        planet_len = int(q.pop(0))

        print(f'Planet ({planet_len}) : ')
        count = 0
        for planet in range(planet_len):
            px, py, r = map(lambda x: int(x), q.pop(0).split())

            print('X : {} Y : {} R : {} 거리: {}'.format(
                px, py, r,
                math.sqrt((px-x1)**2 + (py-y1)**2)
            ))

            d1 = math.sqrt((px-x1)**2 + (py-y1)**2)
            d2 = math.sqrt((px-x2)**2 + (py-y2)**2)

            if (d1 < r < d2) or (d2 < r < d1):
                count += 1

        print(f'Count : {count}\n\n')


def submit():
    """

import sys
import math

case_len = int(sys.stdin.readline())

for case in range(case_len):
    x1, y1, x2, y2 = map(lambda x : int(x), sys.stdin.readline().split(' '))
    planet_len = int(sys.stdin.readline())
    count = 0
    for planet in range(planet_len):
        px, py, r = map(lambda x : int(x), sys.stdin.readline().split(' '))
        d1 = math.sqrt((px-x1)**2 + (py-y1)**2)
        d2 = math.sqrt((px-x2)**2 + (py-y2)**2)


        if (d1 < r < d2) or (d2 < r < d1):
            count +=1

    print(count)
    """


def solve():
    solution(q1)
    solution(q2)
    # submit()
