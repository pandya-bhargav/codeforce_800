n = int(input())
st = list(int(ele) for ele in input().split(" "))
m = min(st)
M = max(st)
total = M-m+1
num = total - n
print(num)

