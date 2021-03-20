def merge_sort():
    if len(li) <= 1:
        return li
    mid  = len(li)//2
    left_li = list[:mid]
    right_li = list[mid:]
    left_li = merge_sort(left_li)
    right_li = merge_sort(right_li)

n =int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def cutting(x, y, n):
    check = paper[x][y]
    for i in range(n):
        for j in range(n):
            if check != paper[i][j]:
                cutting(x, y, n//2)

        