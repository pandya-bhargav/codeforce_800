n = int(input())
sum = 0
# for i in range(1,n+1):
#     sum = sum + i*((-1)**(i))
# print(sum)
if n%2 == 0:
    k = n/2
    sum = k*(k+1)
    sum = sum-k**2
else:
    k =(n+1)/2
    sum = k**2
    sum = k*(k-1)-sum
print(int(sum))