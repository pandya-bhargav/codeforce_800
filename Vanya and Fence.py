n,h = input().split()
arr = [int(x) for x in input().split()]
i=0
sum=0
while i<int(n):
    if arr[i] <= int(h):
        sum+=1
    else:
        sum=sum+2
    i+=1
print(sum)