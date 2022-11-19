n = int(input())
arr = []
for i in range(n):
    skill = input().split()
    arr.append(skill)
for ele in arr:
    k = max(int(ele[0]),int(ele[1]))
    l = max(int(ele[-1]),int(ele[-2]))
    if k < int(ele[-1]) and k < int(ele[-2]):
        print("NO")
    elif l < int(ele[0]) and l < int(ele[1]):
        print("NO")
    else:
        print("YES")
