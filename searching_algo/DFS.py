from collections import defaultdict 
  
class Graph: 
  
    def __init__(self): 
  
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DFSUtil(self,v,visited): 
  
        visited[v]= True
        print v, 
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
  
    def DFS(self,v): 
  
        visited = [False]*(len(self.graph)) 
  
        self.DFSUtil(v,visited) 
  
  
g = Graph()
edges = input("input the number of edges : ")
print "enter nodes with zero based indexing : "
for i in range(edges): 
    a, b = map(int, raw_input().split())
    g.addEdge(a, b) 
  
check = input("DFS check from node : ")
g.DFS(check) 