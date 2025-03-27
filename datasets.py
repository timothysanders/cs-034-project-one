'''
                                    ---------------------------------
                                    Generate general-purpose datasets
                                    ---------------------------------

1. Random (General Case): small size, medium size

Description: A completely random array with no inherent order.
Purpose: Tests the general efficiency of sorting algorithms.

Expected Results:

QuickSort typically performs well (O(n log n) on average).
Merge Sort has a consistent O(n log n) but requires extra space.
Shell Sort may not be as fast as QuickSort but is space-efficient.

2. Nearly Sorted Dataset (Best Case for Shell Sort)
Description: An already sorted array with a few misplaced elements.
Purpose: Evaluates how algorithms handle nearly sorted data.

Expected Results:

Shell Sort should be very fast (almost O(n) due to reduced swaps).
Merge Sort and QuickSort still perform O(n log n), making them slower than Shell Sort in this case.

3. Reverse Ordered Dataset (Worst Case for QuickSort)

Description: A dataset sorted in descending order.
Purpose: Tests how algorithms handle worst-case scenarios.

Expected Results:

QuickSort (with a bad pivot selection strategy) can degrade to O(n²).
Merge Sort remains stable at O(n log n).
Shell Sort performs better than QuickSort in this case, but not as well as Merge Sort.

4. Large Dataset (Scalability Test)

Description: A very large dataset (e.g., 1,000,000 elements).
Purpose: Evaluates how each algorithm scales with increasing data size.

Expected Results:

QuickSort should be the fastest on average.
Merge Sort will be stable but will require extra space.
Shell Sort might not be ideal for very large datasets.

                                    ------------------------------------
                                    Generate algorithm-specific datasets
                                    ------------------------------------


1. datasets for Shell sort
--------------------------

    1) Evenly distributed list without large clusters of disorder
    2) Unevenly distributed list requiring long-distance swaps-Small numbers clustered at
       the end, large numbers at the beginning
    3) Partly ordered but frequently updated list (e.g., Stock Order Book)
    

2. datasets for QuickSort
-------------------------



3. datasets for Merge sort
--------------------------

'''

'''
                                    ---------------------------------
                                    Generate general-purpose datasets
                                    ---------------------------------
'''
import numpy as np
import pandas as pd
import time

# Generate test datasets
import numpy as np
import time
import pandas as pd

# Generate gap sequence
def generate_gap_values(arrSize):
    gap_values = []
    gap = arrSize // 2
    while gap >= 1:
        gap_values.append(gap)
        gap = gap // 2
    return gap_values

# Modified insertion sort for Shell Sort
def insertion_sort_interleaved(arr, start_index, gap_value):
    swaps = 0
    for i in range(start_index + gap_value, len(arr), gap_value):
        j = i
        while (j - gap_value >= start_index) and (arr[j] < arr[j - gap_value]):
            swaps += 1
            arr[j], arr[j - gap_value] = arr[j - gap_value], arr[j]
            j = j - gap_value
    return swaps

# Shell Sort using insertion sort with gaps
def shell_sort(arr):
    arrSize = len(arr)
    gap_values = generate_gap_values(arrSize)
    swaps = []
    for gap_value in gap_values:
        for i in range(gap_value):
            swaps.append(insertion_sort_interleaved(arr, i, gap_value))
    return swaps

# Generate test datasets
def generate_datasets(size):
    half = size // 2
    datasets = {}

    # Add "Large Random" first if applicable
    if size >= 100000:
        datasets["Large Random"] = np.random.randint(0, 1000000, size)

    # Add the rest
    datasets.update({
        "Random": np.random.randint(0, 1000, size),
        "Nearly Sorted": np.sort(np.random.randint(0, 1000, size)) + np.random.randint(-3, 3, size),
        "Reverse Sorted": np.sort(np.random.randint(0, 1000, size))[::-1],
        "Many Duplicates": np.random.choice([5, 10, 15, 20], size=size, replace=True),
        "Even Distributed": np.linspace(0, 1000, size).astype(int),
        "Uneven Distributed (Front Heavy)": np.concatenate([
            np.random.randint(900, 1000, half),
            np.random.randint(0, 100, size - half)
        ]),
        "Uneven Distributed (End Heavy)": np.concatenate([
            np.random.randint(0, 100, half),
            np.random.randint(900, 1000, size - half)
        ])
    })

    return datasets



