"""
                                    ---------------------------------
                                    Generate general-purpose datasets
                                    ---------------------------------

1. Random (General Case): small size, medium size

Description: A completely random array with no inherent order.
Purpose: Tests the general efficiency of sorting algorithms.
Implementation: generate_random_integer_list(size, low=0, high=100)

Expected Results:
-----------------
QuickSort typically performs well (O(n log n) on average).
Merge Sort has a consistent O(n log n) but requires extra space.
Shell Sort may not be as fast as QuickSort but is space-efficient.


2. Nearly Sorted Dataset (Best Case for Shell Sort)
Description: An already sorted array with a few misplaced elements.
Purpose: Evaluates how algorithms handle nearly sorted data.
Implementation: generate_nearly_sorted(size, swap_ratio=0.05)

Expected Results:
-----------------
Shell Sort should be very fast (almost O(n) due to reduced swaps).
Merge Sort and QuickSort still perform O(n log n), making them slower than Shell Sort in this case.


3. Reverse Ordered Dataset (Worst Case for QuickSort)

Description: A dataset sorted in descending order.
Purpose: Tests how algorithms handle worst-case scenarios.
Implementation: generate_reverse_sorted(size, low=0, high=100)

Expected Results:
-----------------
QuickSort (with a bad pivot selection strategy) can degrade to O(n²).
Merge Sort remains stable at O(n log n).
Shell Sort performs better than QuickSort in this case, but not as well as Merge Sort.


4. Large Dataset (Scalability Test)

Description: A very large dataset (e.g., 1,000,000 elements).
Purpose: Evaluates how each algorithm scales with increasing data size.
Implementation: generate_random_integer_list(size, low=0, high=100)

Expected Results:
-----------------
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

    1) List of even numbers
    2) List of odd numbers
    3) List of duplicates of 1 integer
    4) List of duplicates of multiple integers



3. datasets for Merge sort
--------------------------

    1) Empty list
    2) Single element list
    3) Ordered list of two elements
    4) List of identical elements
    5) Duplicate list


"""
from typing import Optional
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


def generate_nearly_sorted(size: int, swap_ratio: Optional[float] = 0.05) -> list[int]:
    """
    Create a nearly ordered list of integers from 0 to n-1 with a small amount of random swaps.

    Parameters
    ----------
    size : int
        Size of the array.
    swap_ratio : float, optional
        Fraction of the list elements to swap (default is 0.05, or 5%).

    Returns
    -------
    list[int]
        Nearly ordered list.
    """
    generated_list = np.arange(size)
    num_swaps = int(size * swap_ratio)

    for _ in range(num_swaps):
        i, j = np.random.randint(0, size, size=2)
        generated_list[i], generated_list[j] = generated_list[j], generated_list[i]
    return generated_list.tolist()

def generate_reverse_sorted(size: int,  low: int=0, high: int=100) -> list[int]:
    """
    Generate a random list of integers sorted in descending order.

    Leverages Python's list.sort() method to create the reverse sorted list.

    Parameters
    ----------
    size : int
    low : int = 0
    high : int = 100

    Returns
    -------
    generated_list : list[int]
        - The generated list sorted in reverse order
    """
    generated_list = generate_random_integer_list(size, low, high)
    generated_list.sort(reverse=True)
    return generated_list