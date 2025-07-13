"""
Assignment 2: Quick Sort 
Merge Sort implementation in Python.
This implementation is to provide a performance comparison between Merge and Quick Sort, see MergeSort.py for Merge Sort implementation.
"""

import time
import random
import tracemalloc  # For memory usage tracking
import sys # Needed for recursion limit adjustment

sys.setrecursionlimit(2000000)  # Increase recursion limit for large arrays

# Quick Sort function
def quick_sort(arr):
    # Call recursive helper function.
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, low, high):
    if low < high:
        # Partition the array and get the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]
    i = (low - 1)  # Pointer for the smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at i + 1 to place it in the correct position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def test_case_run(name, data):
    print(f"Running Test Case: {name}")
    print(f"Data Size: {len(data)} elements")
    
    # Start memory tracking
    tracemalloc.start()

    start_time = time.perf_counter()
    data_copy = list(data)  # Copy data to avoid in-place sorting affecting original data
    sorted_data = quick_sort(data_copy)
    end_time = time.perf_counter()

    # Get memory usage.
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds.

    print(f"Sorted Data (first 12 elements): {sorted_data[:12]}... (Total: {len(sorted_data)} elements)") # Display first 12 elements of sorted data and total count.
    print(f"Execution Time: {execution_time_ms:.4f} ms")
    print(f"Memory Usage: Current = {current / (1024 * 10124):.4f} MB, Peak = {peak / (1024 * 1024):.4f} MB\n")  # Display memory usage in MB.
    print(f"Is Sorted?: {sorted_data == sorted(data)}\n") # Verify if the data is sorted.
    
    
# Use Cases for Quick Sort
if __name__ == "__main__":
  
    # Size of the dataset, picked a large number for performance testing.
    DATA_SIZE = 100000

    # Use Case: Sorted Data
    sorted_data = list(range(DATA_SIZE))
    test_case_run("Sorted Data", sorted_data)

    # Use Case: Reverse Sorted Data
    reverse_sorted_data = list(range(DATA_SIZE, 0, -1))
    test_case_run("Reverse Sorted Data", reverse_sorted_data)

    # Use Case: Random Data
    random_data = random.sample(range(DATA_SIZE * 2), DATA_SIZE)
    test_case_run("Random Data", random_data)