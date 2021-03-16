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



def mini(a, b):
    if b == 0:
        return a
    else:
        return mini(b, a%b)

def maxi(a, b):
    return a*b//mini(a,b)

case= int(input())

for i in range(case):
    x, y = map(int, input().split())
    print(maxi(x, y))