def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

all_list = list(range(2,24))
memo = []

for i in all_list:
    if sosu(i):
        memo.append(i)

n = int(input())

while True:
    count=0
    if n == 0 :
            break
    for i in memo:
        if n < i <=2*n:
            count+=1
    print(count)
    n = int(input())
    

    


# b = int(input)

# for i in range(b, 2*b+1):
#     li = []
#     for j in range(2, int(b**0.5)+1):
#         if b%j != 0:
