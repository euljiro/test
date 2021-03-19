
n=int(input())
memo = {
    1: 1,
    2: 2
}


def tile(n, memo):
    if n in memo:
        return memo[n]

    nth_tile = tile(n - 1,memo) + tile(n - 2,memo)
    memo[n] = nth_tile
    return nth_tile


print(tile(n, memo)%15746)



n=int(input())
m=[0]*1000001
m[1] =1
m[2] = 2

for i in range(3, n+1):
    m[i] = (m[i-1] +m[i-2]) %15746


print(m[n])