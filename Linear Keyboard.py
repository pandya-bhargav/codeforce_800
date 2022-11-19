n = int(input())
arr = []
ans = []
for i in range(2*n):
    k = input()
    arr.append(k)

for j in range(1,len(arr),2):

    keyboard = arr[j-1]
    string = arr[j]
    count = 0
    for k in range(len(string)-1):
        count = count + abs(keyboard.index(arr[j][k]) - keyboard.index(arr[j][k+1]))
    ans.append(count)
print(ans)

        





