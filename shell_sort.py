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

"""
Pseudo code for Shell Sort

DEFINE generate_gapValues(arrSize){
                INITIALIZE gapValues = [ ]
                INITIALIZE gap = arrSize // 2
                WHILE gap >= 1 {
                        APPEND gap TO gapValues
                        SET gap = gap // 2
                }
                RETURN gapValues
}


DEFINE InsertionSortInterleaved(arr, arrSize, startIndex, gapValue) {
                INITIALIZE swaps = 0
                FOR i FROM (startIndex + gapValue) TO (arrSize) in steps of gapValue {
                      INITIALIZE j = i
                      WHILE (j - gapValue) >= startIndex AND (arr[j] < arr[j - gapValue]) {
                                 INCREMENT swaps BY 1
                                 SWAP the value of arr[j] AND the value of arr[j - gapValue]
                                 DECREMENT j BY gapValue
                      }
               }
               RETURN swaps
}


DEFINE ShellSort(arr, arrSize, gapValues) {
                 INITIALIZE swaps = [ ]  
                 FOR each gapValue in the list gapValues {
                          FOR i FROM 0 TO (gapValue - 1) {
                                   APPEND InsertionSortInterleaved(arr, arrSize, i, gapValue) TO
swaps
                          }
         }
               RETURN swaps
}

"""


import numpy as np
import time

def generate_gap_values(arrSize):
    gap_values = []
    gap = arrSize // 2
    while gap >= 1:
        gap_values.append(gap)
        gap = gap // 2
    return gap_values

def insertion_sort_interleaved(arr, start_index, gap_value):
    swaps = 0
    for i in range(start_index + gap_value, len(arr), gap_value):
        j = i
        while (j - gap_value >= start_index) and (arr[j] < arr[j - gap_value]):
            swaps += 1
            temp = arr[j]
            arr[j] = arr[j - gap_value]
            arr[j - gap_value] = temp
            j = j - gap_value
    return swaps

def shell_sort(arr):
    arrSize = len(arr)
    gap_values = generate_gap_values(arrSize)
    swaps = []
    for gap_value in gap_values:
        for i in range(gap_value):
            swaps.append(insertion_sort_interleaved(arr, i, gap_value))
    return swaps
    
    

if __name__ == "__main__":
    my_arr = []

    for i in range(100):
        my_arr.append(np.random.randint(100))

    print("Unsorted:", my_arr)
    print()
    
    start_time = time.time()
    swap_counts = shell_sort(my_arr)
    end_time = time.time()
    
    print("Sorted:", my_arr)
    print()
    
    total_swap = sum(swap_counts)
    print("Total swaps: ", total_swap)
    print()
    print("Execution Time: ", end_time - start_time)









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
