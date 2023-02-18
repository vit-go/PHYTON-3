import heapq

INF = 1e9

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def shortest_path(self, s):
        pq = []
        dist = [INF for _ in range(self.V)]
        heapq.heappush(pq, (0, s))
        dist[s] = 0
        while pq:
            u = heapq.heappop(pq)[1]
            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")

V = ...  # Set the value of V here
g = Graph(V)
# Add edges to the graph here
g.shortest_path(0)  # Replace 0 with the source vertex
V = 5  # Set the value of V here
g = Graph(V)
