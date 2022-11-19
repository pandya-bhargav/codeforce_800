year= int(input())
for i in range(year+1,9013):
    if len(set(str(i)))!=4:
        i+=1
    else:
        print(i)
        break


