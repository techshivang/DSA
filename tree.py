'''
* Tree is a non-linear Data Struture.
* It Represents the Releationships Between the Nodes.
* Tree is a Recursive Data Struture.
    Tree Representaion :     
         (a)-----> Root Node(Parent Node) --------> level -0
        /   \
       (b)  (c) ----------------------------> level-1
      /       \
     (d)      (e) --------------------------> level-2
      |        |  
      |        |
      |        |
      Leaf Node Leaf Node
Basic Terms :

## Degree :
    * Degree of a Node => No of Children contain by that Node
    * Degree of a Tree => Heighest Degree of a Node
    
## Height :
   * Height of a Node => Longest path from leaf node to that Node (No. of Edges include in the path).
   * Height of a Tree => Height of a Root Node.
   * Height of a leaf node => 0
   
## Depth :
   * Depth of a Node => No. of edges present from Root Node to that Node.
   * Depth of a Root Node => 0
   * Depth of a Tree => No. of edges present from Root Node to leaf Node.
   
## Types of a Binary Tree :
   (a) : Full Binary Tree 
   (b) : Complete Binary Tree
   (c) : Perfect Binary Tree
   (d) : Balanced Binary Tree
   (e) : Pathalogical Binary Tree or Degenerate Binary Tree
   
## Binary Search Tree
   ## Operations:
      (a) : Traversal
            (a) : Pre-Order-Traversal ===> RootNode--->LeftSubTree--->RightSubTree
            (b) : In-Order-Traversal  ===> LeftSubTree--->RootNode--->RightSubTree
            (c) : Post-Order-Traversal ===> LeftSubTree--->RightSubTree--->RootNode
            (d) : Level-Order-Traversal ====> Level by Level Traversal Done
      (b) : Insertion
      (c) : Searching
      (d) : Deletion
   
## No. of Nodes in a Binary Tree = (No. of Nodes in Left-Sub-Tree + No. of Nodes in Right-Sub-Tree + RootNode)
## Highest Node in a Binary Tree = Search on Right Sub Tree if R.S.T is Null then Root Node.
## Lowest Node in Binary Tree = Search on Left Sub Tree if L.S.T is Null then Root Node.

'''

class BST:
   def __init__(self,key):
      self.key = key
      self.left_child = None
      self.right_child = None
   
   def insert(self,data):
      if self.key == None:
         self.key = data
         return
      if self.key == data:
         return
      else:
         if self.key > data:
            if self.left_child is None:
               self.left_child = BST(data)
            else:
               self.left_child.insert(data)
         else:
            if self.right_child is None:
               self.right_child = BST(data)
            else:
               self.right_child.insert(data)
               
   def search(self,data):
      if self.key is None:
         return
      if self.key == data:
         print("Node is Found",self.key)
      else:
         if self.key > data:
            if self.left_child:
               self.left_child.search(data)
            else:
               return None
         else:
            if self.right_child:
               self.right_child.search(data)
            else:
               return None
      return None
   
   def preOrderTraversal(self):
      if self.key is None:
         return None
      else:
         print(self.key,end=" ")
         if self.left_child:
            self.left_child.preOrderTraversal()
         if self.right_child:
            self.right_child.preOrderTraversal()
            
   def inOrderTraversal(self):
      if self.key is None:
         return None
      else:
         if self.left_child:
            self.left_child.inOrderTraversal()
         print(self.key)
         if self.right_child:
            self.right_child.inOrderTraversal()
            
   def postOrderTraversal(self):
      if self.left_child:
         self.left_child.postOrderTraversal()
      if self.right_child:
         self.right_child.postOrderTraversal()
      print(self.key,end=" ")
      
   def delete(self,data,curr_key):
      if self.key is None:
         return None
      if data < self.key:
         if self.left_child:
            self.left_child = self.left_child.delete(data,curr_key)
         else:
            return None
      elif data > self.key:
         if self.right_child:
            self.right_child = self.right_child.delete(data,curr_key)
      else:
         if self.left_child is None:
            temp = self.right_child
            if curr_key == data:
               self.key = temp.key
               self.left_child = temp.left_chile
               self.right_child = temp.right_child
               temp = None
               return temp
            self = None
            return temp
         if self.right_child is None:
            temp = self.left_child
            if curr_key == data:
               self.key = temp.key
               self.left_child = temp.left_chile
               self.right_child = temp.right_child
               temp = None
               return temp
            self = None
            return temp
         node = self.right_child
         while node.left_child:
            node = node.left_child
         self.key = node.key
         self.right_child = self.right_child.delete(node.key,curr_key)
      return self
   
   def numberOfNodes(self,node):
      if self.key is None:
         return 0
      return 1+self.numberOfNodes(node.left_child)+self.numberOfNodes(node.right_child)
   
   def MaxandMin(self):
      MinNode = self.key
      MaxNode = self.key
      current = self
      while current.left_child:
         current = current.left_child
         MinNode = current.key
         
      while current.right_child:
         current = current.right_child
         MaxNode = current.key
      return MaxNode,MinNode
          
root = BST(None)
# print(root.key)
# print(root.left_child)
# print(root.right_child)

nodes = [6,3,1,6,98,3,7]
for i in nodes:
   root.insert(i)

# root.search(30)
# root.preOrderTraversal()
# root.inOrderTraversal()
# root.postOrderTraversal()
# root.delete(98)

## Delete root node when it is leaf node
# if root.numberOfNodes(root) > 1:
#    root.delete(6)
# else:
#    print("Can't perform delete opeartion !!")

print(root.MaxandMin())