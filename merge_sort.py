"""
Implementation of the merge sort algorithm.

Merge sort merges the two partitions into a single list by repeatedly selecting the smallest element
from either the left or right partition and adding that element to the temporary merged list.
Once fully merged, this temporary merged list is copied back to the original list

Merge sort is a divide and conquer algorithm that divides the input array into two halves,
recursively sorts the two halves and merges the sorted halves to create a sorted array.
The time complexity varies based on the given sequence, but the average runtime is O(NlogN).
"""

def merge(numbers: list[int | float], start_index: int, mid_index: int, end_index: int) -> None:
    """
    Merge two sorted subarrays into a single sorted subarray.

    Parameters
    ----------
    numbers : list[int|float]
        The list containing the subarrays to merge
    start_index : int
        Start index of the first subarray
    mid_index : int
        End index of the first subarray
    end_index : int
        End index of the second subarray (second subarray starts at j+1)
    """
    merged_size = end_index - start_index + 1
    merged_numbers = [0] * merged_size
    merge_position = 0
    left_position = start_index
    right_position = mid_index + 1
    # Add the smallest element from left or right partition to merged numbers
    while left_position <= mid_index and right_position <= end_index:
        if numbers[left_position] <= numbers[right_position]:
            merged_numbers[merge_position] = numbers[left_position]
            left_position += 1
        else:
            merged_numbers[merge_position] = numbers[right_position]
            right_position += 1
        merge_position += 1
    # If left partition is not empty, add remaining elements to merged numbers
    while left_position <= mid_index:
        merged_numbers[merge_position] = numbers[left_position]
        left_position += 1
        merge_position += 1
    # If right partition is not empty, add remaining elements to merged numbers
    while right_position <= end_index:
        merged_numbers[merge_position] = numbers[right_position]
        right_position += 1
        merge_position += 1
    # Copy merge back to original list
    for merge_index in range(merged_size):
        numbers[start_index + merge_index] = merged_numbers[merge_index]


def merge_sort(numbers: list[int | float], start_index: int, end_index: int) -> None:
    """
    Sort a subarray using the merge sort algorithm.

    This function recursively divides the array into halves until each subarray
    contains at most one element, then merges them back together in sorted order.

    Parameters
    ----------
    numbers : list[int|float]
        - The list to be sorted (sorted in-place)
    start_index : int
        - Start index of the subarray to be sorted
    end_index : int
        - End index of the subarray to be sorted
    """
    if numbers:
        if start_index < end_index:
            mid_index = (start_index + end_index) // 2
            # recursively sort left and right partitions
            merge_sort(numbers, start_index, mid_index)
            merge_sort(numbers, mid_index + 1, end_index)
            # merge left and right partition in sorted order
            merge(numbers, start_index, mid_index, end_index)


if __name__ == "__main__":
    test_one = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(test_one, 0, len(test_one) - 1)
    assert test_one == [3, 9, 10, 27, 38, 43, 82]

    test_two = [8, 4, 2, 8, 3, 4, 7, 1]
    merge_sort(test_two, 0, len(test_two)-1)
    assert test_two == [1, 2, 3, 4, 4, 7, 8, 8]

    test_three = [3.14, 1.59, 2.65, 3.58, 9.79, 3.23]
    merge_sort(test_three, 0, len(test_three)-1)
    assert test_three == [1.59, 2.65, 3.14, 3.23, 3.58, 9.79]