'''
* Graph is a Non-Linear Data Struture
* It is a Orderd Pair of Vertices and Edges

** G = (V,E)
## Note:
    {} : unorderd pair
    () : orderd pair

## Application :
    (a) : Google Maps
    (b) : Social Network
    (c) : Ecommerce Website for recommendation
    
## Types of Graphs:
    (a) : Directed Graph   :  All the edges are Unidirectional
    (b) : Undirected Graph :  All the edges are Bidirectional
    
    (a) : Weighted Graph   :  In which each edge is assigned to some weight/cost/value.
    (b) : UNweighted Graph :  In which each edge is not assigned to some weight/cost/value.
    
    (a) : Cyclic Graph     :  If Graph contains the cycle.
    (b) : Acyclic Graph    :  If Graph does not contains the cycle.
    
## Notes : 
  * Tree is a Acylic Graph.
  * All Tree is a Graph.
  * But all Graph is not Tree.
  
## Adjacent Node :
    * Node 'X' is adjacent to Node 'Y' if there is any edge in between from Node 'X' to Node 'Y'.
    
## Length of path => No. of edges or it should be greter than 1 or equal to 1.

## Types of Path :
    (a) : Simple : If all of its vertices are distinct.
    (b) : Close  : If the first and last node of path is same.
    (c) : Cycle  : If contains the cycle.
    
## Connected Graph :
    * A graph is to said to be connected if there is a path from any node to any other node.
    
## Strongly Connected Graph :
    * In a directed graph if there is a path from any node to any other node.
## Weekly Connected Graph :
    * In a directed graph if there is a path exist through which there is not edge from any node to any other node.
    
## Degree of a Node :
    * In Undirected Graph ,Number of edges connected to that Node.
    * In Directed Graph:
        (a) In-Degree : Number of Edges coming to that Node.
        (b) Out-Degree : Number of edges going through that Node.
        
## Complete Graph :
    * If there is a edge between every pairs of Nodes.

## Graph Representation :
    * Adjacency Matrix
        (a) : Create K*K matrix.
        (b) : Row and Column Represents the Nodes of the Graph.
        (c) : If edge is present then store 1 else store 0.
    * Adjacency List
        ** In adjanency list we store only adjancent nodes instead of storing 0 or 1.
        
## Graph Operations
    * Insertion
    * Deletion
    * Traversal
      (a) : DFS
      (b) : BFS
'''

class AdjacencyMatrix:
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.node_count = 0
    def add_node(self,v):
        global node_count
        if v in self.nodes:
            print("Already Present !!")
        else:
            self.node_count += 1
            self.nodes.append(v)
            for n in self.graph:
                n.append(0)
            temp = []
            for i in range(node_count):
                temp.append(0)
            self.graph.append(temp)
            
    def add_edge(self,v1,v2,cost=None,mode="undirected"):
        if v1 not in self.nodes:
            print("node is not present !!")
        elif v2 not in self.nodes:
            print("node is not present !!")
        index_1 = self.nodes.index(v1)
        index_2 = self.nodes.index(v2)
        
        if(mode == "undirected" and cost is None):
            self.graph[index_1][index_2] = 1
            self.graph[index_2][index_1] = 1
        elif(mode == "undirected" and cost is not None):
            self.graph[index_1][index_2] = cost
            self.graph[index_2][index_1] = cost
        elif(mode == "directed" and cost is not None):
            self.graph[index_1][index_2] = cost
        elif(mode == "directed" and cost is None):
            self.graph[index_1][index_2] = 1       
            
    def delete_node(self,v):
        if v not in self.nodes:
            print("node not present !!")
        else:
            index = self.nodes.index(v)
            self.node_count -= 1
            self.nodes.remove(v)
            self.graph.pop(index)
            for i in self.graph:
                i.pop(index)
    def delete_edge(self,v1,v2,mode="undirected"):
        if v1 not in self.nodes:
            print("not present !!")
        elif v2 not in self.nodes:
            print("not present !!")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            if(mode == "undirected"):
                self.graph[index1][index2] = 0
                self.graph[index2][index1] = 0
            else:
                self.graph[index1][index2] = 0
            
            
    def printGraph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j],end=" ")
        print()

