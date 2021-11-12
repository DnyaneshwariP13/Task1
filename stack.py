class Stack:
    def __init__(self):
        self.d_items=[]

    def isEmpty(self):
        return self.d_items==[]

    def push(self,data):
        self.d_items.append(data)

    def pop(self):
        return self.d_items.pop()

    def top(self):
        return self.d_items[-1]

    def size_stack(self):
        return len(self.d_items)

s=Stack()

print(s.isEmpty())
s.push(2498)
s.push('Dnya')
s.push('Prasad')
s.push('Pawale')
print(s.top())
s.push(True)
s.push(2198)
print(s.size_stack())
print(s.isEmpty())
s.push(1300)
print(s.pop())
print(s.pop())
print(s.size_stack())
