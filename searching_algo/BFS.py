from collections import defaultdict 
  
#--class for directed graph with adjacency list representation 
class Graph: 
	
    #--Constructor of the class
    def __init__(self): 
        #--default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    '''
    --function to add an edge
    --inputs, starting point of the graph
    '''
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    '''
    --to print a BFS of graph
    --inputs, starting point of the graph
    --Prints the BFS starting from the input point
    '''
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
                queue = [] 
  
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
   
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

