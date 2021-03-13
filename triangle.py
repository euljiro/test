case = int(input())
row = []

for i in range(case):
    tri=list(map(int, input().split()))
    row.append(tri)


for i in range(1,case):
    for j in range(len(row[i])):
        if j == 0:
            row[i][0] = row[i][0] + row[i-1][0]
        elif i == j:
            row[i][j] = row[i][j] + row[i-1][j-1]
        else:
            row[i][j] = row[i][j] + max(row[i-1][j], row[i-1][j-1])

print(max(row[case-1][:]))





