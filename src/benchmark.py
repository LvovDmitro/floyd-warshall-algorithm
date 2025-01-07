import time
import numpy as np
from floyd_warshall import floyd_warshall
from floyd_warshall_parallel import floyd_warshall_parallel
from graph_generator import generate_graph, save_graph
import matplotlib.pyplot as plt
import multiprocessing as mp

n = 500  
graph = generate_graph(n)
save_graph(graph, "/repo/input_graph.txt")

start = time.time()
floyd_warshall(graph)
end = time.time()
serial_time = end - start
print(f"Non-parallel time: {serial_time:.4f} seconds")

start = time.time()
floyd_warshall_parallel(graph)
end = time.time()
parallel_time = end - start
print(f"Parallel time: {parallel_time:.4f} seconds")

speedup = serial_time / parallel_time
print(f"Speedup: {speedup:.2f}")

processes = [1, 2, 4, 8, 16, 32]
times_parallel = []

for p in processes:
    start = time.time()
    floyd_warshall_parallel(graph)
    end = time.time()
    times_parallel.append(end - start)

plt.plot(processes, times_parallel, marker='o', label="Parallel")
plt.xlabel('Number of Processes')
plt.ylabel('Time (seconds)')
plt.title('Parallel Speedup Comparison')
plt.legend()
plt.savefig('/repo/speedup_comparison.png')
plt.show()
