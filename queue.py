'''
Queue is follwed FIFO (First in First Out)
Opeartions :
    (a) : Enquee -> Add Element 
    (b) : Dequee -> Delete Element
    (c) : isFull --> Check Overflow
    (d) : isEmpty --> Check Underflow
'''

class Queue:
    def __init__(self):
        self.MAX_LIMIT = 10
        self.queue = []
    def enquee(self,data):
        if(len(self.queue) <= self.MAX_LIMIT):
            self.queue.insert(0,data)
        else:
            return "Queue is Full !!"
    def dequee(self):
        if(not self.queue):
            return "Queue is Empty !!"
        else:
            self.queue.pop()
    def display(self):
        return self.queue
    
class PriorityQueue:
    def __init__(self):
        self.priorityQueue = {}
        self.priority = 0
    
    def insert(self,data):
        if not self.priority:
            self.priorityQueue[self.priority] = data
            self.priority +=1
        else:
            self.priorityQueue[self.priority] = data
            self.priority +=1
    
    def delete(self,key=None):
        if self.priorityQueue:
            if key is None:
                firstKey = next(iter(self.priorityQueue))
                del self.priorityQueue[firstKey]
                return self.display()
            else:
                if key in self.priorityQueue:
                    del self.priorityQueue[key]
                    return self.display()
            return None
            
        
            
    
    def display(self):
        return self.priorityQueue
    
data = PriorityQueue()
data.insert(10)
data.insert(20)
print(data.display())
print(data.delete())
print(data.delete())
print(data.delete())
