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


                            Datasets Created by Michael Jung

Extra Datasets to measure edge cases:
5. Nearly ordered datasets where a few elements are swapped

6. Dataset with exponentially growing elements

7.Dataset that alternates between increasing and decreasing values

8.Dataset that is sorted in groups
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
1) List of even integers
2) List of odd integers
3) List of duplicates of 1 integer
4) List of duplicates of multiple integers



3. datasets for Merge sort
--------------------------
1) Empty list
2) Single element list
3) List of identical elements
4) Duplicate list 

'''
from typing import Iterable

'''
                                    ---------------------------------
                                    Generate general-purpose datasets
                                    ---------------------------------
'''
import numpy as np
import pandas as pd
import time
import random


# Generate structured datasets for characterist testing
def generate_structured_datasets(size: int) -> dict[str, list]:
    """
    Create structured datasets for characteristic testing.

    Parameters
    ----------
    size : int

    Returns
    -------
    dict[str, list]
    """
    half = size // 2
    return {
        "Random": np.random.randint(0, 1000, size).tolist(),
        "Nearly Sorted": (np.sort(np.random.randint(0, 1000, size)) + np.random.randint(-3, 3, size)).tolist(),
        "Reverse Sorted": np.sort(np.random.randint(0, 1000, size))[::-1].tolist(),
        "Many Duplicates": np.random.choice([5, 10, 15, 20], size=size, replace=True).tolist(),
        "Even Distributed": np.linspace(0, 1000, size, dtype=int).tolist(),
        "Uneven Distributed (Front Heavy)": np.concatenate([
            np.random.randint(900, 1000, half),
            np.random.randint(0, 100, size - half)
        ]).tolist(),
        "Uneven Distributed (End Heavy)": np.concatenate([
            np.random.randint(0, 100, half),
            np.random.randint(900, 1000, size - half)
        ]).tolist()
    }

# Generate large scale random dataset for scalability testing
def generate_large_random_dataset(size: int) -> dict[str, list]:
    """
    Single large random dataset for scalability testing.

    Parameters
    ----------
    size : int

    Returns
    -------
    dict[str, list]
    """
    return {
        f"Large Random ({size:,})": np.random.randint(0, 1_000_000, size).tolist()
    }


# Time sorting algorithms on the datasets
def time_sorting_algorithms(datasets):
    results = []

    for name, data in datasets.items():
        arr = data.copy()
        n = len(arr)

        # Generate gap values
        gaps = [n // (2 ** k) for k in range(int(np.log2(n)) + 1) if n // (2 ** k) > 0]

        # Shell Sort (with gap-aware implementation)
        arr_shell = arr.copy()
        t1 = time.time()
        swap_counts = shell_sort(arr_shell)
        t_shell = time.time() - t1
        total_swaps = sum(swap_counts)

        # QuickSort (NumPy built-in)
        t2 = time.time()
        np.sort(arr.copy(), kind='quicksort')
        t_quick = time.time() - t2

        # MergeSort (NumPy built-in)
        t3 = time.time()
        np.sort(arr.copy(), kind='mergesort')
        t_merge = time.time() - t3

        results.append({
            "Dataset": name,
            "Size": n,
            "Shell Sort Time (s)": t_shell,
            "Shell Sort Swaps": total_swaps,
            "QuickSort Time (s)": t_quick,
            "MergeSort Time (s)": t_merge
        })

    return pd.DataFrame(results)


"""
                                    -------------------------------------
                                    Generate shell sort specific datasets
                                    -------------------------------------
"""


def generate_shell_sort_datasets(size: int) -> dict[str, list]:
    """
    Create datasets specifically for testing the shell sort algorithm.

    Parameters
    ----------
    size : int

    Returns
    -------
    dict[str, list]
    """
    datasets = {
        "Evenly distributed": generate_evenly_distributed(size),
        "Unevenly distributed": generate_unevenly_distributed(size),
        "Partly ordered": generate_partly_ordered(size)
    }
    return datasets


# Define function to generate an evenly_distributed dataset for Shell Sort
def generate_evenly_distributed(size: int, low: int = 0, high: int = 1000) -> list:
    """
    Generates an evenly distributed list without large clusters of disorder.

    Parameters
    ----------
    size : int
        - Number of elements in the list.
    low : int
        - Minimum value in the range.
    high : int
        - Maximum value in the range.

    Returns
    -------
    list
        - Evenly distributed list.
    """
    return np.random.permutation(np.linspace(low, high, size)).tolist()

# Define function to generate unevenly_distributed datasets for Shell Sort
def generate_unevenly_distributed(size: int, low: int = 0, high: int = 1000, split_ratio: float = 0.5) -> list:
    """
    Generates an unevenly distributed list where small numbers are clustered at the end
    and large numbers at the beginning.

    Parameters
    ----------
    size : int
        - Number of elements in the list.
    low : int
        - Minimum value in the range.
    high : int
        - Maximum value in the range.
    split_ratio : float
        - Fraction of large numbers at the beginning.

    Returns
    -------
    list
        - Unevenly distributed NumPy array.
    """
    split_point = int(size * split_ratio)
    large_numbers = np.random.randint(high - 100, high, size=split_point)  # Large numbers at the beginning
    small_numbers = np.random.randint(low, low + 100, size=size - split_point)  # Small numbers at the end
    uneven_list = np.concatenate([large_numbers, small_numbers]).tolist()
    np.random.shuffle(uneven_list)  # Introduce some randomness
    return uneven_list


# Define function to generate partly ordered yet frequently updated dataset for Shell Sort
def generate_partly_ordered(size: int, ordered_ratio: float = 0.8, low: int = 0, high: int = 1000) -> list:
    """
    Generates a partly ordered list where the first part is sorted, and the rest is randomly inserted.
    This simulates a stock order book where new data is appended randomly.

    Parameters
    ----------
    size : int
        - Number of elements in the list.
    ordered_ratio: float
        - Fraction of the list that should be pre-sorted.
    low : int
        - Minimum value in the range.
    high: int
        - Maximum value in the range.
    Returns
    -------
    list
        - Partly ordered NumPy array.
    """
    ordered_size = int(size * ordered_ratio)
    unordered_size = size - ordered_size

    ordered_part = np.sort(np.random.randint(low, high, size=ordered_size))  # Sorted first part
    unordered_part = np.random.randint(low, high, size=unordered_size)  # Random last part
    partly_ordered = np.concatenate([ordered_part, unordered_part]).tolist()
    return partly_ordered

'''
                    -----------------------------------------------
                    Extra datasets to test edge cases(from Michael)
                    -----------------------------------------------
