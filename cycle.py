a = int(input())
c=a   #사이클을 계산하기 위한 변수로 전환
count=1

while True:
    b = (c // 10) + (c % 10)
    c= (c%10)*10 + b%10
    if a == c:     #처음 인풋했던 값과 c를 비교하기 위해서
        break
    count+=1

print(count)