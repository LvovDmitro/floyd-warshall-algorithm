import numpy as np
import random

def generate_graph(n, p=0.5, weight_range=(1, 10)):
    graph = np.inf * np.ones((n, n))
    for i in range(n):
        graph[i][i] = 0  
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(weight_range[0], weight_range[1])
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def save_graph(graph, filename):
    graph_with_large_values = np.where(graph == np.inf, 999999, graph)
    np.savetxt(filename, graph_with_large_values, fmt="%d")