'''
# Define function to generate a variant of partially sorted dataset where a few elements are randomly swapped
def generate_sorted_with_random_indices_swapped(size: int, randomness: float=0.1) -> list:
    """
    Generate a variant of partially sorted dataset where a few elements are randomly swapped.

    Parameters
    ----------
    size : int
        - Size of the list to be generated
    randomness : float
        - The proportion of items to be swapped.

    Returns
    -------
    data : list
    """
    data = list(range(size))
    num_swaps = max(1, int(size * randomness))
    for _ in range(num_swaps):
        i, j = random.sample(range(size), 2)
        data[i], data[j] = data[j], data[i]
    return data

# Define function to generate a dataset where each element increases exponentially
def generate_exponentially_growing_dataset(size):
    return [2 ** i for i in range(size)]

# Define function to generate a dataset where elements alternate between high and low peaks, similar to a fractal
def generate_fractal_dataset(size):
    data = []
    for i in range(size):
        data.append(i // 2 if i % 2 == 0 else size - (i // 2 + 1))
    return data

# Define function to generate a variant of partially sorted data, where there are groups of sorted data
def generate_sorted_in_groups(size, group_size=5):
    data = []
    for i in range(0, size, group_size):
        block = list(range(i, min(i + group_size, size)))
        data.extend(block)
    return data

#These functions are pretty intuitive
def generate_list_of_evens(size: int) -> list[int]:
    return [random.choice(range(0, 100000, 2)) for i in range(size)]


def generate_list_of_odds(size: int) -> list[int]:
    return [random.choice(range(1, 100000, 2)) for i in range(size)]


def generate_list_of_duplicates_of_one(size: int) -> list[int]:
    value = random.randint(0, 100000)
    return [value for i in range(size)]


def generate_list_of_duplicates_of_multiple(size: int, num_duplicates: int) -> list[int]:
    values = [random.randint(0, 100000) for i in range(num_duplicates)]
    return [random.choice(values) for i in range(size)]
