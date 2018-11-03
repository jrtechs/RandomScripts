class Queque:

    def __init__(self):
        self.queque = []


    def enqueue(self, data):
        if data not in self.queque:
            self.queque.append(data)
            return True
        
        return False

    def dequeue(self):
        if len(self.queque) > 0:

            return self.queque.pop(0)
        return ('Queque empty')

    def sizeQueque(self):
        return len(self.queque)
    
    def printQueque(self):
        return self.queque


if __name__ == '__main__':
    myqueque = Queque()

    data = myqueque.enqueue(5)
    data = myqueque.enqueue(6)
    data = myqueque.enqueue(7)
    data = myqueque.enqueue(10)

    print(myqueque.sizeQueque())
    print(myqueque.printQueque())


    dequeue = myqueque.dequeue() # delete 5
    dequeue = myqueque.dequeue() # delete 6


    print(myqueque.printQueque())
    print(myqueque.sizeQueque())
