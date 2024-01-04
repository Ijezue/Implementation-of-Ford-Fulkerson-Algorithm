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
