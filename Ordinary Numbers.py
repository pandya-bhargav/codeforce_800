n = int(input())
i = 0
count = 0
while i<n:
    x = int(input())
    for j in range(1,10):
        start = j
        while start <= n:
            count+=1
            start = start*10+i
    print(count) 
    i+=1


    

        

