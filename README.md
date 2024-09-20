# Implementation-of-Ford-Fulkerson-Algorithm
The Ford-Fulkerson algorithm is a greedy algorithm that is commonly used to tackle the maximum flow problem in a flow network. The Ford
Fulkerson Algorithm considers a flow network with specified
 edge capacities and seeks to maximize the total flow from
 source to sink in the network. It was published in 1956 by L.R.
 Ford Jr. and Dr. Fulkerson, and the name ”Ford–Fulkerson” is
 often also used for the Edmonds-Karp algorithm, which is a
 specialization of Ford–Fulkerson.

The algorithm operates on the principle that as long as
 a path from the source to the sink where all
edges have available capacity exists, flow can be sent along one of
 these paths. This process is repeated by identifying augmenting
 paths—paths with available capacity—and sending flow along
 them. The Ford-Fulkerson Algorithm relies on the iterative
 discovery of augmenting paths using depth-first search (DFS) or breadth-first search (BFS). These paths
 are determined based on the residual graph, representing
 the remaining capacity after initial flow allocations. Through
 the identification of augmenting paths and the adjustment of
 f
 low values, the algorithm can determine the maximum flow in
 the network. Utilizing the Ford-Fulkerson algorithm to solve
 the maximum flow problem is the focus of our research.


Edmonds-Karp algorithm is used to refer to the implementation of the Ford-Fulkerson 
that uses Breadth-First Search (BFS) to find augmenting paths. This algorithm repeatedly 
finds the shortest path from the source to the sink in the residual graph and sends as 
much flow as possible through that path until no more augmenting paths can be found.

The Ford-Fulkerson method can also be implemented using Depth-First Search (DFS) to find augmenting paths. 
This approach repeatedly searches for any path from the source to the sink in the residual graph and 
sends as much flow as possible through that path until no more augmenting paths can be found.

In this repo, I implemented Ford-Fulkerson algorithm using both search algorithms (i.e DFS and BFS).
You can implement both and compare their 

##Performance Considerations
###DFS vs BFS:
DFS may be faster in some cases, but it doesn't guarantee the shortest augmenting paths, potentially leading to slower convergence in certain networks. BFS, on the other hand, always finds the shortest augmenting path and tends to perform better in terms of both time complexity and the number of iterations needed to reach the maximum flow.

###Memory Usage:
BFS typically requires more memory than DFS due to the need to store all the nodes at the current level of the search.
