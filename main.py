# Реализовать стек и очередь с помощью списка.
# Filo - стек стр 6-23
# Fifo - очередь стр 26-43
# проверка стр 46-59

class Filo:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_filo(self):
        print(self.items)
##########################################################

class Fifo:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_fifo(self):
        print(self.items)
###########################################################

stek = Filo()
stek.push(1)
stek.push(2)
stek.push(3)
stek.print_filo()
print(stek.size())

queue = Fifo()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print_fifo()
print(queue.size())