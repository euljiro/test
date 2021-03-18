n, m = map(int, input().split())
check = [False]*n
ans = [0]*m


def nm(idx):
          
    if idx == m:
        print(*ans)
        return

    for i in range(n):
        if check[i]:
            continue
        else:
            check[i] =True
            ans[idx] = i+1

        nm(idx+1)

        for j in range(i+1, n):
            check[j] = False

nm(0)

