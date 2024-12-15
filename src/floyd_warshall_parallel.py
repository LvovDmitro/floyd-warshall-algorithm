import numpy as np
import multiprocessing as mp

def floyd_warshall_parallel(graph):
    n = len(graph)
    dist = np.copy(graph)
    
    def update_row(start_row, end_row, k):
        for i in range(start_row, end_row):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    def worker(k):
        num_processes = mp.cpu_count()
        rows_per_process = n // num_processes
        processes = []
        for i in range(num_processes):
            start_row = i * rows_per_process
            end_row = (i + 1) * rows_per_process if i != num_processes - 1 else n
            p = mp.Process(target=update_row, args=(start_row, end_row, k))
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()

    for k in range(n):
        worker(k)
    
    return dist
