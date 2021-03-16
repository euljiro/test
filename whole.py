# n = int(input())
# mea = list(map(int, input().split()))
# a = min(mea)
# b = max(mea)
# print(a*b)


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ



# def mini(a, b):
#     if b == 0:
#         return a
#     else:
#         return mini(b, a%b)

# def maxi(a, b):
#     return a*b//mini(a,b)


# x, y = map(int, input().split())

# print(mini(x, y), maxi(x, y))



# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ



import math

n, k = map(int, input().split())  4개의 구슬  2개의 구슬 뽑는 경우의 수 

bino = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print(bino)  


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import math

case=int(input())

for i in range(case):
    k, n = map(int, input().split())
    bino = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    print(bino)




N, K = list(map(int, input().split()))

up = 1
for i in range(N, N-K,-1): #-1은 내림차순으로 내려가는것 
    up *= i

down = 1
for i in range(1, K+1):
    down *= i

print(up // down)
