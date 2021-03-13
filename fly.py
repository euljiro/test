import math

case=int(input())

for i in range(case):
    a, b = map(int, input().split())
    real_dis = b - a
    root = math.floor(math.sqrt(real_dis))
    
    if real_dis < 4 :
        dis = real_dis
        print(dis)
    
    elif real_dis == root**2:
        dis = (root*2) - 1
        print(dis)

    elif real_dis <= root + root**2:
        dis = root*2
        print(dis)

    elif real_dis > root + root**2:
        dis = root*2 +1
        print(dis)



t = int(input())# 테스트 케이스의 갯수를 받음

for _ in range(t): #for 문을 받은 케이스 수만큼 돌린다
    x, y = map(int,input().split())# 지점의 값을 받는다 
    distance = y - x # 이동해야하는 거리가 나온다
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance : #이동한 거리의 합이 이동해야하는거리 보다 작으면 
        count += 1 #이동횟수를 하나 늘린다
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)



        

