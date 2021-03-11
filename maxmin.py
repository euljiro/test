case=int(input())
type = list(map(int,input().split()))

maxi=type[0]
mini=type[0]
for i in type:
    if i > maxi:         
        maxi = i
    if i < mini:
        mini = i
    
print(maxi, mini)


# case=int(input())
# type = list(map(int,input().split()))
# print("{} {}".format(min(type),max(type)))