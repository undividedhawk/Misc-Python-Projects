def findMissingNumber():
    n = int(input())
    a = [int(x) for x in input().split()]
    for x in range(n-2):
        if a[x] != a[x+1]-1:
            print(a[x]+1)
        elif a[x] == a[x+1]-1 and x+2 == n-1:
            print(a[x+1]+1)

t = int(input())
while t > 0:
    findMissingNumber()
    t = t-1