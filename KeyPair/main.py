def findKeyPair():
    keyPair = False
    n , x = input().split()
    n = int(n)
    x = int(x)
    a = [int(x) for x in input().split()]
    c = n-1
    while c >= 0:
        for element in range(0,c):
            if a[c] + a[element] == x:
                keyPair = True
        c = c - 1
    if keyPair:
        print("Yes")
    else:
        print("No")


t = int(input())
while t > 0:
    findKeyPair()