class AdjacencyList:
    def __init__(self):
        self.graph = {}
        self.visited = set()
    def addNode(self,vertex):
        if vertex in self.graph:
            print("already present in graph !!")
        else:
            self.graph[vertex] = []
    def add_edge(self,vertex1,vertex2,mode="undirected",cost=None):
        if vertex1 not in self.graph:
            print("vertex not present in graph !!")
        elif vertex2 not in self.graph:
            print("vertex not present in graph !")
        
        if(mode == "undirected" and cost is None):
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        elif(mode == "undirected" and cost is not None):
            list1 = [vertex2,cost]
            list2 = [vertex1,cost]
            self.graph[vertex1].append(list1)
            self.graph[vertex2].append(list2)
        elif(mode == "directed" and cost is not None):
            list1 = [vertex2,cost]
            self.graph[vertex1].append(list1)
        elif(mode == "directed" and cost is None):
            self.graph[vertex1].append(vertex2)
            
    def delete_node(self,vertex,cost=None):
        if vertex not in self.graph:
            print("not present !!")
        else:
            del self.graph[vertex]
            for i in self.graph:
                if(cost is None):
                    if(vertex in self.graph[i]):
                        self.graph[i].remove(vertex)
                else:
                    list1 = self.graph[i]
                    for j in list1:
                        if j == vertex:
                            list1.remove(vertex)
                            break
    
    def delete_edge(self,vertex1,vertex2,mode="undirected",cost=None):
        if vertex1 not in self.graph:
            print("not present !!")
        elif vertex2 not in self.graph:
            print("not present !!")
        else:
            if(mode == "undirected" and cost is None):            
                if vertex2 in self.graph[vertex1]:
                    self.graph[vertex1].remove(vertex2)
                    self.graph[vertex2].remove(vertex1)
            elif(mode == "undirected" and cost is not None):
                temp = [vertex1,cost]
                temp1 = [vertex2,cost]
                if temp1 in self.graph[vertex1]:
                    self.graph[vertex1] = temp1
                    self.graph[vertex2] = temp
            elif(mode != "undirected" and cost is None):
                if vertex2 in self.graph[vertex1]:
                    self.graph[vertex1].remove(vertex2)
            elif(mode != "undirected" and cost is not None):
                temp = [vertex1,cost]
                if temp1 in self.graph[vertex1]:
                    self.graph[vertex1] = temp1     
                    
    def DFS(self,startingNode):
        if startingNode not in self.graph:
            print("Node is not present in the graph !!")
            return
        if startingNode not in self.visited:
            self.visited.add(startingNode)
            print(startingNode)
            for i in self.graph[startingNode]:
                self.DFS(i)
                
                
    def DFSIterative(self,node):
        if node not in self.graph:
            print("Node is Not present in the graph !!")
            return
        stack = []
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in self.visited:
                print(current)
                self.visited.add(current)
                for i in self.graph[current]:
                    stack.append(i)
                        
        
    
    def printGraph(self):
        print(self.graph)



# obj = AdjacencyMatrix()        
# print("Before Adding Node !!")
# print(obj.nodes)
# print(obj.graph)

# obj.add_node("A")
# obj.add_node("B")
# obj.add_node("C")
# obj.add_node("D")
# obj.add_edge("A","B")

# print("After Adding Node !!")
# print(obj.nodes)
# obj.printGraph()

# obj = AdjacencyList()
# print("Before Adding Node !!")
# obj.printGraph()

# obj.addNode("A")
# obj.addNode("B")
# obj.addNode("C")
# obj.addNode("D")
# obj.addNode("E")

# obj.add_edge("A","B","undirected",10)

# print("After Adding Node !!")
# print(obj.printGraph())

## DFS Traversal
# obj = AdjacencyList()
# print("Before Adding Node !!")
# obj.printGraph()

# obj.addNode("A")
# obj.addNode("B")
# obj.addNode("C")
# obj.addNode("D")
# obj.addNode("E")

# obj.add_edge("A","B")
# obj.add_edge("B","E")
# obj.add_edge("A","C")
# obj.add_edge("A","D")
# obj.add_edge("B","D")
# obj.add_edge("C","D")
# obj.add_edge("E","D")

# print("After Adding Node !!")
# obj.printGraph()
# obj.DFS("A")