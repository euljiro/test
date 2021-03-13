
memo = {
    1 : 1,
    2: 1,
    3:1,
    4 : 2,
    5:2,
    6 : 3,
    7 : 4,
    8 : 5,
    9 : 7,
    10 : 9
}

def wave(n, memo):
    if n in memo:    #메모라는 딕셔너리에 n값이 있으면 리턴
        return memo[n]
    
    nth_wave = wave(n-1, memo) + wave(n-5, memo) #n번째 값 계산
    memo[n] = nth_wave #memo딕셔너리에 n번째 키값에 nth_wave라는 밸류 저장

    return nth_wave #memo 딕셔너리의 밸류 값들로 계산한 nth_wave 호출

case = int(input())

for i in range(case):
    n = int(input())
    print(wave(n, memo))