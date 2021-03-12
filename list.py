# case = int(input())
# location = []

# for i in range(0,case):
#     num = int(input())
#     location.append(num)


# for i in range(len(location)):
#     j=i
#     index= location[i]
#     while j > 0 and location[j-1] > index:
#         location[j] = location[j-1]
#         j-=1
#     location[j] = index

# print(location)

# case = int(input())
# location = []


case = int(input())
location = []

for i in range(case):
    num = int(input())
    location.append(num)

location = sorted(set(location))

for i in location:
    print(i)