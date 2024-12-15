import numpy as np

def floyd_warshall(graph):
    n = len(graph)
    dist = np.copy(graph)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
