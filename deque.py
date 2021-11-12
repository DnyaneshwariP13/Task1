class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addF(self, item):
        self.items.append(item)

    def addR(self, item):
        self.items.insert(0,item)

    def removeF(self):
        return self.items.pop()

    def removeR(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d=Deque()
print(d.isEmpty())
d.addR(4)
d.addR('a')
d.addF('c')
d.addF('camera')
d.addF(False)
print(d.size())
print(d.isEmpty())
d.addR(2498)
d.addR('Dnya')
print(d.removeF())
print(d.removeR())
print(d.removeF())
