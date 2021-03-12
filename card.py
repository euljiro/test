from collections import deque

case = int(input())
card=[]

for i in list(range(1,case+1)):
    card.append(i)
    dq = deque(card)
    for j in range(len(dq)):
        dq.popleft()
        dq.rotate(-1)
        if len(dq) == 1:
            break
print(dq)


import collections
from collections import deque


dq = collections.deque(i for i in range(case))


while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)

print(dq[0]+1)
    
