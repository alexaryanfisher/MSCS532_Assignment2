"""
Assignment 2: Merge Sort 
Merge Sort implementation in Python.
This implementation is to provide a performance comparison between Merge and Quick Sort, see QuickSort.py for Quick Sort implementation.
"""

import time
import random
import tracemalloc # For memory usage tracking

# Merge Sort function
def merge_sort(arr):
    if len(arr) > 1:
        # Divide Step: Divide the array into two halves
        mid = len(arr) // 2 
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Conquer Step: Recursively sort both halves
        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

        # Combine Step: Merge the sorted halves
        return merge(left_arr, right_arr)
    else:
        return arr

def merge(left, right):  
    merged_arr = []
    # Pointers for left and right subarrays
    i = 0 # left array pointer
    j = 0 # right array pointer

    # Compare elements from both arrays and append the smaller one to the merged array.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    
    # If there are remaining elements in the left array, append them
    while i < len(left):
        merged_arr.append(left[i])
        i += 1

    # If there are remaining elements in the right array, append them
    while j < len(right):
        merged_arr.append(right[j])
        j += 1

    return merged_arr

""" Use Cases for Merge Sort 
Includes Execution Time Measurement, Memory usage, and Prints Results"""

def test_case_run(name, data):
    print(f"Running Test Case: {name}")
    print(f"Data Size: {len(data)} elements")

    tracemalloc.start()  # Start memory tracking.
    start_time = time.perf_counter()
    sorted_data = merge_sort(list(data))
    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()  # Get current and peak memory usage.
    tracemalloc.stop()  # Stop memory tracking.
    
    execution_time_ms = end_time - start_time * 1000  # Convert to milliseconds

    print(f"Sorted Data (first 12 elements): {sorted_data[:12]}... (Total: {len(sorted_data)} elements)") # Display first 12 elements of sorted data and total count.
    print(f"Execution Time: {execution_time_ms:.4f} ms")
    print(f"Memory Usage: Current = {current / (1024 * 10124):.4f} MB, Peak = {peak / (1024 * 1024):.4f} MB\n")  # Display memory usage in MB.
    print(f"Is Sorted?: {sorted_data == sorted(data)}\n") # Verify if the data is sorted.

# Use Cases

if __name__ == "__main__":

    DATA_SIZE = 150000  # Size of the dataset, picked a large number for performance testing.

    # Use Case: Sorted Data
    sorted_data = list(range(DATA_SIZE))
    test_case_run("Sorted Data", sorted_data)

    # Use Case: Reverse Sorted Data
    reverse_sorted_data = list(range(DATA_SIZE, 0, -1))
    test_case_run("Reverse Sorted Data", reverse_sorted_data)

    # Use Case: Random Data
    random_data = [random.randint(0, DATA_SIZE) for _ in range(DATA_SIZE)]
    test_case_run("Random Data", random_data)