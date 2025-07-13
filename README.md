## Merge and Quick Sort Implementations
This is a repository that contains my second assignment for MSCS532. This is a Python implementation of the Merge Sort and Quick Sort algorithms. The algorithm was utilized to sort a list of numbers using the divide and conquer paradigm. It also includes test cases to demonstrate their performance (execution time and memory usage) on various types of datasets.

## Project Overview
This section of the project focuses on the practical implementation and comparison of the two divide-and-conquer sorting algorithms: Merge Sort and Quick Sort. The primary objective is to bridge the gap between theoretical algorithmic complexity and real-world performance.

#### Key Activities:

<strong>Algorithm Implementation:</strong> Both Merge Sort and Quick Sort will be implemented in Python.

<strong>Dataset Preparation:</strong> To rigorously test and compare the algorithms, various datasets will be generated. These include:

* Sorted Data: To evaluate performance under best-case (for Merge Sort) and potential worst-case (for Quick Sort with naive pivot) scenarios.

* Reverse-Sorted Data: Similar to sorted data, this will test worst-case performance for Quick Sort and consistent performance for Merge Sort.

* Random Data: To assess the average-case performance of both algorithms, which is often their most common operational scenario.

#### Performance Metric Collection: 

For each algorithm and dataset combination, two key performance metrics will be recorded:

<em>Execution Time:</em> Measured to understand the time efficiency and throughput of each algorithm.

<em>Memory Usage:</em> Tracked to assess the memory allocation and space efficiency, particularly highlighting the auxiliary space requirements of Merge Sort versus the in-place nature of Quick Sort.


## Deliverables:
``` MergeSort.py ``` - Python file containing the functions merge_sort, merge, and test_case_run. Also includ example use cases to merge sort sorted data, reverse sorted data, and random sorted data. 

``` QuickSort.py ``` - Python file containing the functions quick_sort, quick_sort_helper, partition, and test_case_run and example use cases to quick sort sorted data, reverse sorted data, and random sorted data. 

How to Run:
- Save the Python files.
- Open terminal or preferred IDE
- Navigate and open the saved file
- Run the script using your Python interpreter.
