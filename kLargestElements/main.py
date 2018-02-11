def printKLargest():
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = [int(x) for x in input().split()]
    mergeSort(a)
    a.reverse()
    print(a[:k])


def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        leftHalf = a[:mid]
        rightHalf = a[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0
        j=0
        k=0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                a[k] = leftHalf[i]
                i = i+1
            else:
                a[k] = rightHalf[j]
                j = j+1
            k = k+1

        while i < len(leftHalf):
            a[k] = leftHalf[i]
            i = i+1
            k = k+1

        while j < len(rightHalf):
            a[k] = rightHalf[j]
            j = j+1
            k = k+1

t = int(input())
while t > 0:
    printKLargest()


