import pandas as pd
import time

from datasets import (generate_structured_datasets,
                      generate_merge_sort_datasets,
                      generate_quicksort_datasets,
                      generate_shell_sort_datasets)
from quicksort import quicksort
from merge_sort import merge_sort
from shell_sort import shell_sort


# Time sorting algorithms on the datasets
def time_sorting_algorithms(size: int):
    datasets = generate_structured_datasets(size)
    results = []

    for name, data in datasets.items():
        n = len(data)

        # Shell Sort (with gap-aware implementation)
        arr_shell = data.copy()
        t1 = time.time()
        swap_counts = shell_sort(arr_shell)
        t_shell = time.time() - t1
        total_shell_swaps = sum(swap_counts)

        # QuickSort
        arr_quicksort = data.copy()
        t2 = time.time()
        quicksort(arr_quicksort, 0, len(arr_quicksort) - 1)
        t_quick = time.time() - t2

        # MergeSort
        arr_mergesort = data.copy()
        t3 = time.time()
        merge_sort(arr_mergesort, 0, len(arr_mergesort) - 1)
        t_merge = time.time() - t3

        results.append({
            "Dataset": name,
            "Size": n,
            "Shell Sort Time (s)": t_shell,
            "Shell Sort Swaps": total_shell_swaps,
            "QuickSort Time (s)": t_quick,
            "QuickSort Swaps": 0,
            "MergeSort Time (s)": t_merge,
            "MergeSort Swaps": 0
        })

    return pd.DataFrame(results)

def time_shell_sort_algorithm(size: int):
    datasets = generate_shell_sort_datasets(size)
    results = []
    for name, data in datasets.items():
        n = len(data)
        # Shell Sort (with gap-aware implementation)
        t1 = time.time()
        swap_counts = shell_sort(data)
        t_shell = time.time() - t1
        total_shell_swaps = sum(swap_counts)
        results.append({
            "Dataset": name,
            "Size": n,
            "Shell Sort Time (s)": t_shell,
            "Shell Sort Swaps": total_shell_swaps,
        })
    return pd.DataFrame(results)

def time_merge_sort_algorithm(size: int):
    datasets = generate_merge_sort_datasets(size)
    results = []
    for name, data in datasets.items():
        n = len(data)
        t1 = time.time()
        merge_sort(data, 0, len(data) - 1)
        t_merge = time.time() - t1
        results.append({
            "Dataset": name,
            "Size": n,
            "Merge Sort Time (s)": t_merge,
            "Merge Sort Swaps": 0,
        })
    return pd.DataFrame(results)

def time_quick_sort_algorithm(size: int):
    datasets = generate_quicksort_datasets(size)
    results = []
    for name, data in datasets.items():
        n = len(data)
        t1 = time.time()
        quicksort(data, 0, len(data) - 1)
        t_quick = time.time() - t1
        results.append({
            "Dataset": name,
            "Size": n,
            "QuickSort Time (s)": t_quick,
            "QuickSort Swaps": 0,
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    dataset_size = 1000
    general_results = time_sorting_algorithms(dataset_size)
    shell_sort_results = time_shell_sort_algorithm(dataset_size)
    quicksort_results = time_quick_sort_algorithm(dataset_size)
    merge_sort_results = time_merge_sort_algorithm(dataset_size)
    print(f"""
    -------------------------
    GENERAL RESULTS
    -------------------------
    {general_results}
    -------------------------
    SHELL SORT RESULTS
    -------------------------
    {shell_sort_results}
    -------------------------
    QUICKSORT RESULTS
    -------------------------
    {quicksort_results}
    -------------------------
    MERGE SORT RESULTS
    -------------------------
    {merge_sort_results}
    """)