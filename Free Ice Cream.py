n , x = input().split()
n ,x = int(n) , int(x)
arr = []
i=1
while i<=n:
    k , l = input().split(" ")
    arr.append(k)
    arr.append(int(l))
    i+=1
count =0

for i in range(0 , len(arr) ,2):
    if arr[i] == '+':
        x += arr[i+1]
    else :
        if x < arr[i+1]:
            count+=1
        else:
            x -= arr[i+1]
print(str(x)+" "+str(count))

