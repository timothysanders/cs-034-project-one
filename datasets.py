"""
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
    4) Mixed negative and positive elements
    5) Sorted, then rotated elements
    6) Floating point elements
    7) Periodic pattern elements
"""

"""
                                    ---------------------------------
                                    Generate general-purpose datasets
                                    ---------------------------------
"""
import numpy as np
import random


# Generate structured datasets for characteristic testing
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
        ]).tolist(),
        "Sorted with Indices Swapped": generate_sorted_with_random_indices_swapped(size),
        "Exponentially Growing": generate_exponentially_growing_dataset(size),
        "Fractal": generate_fractal_dataset(size),
        "Sorted in Groups": generate_sorted_in_groups(size),
        "Evens": generate_list_of_evens(size),
        "Odds": generate_list_of_odds(size),
        "One Duplicate": generate_list_of_duplicates_of_one(size),
        "Multiple Duplicates": generate_list_of_duplicates_of_multiple(size, num_duplicates=10)
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
def generate_evenly_distributed(size: int, low: int = 0, high: int = 1000) -> list[float]:
    """
    Generates an evenly distributed list without large clusters of disorder.

    Parameters
    ----------
    size : int
        Number of elements in the list.
    low : int
        Minimum value in the range.
    high : int
        Maximum value in the range.

    Returns
    -------
    list[float]
        Evenly distributed list.
    """
    return np.random.permutation(np.linspace(low, high, size)).tolist()

# Define function to generate unevenly_distributed datasets for Shell Sort
def generate_unevenly_distributed(size: int, low: int = 0, high: int = 1000, split_ratio: float = 0.5) -> list[int]:
    """
    Generates an unevenly distributed list where small numbers are clustered at the end
    and large numbers at the beginning.

    Parameters
    ----------
    size : int
        Number of elements in the list.
    low : int
        Minimum value in the range.
    high : int
        Maximum value in the range.
    split_ratio : float
        Fraction of large numbers at the beginning.

    Returns
    -------
    list[int]
        Unevenly distributed NumPy array.
    """
    split_point = int(size * split_ratio)
    large_numbers = np.random.randint(high - 100, high, size=split_point)  # Large numbers at the beginning
    small_numbers = np.random.randint(low, low + 100, size=size - split_point)  # Small numbers at the end
    uneven_list = np.concatenate([large_numbers, small_numbers]).tolist()
    np.random.shuffle(uneven_list)  # Introduce some randomness
    return uneven_list


# Define function to generate partly ordered yet frequently updated dataset for Shell Sort
def generate_partly_ordered(size: int, ordered_ratio: float = 0.8, low: int = 0, high: int = 1000) -> list[int]:
    """
    Generates a partly ordered list where the first part is sorted, and the rest is randomly inserted.
    This simulates a stock order book where new data is appended randomly.

    Parameters
    ----------
    size : int
        Number of elements in the list.
    ordered_ratio: float
        Fraction of the list that should be pre-sorted.
    low : int
        Minimum value in the range.
    high: int
        Maximum value in the range.

    Returns
    -------
    list[int]
        Partly ordered NumPy array.
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
def generate_sorted_with_random_indices_swapped(size: int, randomness: float=0.1) -> list[int]:
    """
    Generate a variant of partially sorted dataset where a few elements are randomly swapped.

    Parameters
    ----------
    size : int
        Size of the list to be generated.
    randomness : float
        The proportion of items to be swapped.

    Returns
    -------
    data : list[int]
        A list containing the dataset with some elements randomly swapped.
    """
    data = list(range(size))
    num_swaps = max(1, int(size * randomness))
    for _ in range(num_swaps):
        i, j = random.sample(range(size), 2)
        data[i], data[j] = data[j], data[i]
    return data

# Define function to generate a dataset where each element increases exponentially
def generate_exponentially_growing_dataset(size: int) -> list[int]:
    """
    Generate a dataset where each element increases exponentially

    Parameters
    ----------
    size : int
        The size of the dataset to be created

    Returns
    -------
    list[int]
    """
    return [2 ** i for i in range(size)]

# Define function to generate a dataset where elements alternate between high and low peaks, similar to a fractal
def generate_fractal_dataset(size: int) -> list[int]:
    """
    Generate a dataset where elements alternate between high and low peaks, similar to a fractal

    Parameters
    ----------
    size : int

    Returns
    -------
    data : list[int]
        A list of the generated fractal data
    """
    data = []
    for i in range(size):
        data.append(i // 2 if i % 2 == 0 else size - (i // 2 + 1))
    return data

# Define function to generate a variant of partially sorted data, where there are groups of sorted data
def generate_sorted_in_groups(size: int, group_size: int=5) -> list[int]:
    """
    Generate a variant of partially sorted data, where there are groups of sorted data

    Parameters
    ----------
    size : int
        The size of the dataset to be returned
    group_size : int
        The size of the groups within the sorted data

    Returns
    -------
    data : list[int]
    """
    data = []
    for i in range(0, size, group_size):
        block = list(range(i, min(i + group_size, size)))
        data.extend(block)
    return data

#These functions are pretty intuitive
def generate_list_of_evens(size: int) -> list[int]:
    """
    Generate a list of even numbers.

    Parameters
    ----------
    size : int

    Returns
    -------
    list[int]
    """
    return [random.choice(range(0, 100000, 2)) for i in range(size)]


def generate_list_of_odds(size: int) -> list[int]:
    """
    Generate a list of odd numbers.

    Parameters
    ----------
    size : int

    Returns
    -------
    list[int]
    """
    return [random.choice(range(1, 100000, 2)) for i in range(size)]


def generate_list_of_duplicates_of_one(size: int) -> list[int]:
    """
    Generate a list of duplicates of a single randomly chosen integer.

    Parameters
    ----------
    size : int
        The number of elements in the list

    Returns
    -------
    list[int]
        A list of the randomly chosen number
    """
    value = random.randint(0, 100000)
    return [value for i in range(size)]


def generate_list_of_duplicates_of_multiple(size: int, num_duplicates: int) -> list[int]:
    """
    Generate a list of length `size` where there are `num_duplicates` distinct numbers.

    Parameters
    ----------
    size : int
    num_duplicates : int

    Returns
    -------
    list[int]
        The generated list of length `size` with `num_duplicates` distinct numbers.
    """
    values = [random.randint(0, 100000) for i in range(num_duplicates)]
    return [random.choice(values) for i in range(size)]


"""
                    ----------------------------------------------
                    Generate quicksort specific datasets (Michael)
                    ----------------------------------------------
