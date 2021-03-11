case = int(input())

for i in range(case):
    score = list(map(int,input().split()))
    average = sum(score[1:])/score[0]
    count = 0
    for j in score[1:]:
        if j > average:
            count += 1
    over= count / score[0] * 100
    print(f'{over:.3f}%')