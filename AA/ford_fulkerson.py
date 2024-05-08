class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        self.visited = [False] * self.ROW

    def dfs(self, u, t, parent):
        self.visited[u] = True
        if u == t:
            return True
        for v in range(self.ROW):
            if self.visited[v] == False and self.graph[u][v] > 0:
                parent[v] = u
                if self.dfs(v, t, parent):
                    return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        while True:
            print('Current flow:', max_flow)
            self.visited = [False] * self.ROW
            if not self.dfs(source, sink, parent):
                break 
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
g = Graph(graph)
source = 0
sink = 5
print("Max Flow:", g.FordFulkerson(source, sink))
