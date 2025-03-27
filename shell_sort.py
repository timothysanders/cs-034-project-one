"""
Datasets and Test cases for Shell Sort

1) Even distributed list without large clusters of disorder

2) An unevenly distributed list, where elements are positioned in a way that
requires frequent long-distance swaps—for example, extremely small numbers
clustered near the end or extremely large numbers grouped near the beginning.

3) Partly ordered yet frequently updated list, such as time-series data in the
database, where older entries remain mostly in order while new data is appended.
For example, in a Stock Order Book application,  the first 80% of the data list
is already sorted by price.  Incoming trades will be randomly inserted In the last
20% of the given list. Then we will measure the efficiency and performance of Shell
Sort to mimic this real-life scenario.

"""

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

# Generate characteristic testing datasets
def generate_structured_datasets(size):
    """Structured datasets for characteristic testing."""
    half = size // 2
    return {
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
    }

# Generate large scale random datasets
def generate_large_random_dataset(size):
    """Single large random dataset for scalability testing."""
    return {
        f"Large Random ({size:,})": np.random.randint(0, 1_000_000, size)
    }


# Main execution block
if __name__ == "__main__":
    results = []
    
    # Structured dataset size
    structured_size = 5_000
    structured_datasets = generate_structured_datasets(structured_size)

    # Large random dataset size
    large_size = 200_000
    large_dataset = generate_large_random_dataset(large_size)

    # Combine both sets of datasets
    all_datasets = {**structured_datasets, **large_dataset}

    print(f"\n Dataset Characteristics\n")
    for name, data in all_datasets.items():
        print(f"Dataset: {name}")
        print(f"  ➤ Size: {len(data)}")
        print(f"  ➤ Min: {np.min(data)}")
        print(f"  ➤ Max: {np.max(data)}")
        print(f"  ➤ Mean: {np.mean(data):.2f}")
        print(f"  ➤ Std Dev: {np.std(data):.2f}")
        print("-" * 40)

    for name, data in all_datasets.items():
        my_arr = data.copy()

        start_time = time.time()
        swap_counts = shell_sort(my_arr)
        end_time = time.time()

        total_swaps = sum(swap_counts)
        execution_time = end_time - start_time

        results.append({
            "Dataset": name,
            "Size": len(data),
            "Total Swaps": total_swaps,
            "Execution Time (s)": execution_time
        })

    df = pd.DataFrame(results)
    print("\n Shell Sort Performance Summary:\n")
    print(df.to_string(index=False))


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
Implementation of the shell sort algorithm.

Shell sort uses a variation of the insertion sort algorithm to sort subsets of an input list.
Instead of sorting items immediately adjacent to each other, it compares elements that are a fixed distance apart,
known as a gap space, or gap value.

The algorithm performs multiple passes with decreasing gap values, gradually sorting the list.
The time complexity varies based on the given sequence, but the average runtime is O(N^{1.5}).


def insertion_sort_interleaved(numbers: list[int], start_index: int, gap: int) -> None:
    '''
    Perform insertion sort on interleaved elements with the specified gap.

    This function sorts a subsequence of elements starting at start_index
    and considering only elements that are 'gap' indices apart.

    Parameters
    ----------
    numbers : list[int]
        - The list to be sorted
    start_index : int
        - The starting position for sorting
    gap : int
        - The interval between elements of the list

    Returns
    -------
    None
   '''
    if not numbers or start_index < 0 or gap < 1 or start_index >= len(numbers):
        raise ValueError("Invalid parameters")

    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            numbers[j], numbers[j - gap] = numbers[j - gap], numbers[j]
            j = j - gap


def shell_sort(numbers: list[int], gap_values: list[int]) -> None:
   '''
    Sort a list using the shell sort algorithm.

    Performs multiple passes over the list with decreasing gap values.
    Each pass sorts interleaved subsequences using `insertion_sort_interleaved()`.

    Parameters
    ----------
    numbers : list[int]
        - The list to be sorted
    gap_values : list[int]
        - A sequence of gap values (preferably in descending order)
    Returns
    -------
    None
    '''
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)

if __name__ == "__main__":
    test_one = [9, 8, 3, 7, 5, 6, 4, 1]
    shell_sort(test_one, [4, 2, 1])
    assert test_one == [1, 3, 4, 5, 6, 7, 8, 9]

"""
