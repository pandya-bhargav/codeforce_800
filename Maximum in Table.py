import math
n = int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    k = n*2-2
    print(math.comb(k,n-1))




