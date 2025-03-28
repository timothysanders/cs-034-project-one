import timeit
import tracemalloc

from datasets import (generate_random_integer_list,
                      generate_evenly_distributed, 
                      generate_unevenly_distributed, 
                      generate_partly_ordered, 
                      generate_sorted_with_random_indices_swapped, 
                      generate_exponentially_growing_dataset, 
                      generate_fractal_dataset, 
                      generate_sorted_in_groups, 
                      generate_list_of_evens, 
                      generate_list_of_odds, 
                      generate_list_of_duplicates_of_one, 
                      generate_list_of_duplicates_of_multiple)   
from quicksort import quicksort
from merge_sort import merge_sort
from shell_sort import shell_sort


def measure_quicksort_memory() -> None:
    """
    Measure the memory utilization of the quicksort algorithm on the list `numbers`.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """
    numbers = generate_random_integer_list(size=100000)
    tracemalloc.start()
    quicksort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for quicksort: {peak / 1024**2:.4f} MB")


def measure_merge_sort_memory() -> None:
    """
    Measure the memory utilization of the merge sort algorithm on the list `numbers`.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """
    numbers = generate_random_integer_list(size=100000)
    tracemalloc.start()
    merge_sort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for merge sort: {peak / 1024**2:.4f} MB")


def measure_shell_sort_memory() -> None:
    """
    Measure the memory utilization of the shell sort algorithm on the list `numbers`.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """
    numbers = generate_random_integer_list(size=100000)
    tracemalloc.start()
    shell_sort(numbers, [88573, 29524, 9841, 3280, 1093, 364, 121, 40, 13, 4])
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for shell sort: {peak / 1024**2:.4f} MB")


def measure_quicksort_memory_for_list_of_evens() -> None:
    """
    Measure the memory utilization of quicksort on a list of even numbers.

    Parameters
    ----------
    numbers : list[int]
    - A list of numbers to be sorted.

    Returns
    -------
    None
    """
    numbers = generate_list_of_evens(size=100000)
    tracemalloc.start()
    quicksort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for quicksort on evens: {peak / 1024**2:.4f} MB")


def measure_quicksort_memory_for_list_of_odds() -> None:
    """
    Measure the memory utilization of quicksort on a list of odd numbers.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """        
    numbers = generate_list_of_odds(size=100000)
    tracemalloc.start()
    quicksort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for quicksort on odds: {peak / 1024**2:.4f} MB")


def measure_quicksort_memory_for_list_of_duplicates_of_one() -> None:
    """
    Measure the memory utilization of quicksort on a list of duplicates of one number.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """              
    numbers = generate_list_of_duplicates_of_one(size=100000)
    tracemalloc.start()
    quicksort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for quicksort on single duplicates: {peak / 1024**2:.4f} MB")      


def measure_quicksort_memory_for_list_of_duplicates_of_multiple() -> None:
    """
    Measure the memory utilization of quicksort on a list of duplicates of multiple numbers.

    Parameters
    ----------
    numbers : list[int]
        - A list of numbers to be sorted.

    Returns
    -------
    None
    """           
    numbers = generate_list_of_duplicates_of_multiple(size=100000, num_duplicates=500)
    tracemalloc.start()
    quicksort(numbers, 0, len(numbers) - 1)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Peak memory usage for quicksort on multiple duplicates: {peak / 1024**2:.4f} MB")    
    

if __name__ == "__main__":
    execution_time = timeit.timeit(
        stmt=lambda: measure_quicksort_memory(),
        number=10
    )
    print(f"Total quicksort execution time: {execution_time:.4f} seconds for 10 runs.")

    execution_time = timeit.timeit(
        stmt=lambda: measure_merge_sort_memory(),
        number=10
    )
    print(f"Total merge sort execution time: {execution_time:.4f} seconds for 10 runs.")

    execution_time = timeit.timeit(
        stmt=lambda: measure_shell_sort_memory(),
        number=10
    )
    print(f"Total shell sort execution time: {execution_time:.4f} seconds for 10 runs.")

    execution_time = timeit.timeit(
        stmt=lambda: measure_quicksort_memory_for_list_of_evens(),
        number=10
    )
    print(f"Total quicksort execution time for list of evens: {execution_time:.4f} seconds for 10 runs.")

    execution_time = timeit.timeit(
        stmt=lambda: measure_quicksort_memory_for_list_of_odds(),
        number=10
    )
    print(f"Total quicksort execution time for list of odds: {execution_time:.4f} seconds for 10 runs.")  

    execution_time = timeit.timeit(
        stmt=lambda: generate_list_of_duplicates_of_one(),
        number=10
    )
    print(f"Total quicksort execution time for a list of duplicates of one number: {execution_time:.4f} seconds for 10 runs.") 
     
    execution_time = timeit.timeit(
        stmt=lambda: measure_quicksort_memory_for_list_of_duplicates_of_multiple(),
        number=10
    )
    print(f"Total quicksort execution time for a list of duplicates of multiple numbers: {execution_time:.4f} seconds for 10 runs.")         
