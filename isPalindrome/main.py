def isPalindrome():
    n = input()
    m = len(n)-1
    flag = True
    for x in range(len(n)):
        if n[x] != n[m]:
           flag = False
        m = m-1
    if flag == True:
        print("Yes")
    else:
        print("No")

t = int(input())
while t > 0:
    isPalindrome()
    t = t-1
    