# Main execution block
if __name__ == "__main__":
    results = []
    arr_size = 100
    datasets = generate_datasets(arr_size)

    for name, data in datasets.items():
        my_arr = data.copy()

        start_time = time.time()
        swap_counts = shell_sort(my_arr)
        end_time = time.time()

        total_swaps = sum(swap_counts)
        execution_time = end_time - start_time

        results.append({
            "Dataset": name,
            "Total Swaps": total_swaps,
            "Execution Time (s)": execution_time
        })

    # Convert results to DataFrame and print nicely
    df = pd.DataFrame(results)
    print("\nShell Sort Performance Summary:\n")
    print(df.to_string(index=False))

  

# Time sorting algorithms on the datasets
def time_sorting_algorithms(datasets):
    results = []

    for name, data in datasets.items():
        arr = data.copy()
        n = len(arr)
        gaps = [n // (2 ** k) for k in range(int(np.log2(n)) + 1) if n // (2 ** k) > 0]

        # Shell Sort
        t1 = time.time()
        shell_sort(arr.copy(), gaps)
        t_shell = time.time() - t1

        # QuickSort
        t2 = time.time()
        np.sort(arr.copy(), kind='quicksort')
        t_quick = time.time() - t2

        # MergeSort
        t3 = time.time()
        np.sort(arr.copy(), kind='mergesort')
        t_merge = time.time() - t3

        results.append({
            "Dataset": name,
            "Shell Sort": t_shell,
            "QuickSort": t_quick,
            "MergeSort": t_merge
        })

    return pd.DataFrame(results)


'''
                                    -----------------------------------
                                    Generate random datasets (from Tim)
                                    -----------------------------------
'''

import numpy as np


def generate_random_integer_list(size: int, low: int=0, high: int=100) -> list[int]:
    """
    Generate a random list with a length of `size`.

    Parameters
    ----------
    size : int
    low : int = 0
    high : int = 100

    Returns
    -------
    list[int]
    """
    return np.random.randint(low, high, size=size).tolist()

# Define function to generate an evenly_distributed dataset for Shell Sort

def generate_evenly_distributed(size: int, low: int = 0, high: int = 1000) -> np.ndarray:
    """
    Generates an evenly distributed list without large clusters of disorder.
    
    :param size: Number of elements in the list.
    :param low: Minimum value in the range.
    :param high: Maximum value in the range.
    :return: Evenly distributed NumPy array.
    """
    return np.random.permutation(np.linspace(low, high, size))

# Define function to generate unevenly_distributed datasets for Shell Sort
def generate_unevenly_distributed(size: int, low: int = 0, high: int = 1000, split_ratio: float = 0.5) -> np.ndarray:
    """
    Generates an unevenly distributed list where small numbers are clustered at the end 
    and large numbers at the beginning.
    
    :param size: Number of elements in the list.
    :param low: Minimum value in the range.
    :param high: Maximum value in the range.
    :param split_ratio: Fraction of large numbers at the beginning.
    :return: Unevenly distributed NumPy array.
    """
    split_point = int(size * split_ratio)
    large_numbers = np.random.randint(high - 100, high, size=split_point)  # Large numbers at the beginning
    small_numbers = np.random.randint(low, low + 100, size=size - split_point)  # Small numbers at the end
    uneven_list = np.concatenate([large_numbers, small_numbers])
    np.random.shuffle(uneven_list)  # Introduce some randomness
    return uneven_list


# Define function to generate partly ordered yet frequently updated dataset for Shell Sort
def generate_partly_ordered(size: int, ordered_ratio: float = 0.8, low: int = 0, high: int = 1000) -> np.ndarray:
    """
    Generates a partly ordered list where the first part is sorted, and the rest is randomly inserted.
    This simulates a stock order book where new data is appended randomly.
    
    :param size: Number of elements in the list.
    :param ordered_ratio: Fraction of the list that should be pre-sorted.
    :param low: Minimum value in the range.
    :param high: Maximum value in the range.
    :return: Partly ordered NumPy array.
    """
    ordered_size = int(size * ordered_ratio)
    unordered_size = size - ordered_size

    ordered_part = np.sort(np.random.randint(low, high, size=ordered_size))  # Sorted first part
    unordered_part = np.random.randint(low, high, size=unordered_size)  # Random last part

    return np.concatenate([ordered_part, unordered_part])
