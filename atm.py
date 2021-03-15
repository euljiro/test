person = int(input())
atm= list(map(int, input().split()))
atm.sort()
minute=0

for i in range(len(atm)):
    minute = minute + atm[i]
    atm[i] = minute

print(sum(atm))

