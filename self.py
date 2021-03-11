def self():
    n = 0
    li = []
    for i in range(0,10001):
        if i < 10:
            n = i + i
            li.append(n)
        
        elif i < 100:
            n = i + i//10 + i%10
            li.append(n)
        
        elif i < 1000:
            n = i + i//100 + (i%100)//10 + i%10
            li.append(n)
        
        elif i < 10000:
            n = i + i//1000 + i%1000//100 + i%100//10 + i%10
            li.append(n)
            
            if n <= 10001:
                li.append(n)

            li.sort()
    for j in range(0,10001):
        if j not in li:
            print(j)

self();
            

