class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop(0)

    def push(self, item):
        self.items.insert(0, item)

#peek returns the top element in the stack
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = stack()

def reverseWords():
    a = [input().split(".")]
    for x in range(0,len(a)):
        s.push(a[x])
    for x in range(0,s.size()):
        print(s.pop())

t = int(input())
while t > 0:
    reverseWords()
    t = t - 1
