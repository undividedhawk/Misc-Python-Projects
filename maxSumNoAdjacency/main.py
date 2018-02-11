def maxSum():
    n = int(input())
    a = [int(x) for x in input().split()]
    max = 0
    sum = 0
    k = 2
    while k < n:
        for x in range(0,n, 2):
            sum = sum + a[x]
        k = k + 1
    for x in range(1,n, 2):
        max = max + a[x]
    if max > sum:
        print(max)
    else:
        print(sum)


t = int(input())
while t > 0:
    maxSum()