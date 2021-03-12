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







        

