from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def DFS(self, s, t, parent, visited):
        visited[s] = True
        if s == t:
            return True

        for ind, val in enumerate(self.graph[s]):
            if visited[ind] == False and val > 0:
                parent[ind] = s
                if self.DFS(ind, t, parent, visited):
                    return True

        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.DFS(source, sink, parent, [False] * self.ROW):
            path_flow = float("Inf")
            s = sink
            path = []

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                path.append(s)
                s = parent[s]

            path.append(source)
            path.reverse()

            # Print the augmenting path
            print("Augmenting Path:", " -> ".join(map(str, path)))

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Create a graph given in the above diagram
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
