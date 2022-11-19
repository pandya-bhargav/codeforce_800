n = input()
arr = [int(x) for x in input().split()]
string = str(arr)
count = string.count('1')
if count!=0:
    print("HARD")
else:
    print("EASY")

    