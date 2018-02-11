def checkProduct():
    n , p = input().split()
    n = int(n)
    p = int(p)
    a = [int(x) for x in input().split()]
    for x in a:
        for y in a:
            if x*y == p:
                print("Yes")
                return 0
    print("No")
    return 0

t = int(input())
while t > 0:
    checkProduct()
    t = t-1

