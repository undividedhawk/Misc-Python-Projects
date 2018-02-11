# Find the Odd Occurence from http://practice.geeksforgeeks.org/problems/find-the-odd-occurence/0
# Given an array of positive integers. All numbers occur even number of times
# except one number which occurs odd number of times. Find the number.


def largest(a):
    lg = 0
    for x in range(len(a)):
        if lg <= a[x]:
            lg = a[x]
    return lg


def hashFunction(value, a):
    lg = largest(a)
    return(value % lg)

def makehashtable(a):
    result = 0
    hashed = [None] * largest(a)
    counter = [0] * largest(a)
    for index, item in enumerate(a):
        if hashed[hashFunction(item, a)] is None:
            hashed[hashFunction(item, a)] = item
        counter[hashFunction(item, a)] = (counter[hashFunction(item, a)]) + 1
    print(hashed)
    for value in counter:
         if value % 2 != 0:
            result = hashed[hashFunction(item, a)]
    print(result)
    print(counter)

test = [int(x) for x in input("Please enter an array of size N: ").split()]
hashFunction(13, test)
makehashtable(test)
