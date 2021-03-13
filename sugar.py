sugar = int(input())

if 3 < sugar < 5:
    print("-1")

elif sugar % 5 == 0 :
    print(sugar//5)

elif sugar % 3 == 0 :
    if sugar < 10:
        print(sugar//3)
    else:
        for i in range(sugar):
            k = sugar - 5*i
            if 3<= k < 5:
                break
        print(i)

else:
    for i in range(sugar):
        k = sugar - 5*i  #5로 나눈 나머지 값 -> sugar%5
        if k % 3 == 0 :
            print(i + k//3 )
            break
        else:
            print("-1")
            break




n = int(input())
# 초기화
five = 0
three = 0
 
# 최대 5kg의 갯수와 나머지를 구한다.
five = n//5
b = n%5
 
# 나머지가 0이 아니면 3kg 갯수를 구한다.
if b !=0:
    while five >= 0:
        if b%3 == 0:
            three = b//3
            break
        five -= 1  #5로 나눈 나머지 값이 3의 배수가 아니면 -1 될때까지 빼준다
        b += 5 # 나머지가 3으로 나누어 떨어질때 까지 5를 더해서 다시 구한다.어떻게 이런 생각을?
            
ret=five + three
 
if ret < 1:
    ret = -1
print(ret)



# sugar = int(input())

# k = sugar//5
# j = sugar%5

# if j != 0:
#     bag = 0
#     if j%3 == 0 :
#         bag = j //3
#         print(k + bag)
    
#     elif sugar%3 == 0 :
#         print(sugar//3)
    
#     elif
    
#     else:
#         print("-1")

# else:
#     print(k)
        







# order = int(input())

# if order % 5 == 0:
#     print(order // 5)

# elif order % 5 == 3:
#     print(order // 5 + 1)

# elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 6:
#     print((order // 5 - 1) + 2)

# elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 9:
#     print((order // 5 - 1) + 3)

# elif order // 5 - 2 >= 0 and order - (5 * (order // 5 - 2)) == 12:
#     print((order // 5 - 2) + 4)

# else:
#     print(-1)








a = int(input())
box = 0
while True:
  if a%5 ==0:
    box = box + (a//5)
    print(box)
    break
  a = a - 3
  box += 1
  if a < 0:
    print("-1")
    break






# def sugar(N) :
#     for y in range( (N//3)+1) :
#         for x in range( (N//5)+1 ) :
#             if ((5*x + 3*y) == N) :
#                 return x+y
            
#     return -1

# N = int(input()) #배달해야할 설탕 킬로그램         
# print(sugar(N))
