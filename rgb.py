case = int(input())
street=[]

for i in range(case):
    house = list(map(int, input().split()))
    street.append(house)

for i in range(1,len(street)):
    street[i][0] = street[i][0] + min(street[i-1][1], street[i-1][2])
    street[i][1] = street[i][1] + min(street[i-1][0], street[i-1][2])
    street[i][2] = street[i][2] + min(street[i-1][0], street[i-1][1])

print(min(street[case-1][0], street[case-1][1], street[case-1][2]))