"""

def generate_quicksort_datasets(size: int) -> dict[str, list]:
    return {
        "Evens": generate_list_of_evens(size),
        "Odds": generate_list_of_odds(size),
        "Duplicates of One": generate_list_of_duplicates_of_one(size),
        "Multiple Duplicates": generate_list_of_duplicates_of_multiple(size, num_duplicates=10)
    }

"""
                    -------------------------------------
                    Generate merge sort specific datasets
                    -------------------------------------
"""

def generate_merge_sort_datasets(size: int) -> dict[str, list]:
    return {
        "Empty List": [],
        "Single Value": generate_single_value_dataset(),
        "Uniform List": generate_uniform_dataset(size),
        "Mixed -/+ List": generate_mixed_neg_pos_dataset(size),
        "Sorted + Rotated List": generate_sorted_rotated_dataset(size),
        "Float List": generate_random_float_dataset(size),
        "Periodic Pattern": generate_periodic_pattern_dataset(size)
    }

def generate_single_value_dataset() -> list[int]:
    """
    Generate a singleton dataset containing a single random integer.

    Returns
    -------
    list[int]
        A list containing a single random integer.
    """
    return [random.randint(0, 1000)]

def generate_uniform_dataset(size: int) -> list[int]:
    """
    Generate a list of length `size` where all elements are the same.

    Parameters
    ----------
    size : int
        The number of elements in the dataset.

    Returns
    -------
    list[int]
        A list of length `size` where every element is the same randomly chosen integer.
    """
    value = random.randint(0, 1000)
    return [value] * size

def generate_mixed_neg_pos_dataset(size: int) -> list[int]:
    """
    Generate a list of length `size` containing a mix of negative and positive integers.

    Parameters
    ----------
    size : int
        The number of items in the list.

    Returns
    -------
    list[int]
        A list of random integers ranging from -1000 to 1000.
    """
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_sorted_rotated_dataset(size: int) -> list[int]:
    """
    Generate a sorted, then rotated dataset.

    Parameters
    ----------
    size : int
        The number of items in the list.

    Returns
    -------
    list[int]
        A sorted list of integers rotated by a random pivot.
    """
    if size == 0:
        return []
    sorted_list = list(range(size))
    pivot = random.randint(0, size - 1)
    return sorted_list[pivot:] + sorted_list[:pivot]

def generate_random_float_dataset(size: int) -> list[float]:
    """
    Generate a dataset of random floating-point numbers.

    Parameters
    ----------
    size : int
        The number of elements in the dataset.

    Returns
    -------
    list[float]
        A list of random floats in the range [0.0, 1000.0).
    """
    return [random.uniform(0.0, 1000.0) for _ in range(size)]

def generate_periodic_pattern_dataset(size: int) -> list[int]:
    """
    Generate a list with a periodic repeating pattern.

    Parameters
    ----------
    size : int
        The number of items in the list.

    Returns
    -------
    list[int]
        A list where a specific pattern of [1, 2, 3] is repeated to fill the dataset.
    """
    pattern = [1, 2, 3]
    repeated = (pattern * ((size // len(pattern)) + 1))[:size]
    return repeated