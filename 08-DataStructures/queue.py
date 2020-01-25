class Queue:

    def __init__(self):
        self.queue = []

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def push(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue)==0
kolejka=Queue()
kolejka.push(3)
kolejka.push(7)
kolejka.push(9)
kolejka.push(4)
kolejka.push(5)
for i in range(3):
    print(kolejka.pop())
