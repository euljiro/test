# case = int(input())

# stack = []

# for i in range(case):
#     n = int(input())

#     if n != 0:
#         stack.append(n)
#         continue
#     else:
#         stack.pop()
#         continue

# print(sum(stack))



case = int(input())

for i in range(case):
        
    n = list(input())
    stack = []
    count = 0

    for j in n:
        if j == '(':
            stack.append(j)
            count+=1

        elif j == ')':
            if len(stack) == 0:
                count-=1
                break

            elif stack[-1] == '(':
                stack.pop()
                count-=1


    if  count==0 and len(stack) ==0 :
        print('YES')
    else:
        print('NO')
