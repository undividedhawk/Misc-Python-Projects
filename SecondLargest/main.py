def secondLargest():
    n = int(input())
    a = [int(x) for x in input().split()]
    max = 0
    secondLargest = 0
    temp = 0
    for x in range(n):
        if a[x] > secondLargest:
            secondLargest = a[x]
        if secondLargest > max:
            temp = secondLargest
            secondLargest = max
            max = temp
    print(secondLargest)
t = int(input())
while t > 0:
    secondLargest()
    t = t-1