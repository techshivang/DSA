'''
Singluar Linked List ===========> [node] + reference_node
Doubly Linked List ===========> prev_node + [node] + reference_node

Eg : [20 | ref_node]----->[30 | ref_node]----->[40 | ref_node]------> Null

Types of Linked List :
(a) : Single Linked List
(b) : Doubly Linked List
(c) : Circular Linked List

Operation on Linked List :
(a) : Add element in Linked List
      * Add element at begining.
      * Add element at end.
      * Add element in between two nodes
        (a) : after node
        (b) : before node
(b) : Delete element in Linked List
      * Del element at begining.
      * Del element at end.
      * Del element in between two nodes
(c) : Traversal in Linked List
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.reference = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_begin(self,data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.reference is not None:
            node = node.reference
        node.reference = new_node
    def add_after(self,data,x):
        node = self.head
        while node:
            if node.data == x:
                break
            node = node.reference
        if node is None:
            print("Node is not present in the linked list !!")
        else:
            new_node = Node(data)
            new_node.reference = node.reference
            node.reference = new_node
    def add_before(self,data,x):
        if self.head is None:
            return
        if self.head.data == x:
            self.add_begin(data)
            return
        node = self.head
        while node.reference is not None:
            if node.reference.data == x:
                break
            node = node.reference
        if node.reference is None:
            print("Node is not present in the linked list !!")
        else:
            new_node = Node(data)
            new_node.reference = node.reference
            node.reference = new_node
    def add_nodes(self,data_list):
        if self.head is None:
            for data in data_list:
                self.add_end(data)
        else:
            print("Linked List is Not Empty !!")
            
    def del_begin(self):
        if self.head is not None:
            first_node = self.head
            self.head = first_node.reference
        else:
            print("Linked List is Empty !!")
    
    def del_end(self):
        if self.head is not None:
            node = self.head
            while node:
                if node.reference.reference is None:
                    break
                node = node.reference
            node.reference = None
    
    def del_after(self,x):
        if self.head is None:
            print("Linked List is Empty !!")
            return
        node = self.head
        while node:
            if node.data == x:
                break
            node = node.reference
        if node is None:
            print("Node is not present !!")
        else:
            node.reference = node.reference.reference
    
    def del_before(self,x):
        if self.head is None:
            print("Linked List is Empty !!")
            return
        if self.head.data == x:
            print("Can't delete before first Node !!")
            return
        node = self.head
        while node.reference is not None:
            if node.reference.data == x:
                break
            node = node.reference
        if node is None:
            print("Node is not present !!")
        else:
            if node.data == self.head.data:
                self.head = self.head.reference
            else:
                node.reference = node.reference.reference
    
    def del_value(self,x):
        if self.head is None:
            print("Linked List is Empty!!")
            return
        if self.head.data == x:
            self.head = self.head.reference
            return
        node = self.head
        while node:
            if node.reference.data == x:
                break
            node = node.reference
        if node is None:
            print("Value is not present in linked list !!")
        else:
            if node.reference.reference == None:
                self.del_end()
            else:
                node.reference = node.reference.reference
        
            
            
            
    def getLinkedList(self):
        if self.head is not None:
            node = self.head
            llist = ""
            while node:
                llist += str(node.data) +"--->"
                node = node.reference
            print(llist)
            
class Node_Doubly:
    def __init__(self,data):
        self.data = data
        self.prev_ref = None
        self.next_ref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        if self.head is None:
            new_node = Node_Doubly(data)
            self.head = new_node
        else:
            new_node = Node_Doubly(data)
            new_node.next_ref = self.head
            self.head.prev_ref = new_node
            self.head = new_node
    def insert_end(self,data):
        if self.head is None:
            self.insert_begin(data)
        else:
            node = self.head
            while node.next_ref is not None:
                node = node.next_ref
            new_node = Node_Doubly(data)
            if node.prev_ref is None:
                node.next_ref = new_node
                new_node.prev_ref = node
            else:
                new_node.prev_ref = node
                node.next_ref = new_node
    
    def insert_after(self,data,x):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.data == x:
            new_node = Node_Doubly(data)
            new_node.next_ref = self.head.next_ref
            self.head.next_ref = new_node
        else:
            node = self.head
            while node.data != x:
                node = node.next_ref
            if node is None:
                print("Node is not find in list !!")
                return
            new_node = Node_Doubly(data)
            if node.next_ref is None:
                new_node.prev_ref = node
                node.next_ref = new_node
            else:
                new_node.next_ref = node.next_ref
                node.next_ref = new_node
                
    def insert_before(self,data,x):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.data == x:
            new_node = Node_Doubly(data)
            new_node.next_ref = self.head
            self.head = new_node
        else:
            node = self.head
            while node:
                if node.next_ref.data == x:
                    break
                node = node.next_ref
            if node is None:
                print("Node is not present in list !!")
            else:
                new_node = Node_Doubly(data)
                new_node.next_ref = node.next_ref
                node.next_ref = new_node
                
    def del_begin(self):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.next_ref is None:
            self.head = None
        else:
            self.head = self.head.next_ref
           
    def del_end(self):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.next_ref is None:
            self.head = None
        else:
            node = self.head
            while node.next_ref.next_ref is not None:
                node = node.next_ref
            node.next_ref = None
            
    
    def del_after(self,x):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.data == x:
            if self.head.next_ref == None:
                print("There is no node present !!")
            else:
                self.head = self.head.next_ref
        else:
            node = self.head
            while node:
                if node.data == x:
                    break
                node = node.next_ref
            if node is None:
                print("Value is not present in the list !!")
            else:
                if node.next_ref.next_ref is None:
                    node.next_ref = None
                else:
                    node.next_ref = node.next_ref.next_ref
    
    def del_before(self,x):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.data == x:
            print("No node is present to delete !!")
            return
        node = self.head
        while node:
            if node.data == x:
                break
            node = node.next_ref
        if node is None:
            print("Node is not present in the list !!")
            return
        if node.prev_ref.data == self.head.data:
            self.head = node
        else:
            node.prev_ref.prev_ref.next_ref = node
            node.prev_ref = node.prev_ref.prev_ref
            
    def del_value(self,x):
        if self.head is None:
            print("Linked List is empty !!")
            return
        if self.head.data == x:
            self.head = self.head.next_ref
            return
        node = self.head
        while node:
            if node.data == x:
                break
            node = node.next_ref
        if node is None:
            print("Node is not present in the list !!")
        else:
            node.prev_ref.next_ref = node.next_ref
            node.next_ref.prev_ref = node.prev_ref
            
    
    def forward_traverse(self):
        if self.head is None:
            print("Linked List is empty!!")
            return
        node = self.head
        llsit = ""
        while node is not None:
            llsit += str(node.data) + "--->"
            node = node.next_ref
        print(llsit)
    
    def backword_traverse(self):
        if self.head is None:
            print("Linked List is empty!!")
            return
        node = self.head
        llsit = ""
        while node.next_ref is not None:
            node = node.next_ref
        
        while node is not None:
            llsit += str(node.data) + "--->"
            node = node.prev_ref
        print(llsit)
              

                
if __name__ == "__main__":
    # root = LinkedList()
    # root.add_begin(20)
    # root.add_begin(30)
    
    # root.add_end(10)
    # root.add_end(20)
    
    # root.add_after(15,10)
    # root.add_before(18,20)
    
    # root.add_nodes([10,20,30,40,50])
    # root.del_begin()
    # root.del_end()
    
    # root.getLinkedList()    
    # root.del_after(20)
    
    # root.getLinkedList()
    # root.del_before(30)
    
    # root.getLinkedList()
    # root.del_value(50)
    
    # root.getLinkedList()
    
    root = DoublyLinkedList()
    # root.insert_begin(10)
    # root.insert_begin(20)
    # root.backword_traverse()
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.backword_traverse()
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.forward_traverse()
    # root.insert_after(40,30)
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.forward_traverse()
    # root.insert_before(40,30)
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.forward_traverse()
    # root.del_begin()
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.forward_traverse()
    # root.del_end()
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.insert_end(40)
    # root.forward_traverse()
    # root.del_after(20)
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.insert_end(40)
    # root.insert_end(50)
    # root.forward_traverse()
    # root.del_before(20)
    # root.forward_traverse()
    
    # root.insert_end(10)
    # root.insert_end(20)
    # root.insert_end(30)
    # root.insert_end(40)
    # root.insert_end(50)
    # root.forward_traverse()
    # root.del_value(20)
    # root.forward_traverse()
