import math
import sys
import collections
from collections import Counter

case = int(sys.stdin.readline())
li = []

for i in range(case):
    n = int(sys.stdin.readline())
    li.append(n)

li.sort()
maxim = Counter(li).most_common()

print(round(sum(li)/case))
print(li[case//2])
if len(maxim) > 1:
    if maxim[0][1] == maxim[1][1]:
        print(maxim[1][0])
    else:
        print(maxim[0][0])
else:
    print(maxim[0][0])
        
print(li[-1] - li[0])
