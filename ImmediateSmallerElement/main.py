def smallElements():
    n = int(input())
    a = [int(x) for x in input().split()]
    for x in range(n):
        if x == (n-1):
            print(-1)
        elif a[x] > a[x+1]:
            print(a[x+1])
        elif a[x] < a[x+1]:
            print(-1)
t = int(input())
while t > 0:
    smallElements()
    t = t-1