n1 = input()
n2 = input()
ans = ""
for i in range(len(n1)):
    if n1[i]!=n2[i]:
        ans = ans+"1"
    else:
        ans=ans+"0"
print(ans)
