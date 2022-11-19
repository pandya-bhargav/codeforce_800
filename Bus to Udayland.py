n = int(input())
arr = []
count = 0
for i in range(n):
    seats = input()
    if count==0:
        if (seats[0]=='O' and seats[1]=='O'):
            arr.append('++|'+seats[-2]+seats[-1])
            count+=1
        elif (seats[-1]=='O' and seats[-2]=='O'):
            arr.append(seats[0]+seats[1]+'|++')
            count+=1
        else:
            arr.append(seats)
    else:
        arr.append(seats)
if count > 0:
    print("YES")
    for ele in arr:
        print(ele)
else:
    print("NO")


    