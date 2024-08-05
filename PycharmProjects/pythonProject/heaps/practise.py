class node:
    def __init__(self,val):
        self.data=val
        self.neighbors=[]
class graph:
    def __init__(self):
        self.nodes={}
        self.edges=[]
        self.size=0

    def addnode(self,val):
        if val in self.nodes:
            self.nodes[val]=node(val)
            self.size+=1

    def addedge(self,a,b,weight):
        if a not in self.nodes:
            self.addnode(a)
        if b not in self.nodes:
            self.addnode(b)
        if a in self.nodes and b in self.nodes:
            self.nodes[a].neighbors.append((b,weight))
            self.nodes[b].neighbors.append((a,weight))
            self.edges.append((a,b,weight))
    def deletenode(self,vertex):
        if vertex in self.nodes:
            for n,w in self.nodes[vertex].neighbors:
                self.nodes[n].vertex=[(v,w) for v,w in self.nodes[n].neighbors if v!=vertex]
            self.edges=[edges for edges in self.edges if edges[0]!=vertex and edges[1]!=vertex]
            self.size-=1

    def bfs(self,start):
        if start not in self.nodes:
            return
        queue=[start]
        visited=set()
        bfs=[]

        while queue:
            current=queue.pop(0)
            if current not in visited:
                visited.add(current)
                bfs.append(current)
                for n,w in self.nodes[current].neighbors:
                    if n not in visited:
                        queue.append(n)
        print("bfs order",bfs)
        return bfs

    def dfsn(self,start):
        visited=set()
        dfs=[]

        def dfs(node):
            if node not in visited:
                visited.add(node)
                dfs.append(node)
                for n,w in self.nodes[node].neighbors:
                    dfs(n)
        if start in self.nodes:
            dfs(start)

    def toposort(self):
        visited=set()
        stack=[]

        def dfs(node):
            visited.add(node)
            for n,w in self.nodes[node].neighbors:
                if n not in visited:
                    dfs(n)
            stack.append(node)

        for node in self.nodes:
            if node not in visited:
                dfs(node)




