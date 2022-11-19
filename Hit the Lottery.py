dollar = int(input())
count = 0
notes = [100,20,10,5,1]
for ele in notes:
    count=count+dollar//(ele)
    dollar = dollar%ele
print(count)