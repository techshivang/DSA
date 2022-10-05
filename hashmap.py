## Hashmap in Python
'''
In Python, Dictionray uses Hashmap Function and its time complexity or look up Time is : O(1)
'''

'''
Collision Detection : when Two have same hashKey
For eg:
'march 16' : 20 ------> hashKey = 9
'march 17' : 24 ------> hashKey = 9
Here both having different value but same hashKey
Solution :
(a) : Linear Chaning : Store Same key & value as a tuple -->(key,value) and make a Linked List. 
(b) : Linear Probing : Store Same key('march 6') & value('hashkey') as a tuple but not make a LinkedList and search for empty slots.
'''

class HashMap:
    def __init__(self):
        self.MAX_LIMIT = 10
        self.arr = [None]*self.MAX_LIMIT
    
    def getHashKey(self,string):
        sum = 0
        for char in string:
            sum += int(ord(char))
        return sum % self.MAX_LIMIT
    
    def __setitem__(self,key,val):
        loc = self.getHashKey(key)
        self.arr[loc] = val
    
    def __getitem__(self,key):
        loc = self.getHashKey(key)
        return self.arr[loc]
    
    def __delitem__(self,key):
        loc = self.getHashKey(key)
        self.arr[loc] = None
        return self.arr[loc]
data = HashMap()
print("Getting Hashkey of March 6 :",data.getHashKey("march 6"))
data["march 6"] = 320
data["march 7"] = 321
data["march 8"] = 322

print("value of march 6 :",data['march 6'])    
print("value of march 7 :",data['march 7'])    
print("value of march 8 :",data['march 8'])
del data['march 6']
print("Delete value of march 6 :",data['march 6'])

## But Here one issue occur
print("Getting Hashkey of March 6 :",data.getHashKey("march 6"))  ## ----> return hashkey = 9
print("Getting Hashkey of March 17 :",data.getHashKey("march 17")) ## ----> return hashkey = 9
data["march 6"] = 320
data["march 17"] = 321
print(data['march 6']) # return 321
'''
So here for both key "march 6" && "march 17" hashkey is same so this problem is known as Collision Detection
So we need to fix our solution to handle with this problem.
'''

class LinearChaining:
    def __init__(self):
        self.MAX_LIMIT = 10
        self.arr = [[None] for i in range(self.MAX_LIMIT)]
        
    def getHashKey(self,string):
        sum = 0
        for char in string:
            sum += int(ord(char))
        return sum % self.MAX_LIMIT
    
    def __setitem__(self,key,val):
        loc = self.getHashKey(key)
        found = False
        for idx,element in enumerate(self.arr[loc]):
            if element is not None:
                if(len(element) == 2 and element[0] == key):
                    self.arr[loc][idx] = (key,val)
                    found = True
        if not found:
            if self.arr[loc][0] is None:
                self.arr[loc][0] = (key,val)
            else:
                self.arr[loc].append((key,val))
    
    def __getitem__(self,key):
        loc = self.getHashKey(key)
        for elem in self.arr[loc]:
            if(elem):
                if(elem[0] == key):
                    return elem[1]
    
    def __delitem__(self,key):
        loc = self.getHashKey(key)
        for idx,elem in enumerate(self.arr[loc]):
            if(elem):
                if(elem[0] == key):
                    del self.arr[loc][idx]
                    break
class LinearProbing:
    def __init__(self):
        self.MAX_LIMIT = 10
        self.arr = [None]*self.MAX_LIMIT
        
    def getHashKey(self,string):
        sum = 0
        for char in string:
            sum += int(ord(char))
        return sum % self.MAX_LIMIT
            
    def __setitem__(self,key,val):
        loc = self.getHashKey(key)
        if self.arr[loc] is None:
            self.arr[loc] = (key,val)
        else:
            if(loc == len(self.arr)):
                for i in range(0,loc):
                    if(self.arr[i] is None):
                        self.arr[i] = (key,val)
                        return
            else:
                for i in range(0,len(self.arr)):
                    if i == loc:
                        continue
                    else:
                        if(self.arr[i] is None):
                            self.arr[i] = (key,val)
                            return
    
    def __getitem__(self,key):
        for i in self.arr:
            if i:
                if(i[0] == key):
                    return i[1]
    
    def __delitem__(self,key):
        for i in range(len(self.arr)):
            if self.arr[i]:
                if(self.arr[i][0] == key):
                    self.arr[i] = None
                    return

             
    
                    
                
             
'''
Linear Chaning
'''        

data = LinearChaining()    
data["march 6"] = 320
data["march 17"] = 321
print(data['march 6'])
print(data['march 17'])
print("updating the value !!")
data["march 17"] = 420
print(data['march 17'])
print(data.arr)
print("deleting the value")
del data["march 6"]
print(data.arr)

'''
Linear Probing
'''

data = LinearProbing()
print(data.arr)
data["march 6"] = 320
data["march 17"] = 321
print(data.arr)
print(data['march 6'])
print(data["march 17"])
print("deleting the value")
del data["march 6"]
print(data.arr)