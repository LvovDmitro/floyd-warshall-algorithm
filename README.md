# Floyd-Warshall Algorithm with Parallelization

This repository contains two implementations of the Floyd-Warshall algorithm:
1. **Non-parallel** implementation in Python.
2. **Parallel** implementation using Python's `concurrent.futures` for multi-threading.

## Algorithm and Parallelization

The **Floyd-Warshall** algorithm is used to find the shortest paths in a weighted graph. The parallel version divides the workload of updating rows of the distance matrix across multiple threads to speed up the computation.

## Instructions to Reproduce

1. **Dependencies**:  
   Install the necessary Python libraries:  

2. **Generate and Save Graph**:  
Use the `graph_generator.py` script to generate a random graph and save it to a file:
```bash
python src/graph_generator.py

3. **Run the Benchmark**:
To run the benchmark and compare the performance of the non-parallel and parallel implementations, run:
python src/benchmark.py
