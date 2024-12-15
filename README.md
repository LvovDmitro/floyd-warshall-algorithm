# Floyd-Warshall Algorithm with Parallelization

This repository contains two implementations of the Floyd-Warshall algorithm:  
1. **Non-parallel implementation** written in Python.  
2. **Parallel implementation** using Python's `multiprocessing` library for CPU-bound parallel computation.

The goal is to demonstrate how parallelization can speed up the computation of shortest paths in a graph and provide a comparison of performance between the two approaches.

---

## Algorithm and Parallelization  
The **Floyd-Warshall algorithm** computes the shortest paths between all pairs of nodes in a weighted graph. It iteratively updates the shortest path distance matrix by considering whether intermediate nodes provide a shorter path.  

In the **parallel implementation**, the work of updating the rows of the distance matrix for each intermediate node (`k`) is distributed among multiple processes using the `multiprocessing` library.

---

## How to Reproduce Results  

### Prerequisites  

1. Install Python 3.7+ (preferably with `conda` or `venv`).  
2. Install required Python packages:  
   ```bash
   pip install numpy matplotlib
   ```  

---

### Repository Structure  

```plaintext
repo/
├── data/                 # Folder for input graph and generated results
│   └── input_graph.txt   # Randomly generated adjacency matrix (500 nodes)
├── benchmarks/           # Folder for benchmark results
│   └── speedup_comparison.png  # Speedup comparison graph
├── src/
│   ├── graph_generator.py       # Script to generate random graph
│   ├── floyd_warshall.py        # Non-parallel implementation
│   ├── floyd_warshall_parallel.py  # Parallel implementation using multiprocessing
│   └── benchmark.py             # Benchmark script
├── README.md             # Documentation
```

---

### Steps  

1. **Generate Input Graph**  
   Run the `graph_generator.py` script to generate a random graph and save it in the `data/` directory:  
   ```bash
   python src/graph_generator.py
   ```
   This will create a random weighted adjacency matrix (`data/input_graph.txt`) with:  
   - 500 nodes  
   - Edge connection probability: 0.5  

2. **Run Benchmark**  
   Execute the `benchmark.py` script to compare the performance of the non-parallel and parallel implementations:  
   ```bash
   python src/benchmark.py
   ```
   The results will display:  
   - Execution time for the non-parallel version.  
   - Execution time for the parallel version.  
   - Calculated speedup.  
   - A speedup graph (`benchmarks/speedup_comparison.png`) that compares execution time across various process counts.  

3. **Input Data Format**  
   The input graph is stored as an adjacency matrix in a `.txt` file. Each entry represents the weight of the edge between two nodes (`999999` for disconnected nodes).

---

## Explanation of Parallelization  

In the **parallel version**, the work of updating the distance matrix is split across multiple processes:  
- Each process is responsible for updating a range of rows in the matrix during the iteration over an intermediate node (`k`).  
- Processes run in parallel, leveraging all available CPU cores to reduce runtime significantly.  

---

## Speedup Results  

The script outputs a speedup graph (`benchmarks/speedup_comparison.png`) that visualizes the improvement in performance as the number of processes increases.  

### Formula:  
```plaintext
Speedup = Time(Serial) / Time(Parallel)
```

For a graph with **500 nodes** and edge probability **0.5**, the results are:  
- Non-parallel execution time: **~49 seconds**  
- Parallel execution time: **~12 seconds (4.1x speedup)**  

Speedup graph:  

![Speed up comparison](https://github.com/user-attachments/assets/10fb56b8-63c5-44b9-822f-247d33eed89c))

---

## Notes  

1. The parallel implementation uses the Python `multiprocessing` library and divides work evenly across processes based on the number of CPU cores.  
2. To avoid overflow errors when saving `np.inf` values, these are replaced with `999999` in the adjacency matrix.
