import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

class Graph:
    def __init__(self, graph):
        # Initialize the graph with the provided adjacency matrix
        self.graph = graph
        self.ROW = len(graph)

    def plot_graph(self, graph, title):
        # Create a directed graph and plot it using networkx
        G = nx.DiGraph()

        # Add edges with capacities from the original graph
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] > 0:
                    G.add_edge(i, j, capacity=graph[i][j])

        # Define layout and draw the graph with node and edge labels
        pos = nx.spring_layout(G)
        capacities = nx.get_edge_attributes(G, 'capacity')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities, font_color="red")

        # Display the plot with the specified title
        plt.title(title)
        plt.show()

    def plot_residual_graph(self, residual_graph, title):
        # Create a directed graph for the residual graph and plot it
        G = nx.DiGraph()

        # Add edges with capacities from the residual graph
        for i in range(len(residual_graph)):
            for j in range(len(residual_graph[i])):
                if residual_graph[i][j] > 0:
                    G.add_edge(i, j, capacity=residual_graph[i][j])

        # Define layout and draw the residual graph with node and edge labels
        pos = nx.spring_layout(G)
        capacities = nx.get_edge_attributes(G, 'capacity')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities, font_color="red")

        # Display the plot with the specified title
        plt.title(title)
        plt.show()

    def BFS(self, s, t, parent):
        # Perform Breadth-First Search to find augmenting paths
        visited = [False] * (self.ROW)
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def EdmondsKarp(self, source, sink, plot=True):
        # Implement the Edmonds-Karp algorithm to find maximum flow
        parent = [-1] * (self.ROW)
        max_flow = 0

        # Print the original graph if plotting is enabled
        if plot:
            self.plot_graph(self.graph, "Original Graph")

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            path = []

            # Trace the augmenting path and find its minimum capacity
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                path.append(s)
                s = parent[s]

            path.append(source)
            path.reverse()

            # Print the augmenting path and maximum flow for each iteration
            print("\nAugmenting Path (Edmonds-Karp):", " -> ".join(map(str, path)))
            print("Maximum Flow:", path_flow)

            # Update the residual graph and accumulate the maximum flow
            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            # Print and plot the residual graph if plotting is enabled
            if plot:
                self.plot_residual_graph(self.graph, "Residual Graph (Edmonds-Karp)")

        return max_flow


# The test is commented out so the output will not mess with the interface and analysis
'''
# Test

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
  
print ("The maximum possible flow in this network is %d " % g.EdmondsKarp(source, sink, plot=False))
'''
