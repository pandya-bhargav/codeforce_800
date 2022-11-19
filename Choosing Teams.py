n , k = input().split()
n = int(n)
k = int(k)
st = input()
arr = []
for i in range(0,len(st),2):
    arr.append(int(st[i]))
count = 0
for ele in arr:
    if (ele+k)<=5:
        count+=1
team = count//3
print(team)        