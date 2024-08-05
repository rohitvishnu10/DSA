class Node:
    def __init__(self, val):
        self.data = val
        self.nbs = []


class Graph:
    def __init__(self):
        self.vertices = 0
        self.nodes = {}
        self.edges = []

    def add_node(self, val):
        if val not in self.nodes:
            self.vertices += 1
            self.nodes[val] = Node(val)
            print(f"Node {val} added")

    def add_edge(self, a, b, weight):
        if a not in self.nodes:
            self.add_node(a)
        if b not in self.nodes:
            self.add_node(b)
        if a in self.nodes and b in self.nodes:
            self.nodes[a].nbs.append((b, weight))
            self.nodes[b].nbs.append((a, weight))
            self.edges.append((a, b, weight))
            print(f"Edge between {a} and {b} with weight {weight} added")

    def del_node(self, vertex):
        if vertex in self.nodes:
            # Remove edges associated with the node
            for neighbor, weight in self.nodes[vertex].nbs:
                self.nodes[neighbor].nbs = [(v, w) for v, w in self.nodes[neighbor].nbs if v != vertex]
            self.edges = [edge for edge in self.edges if edge[0] != vertex and edge[1] != vertex]
            # Remove the node
            del self.nodes[vertex]
            self.vertices -= 1
            print(f"Node {vertex} removed")
        else:
            print(f"Node {vertex} not found")

    def del_edge(self, a, b):
        if a in self.nodes and b in self.nodes:
            self.nodes[a].nbs = [(v, w) for v, w in self.nodes[a].nbs if v != b]
            self.nodes[b].nbs = [(v, w) for v, w in self.nodes[b].nbs if v != a]
            self.edges = [edge for edge in self.edges if
                          not ((edge[0] == a and edge[1] == b) or (edge[0] == b and edge[1] == a))]
            print(f"Edge between {a} and {b} removed")
        else:
            print(f"Edge between {a} and {b} not found")

    def dijkstra(self, start_vertex):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_vertex] = 0
        predecessors = {node: None for node in self.nodes}
        unvisited = set(self.nodes.keys())

        while unvisited:
            min_node = None
            for node in unvisited:
                if min_node is None:
                    min_node = node
                elif distances[node] < distances[min_node]:
                    min_node = node

            if distances[min_node] == float('inf'):
                break

            unvisited.remove(min_node)
            current_d = distances[min_node]

            for neighbor, weight in self.nodes[min_node].nbs:
                distance = current_d + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = min_node

        return distances, predecessors

    def bfs(self, start):
        if start in self.nodes:
            visited = set()
            queue = [start]
            bfs_order = []

            while queue:
                current = queue.pop(0)
                if current not in visited:
                    visited.add(current)
                    bfs_order.append(current)
                    for n, w in self.nodes[current].nbs:
                        if n not in visited:
                            queue.append(n)
            return bfs_order
        else:
            print(f"Node {start} not found")
            return []

    def dfs(self, start):
        visited = set()
        dfs_order = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                dfs_order.append(node)
                for neighbor, weight in self.nodes[node].nbs:
                    dfs_recursive(neighbor)

        if start in self.nodes:
            dfs_recursive(start)
            return dfs_order
        else:
            print(f"Node {start} not found")
            return []

    def bellman_ford(self, start_vertex):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_vertex] = 0
        predecessors = {node: None for node in self.nodes}

        # Relax edges repeatedly
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle")
                return None, None

        return distances, predecessors


# Example usage
g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 1)
g.add_edge(4, 2, -3)  # This creates a negative cycle

distances, predecessors = g.bellman_ford(1)
if distances is None and predecessors is None:
    print("Negative cycle detected in the graph")
else:
    print("Distances:", distances)
    print("Predecessors:", predecessors)

bfs_order = g.bfs(1)
print("BFS Order:", bfs_order)

dfs_order = g.dfs(1)
print("DFS Order:", dfs_order)

g.del_edge(1, 2)
g.del_node(1)
g.del_node(2)
