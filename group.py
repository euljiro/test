n=int(input())
count=0

for i in range(n):
    word=input()
    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                    break     
        else:
            count+=1
            
print(count)
        # if word[k] != li[j]:
        #     count += 1
        #     print(word[k],li[j],count)


                
