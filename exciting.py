import sys

def w(a, b, c):
    global mem  #함수 안에서의 전역 변수/보통 함수안에 있는 건 지역 변수/함수가 끝나고 없어지지 않는다.

    if (a, b, c) in mem.keys():   #저장된 key 값들을 불러온다
        return mem[(a, b, c)]
    
    if a <= 0 or b <= 0 or c<= 0:    
        return 1

    elif a > 20 or b > 20 or c > 20:
        mem[(20, 20, 20)] = w(20, 20, 20)
        return mem[(20, 20, 20)]

    elif a < b < c:
        mem[(a, b, c)] = w(a, b ,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return mem[(a, b, c)]

    else: 
        mem[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mem[(a, b, c)]

    return mem[(a, b, c)]

while True:
    x, y, z = map(int, sys.stdin.readline().split())

    if x == -1 and y == -1 and z == -1:
        break

    mem = dict() #mem 호출/딕셔너리는 리스트, 튜플과 다르게 key값으로 value를 얻는다.dict((a,x),(b,x),(c,x))
    print('w({}, {}, {}) = {}'.format(x, y, z, w(x, y, z)) )