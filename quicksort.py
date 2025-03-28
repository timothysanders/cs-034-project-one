"""
Implementation of the quicksort algorithm.

The quicksort algorithm partitions a section of the unsorted list into a low partition and a high partition,
based on the pivot element within the list. After each partition has been created, each partition needs to be sorted.
Quicksort is then called recursively to sort the low and high partitions. This recursive sorting process continues
until a partition has one or zero elements, which will already be sorted.

The time complexity varies based on the given sequence, but the average runtime is O(NlogN).
"""


def partition(numbers: list[int | float], low_index: int, high_index: int) -> tuple[int, int]:
    """
    Partition the array segment and return the partition index, along with the swap count.

    Parameters
    ----------
    numbers : list[int|float]
        The list to be partitioned
    low_index : int
        The lower bound of the segment to be partitioned
    high_index : int
        The upper bound of the segment to be partitioned

    Returns
    -------
    tuple[int, int]
        A tuple containing the index of the last element in the lower partition and the number of swaps made.
    """
    # Identify the midpoint/pivot value using floor division
    midpoint = low_index + (high_index - low_index) // 2
    pivot = numbers[midpoint]
    swap_count = 0
    done = False
    while not done:
        while numbers[low_index] < pivot:
            low_index += 1
        while pivot < numbers[high_index]:
            high_index -= 1
        if low_index >= high_index:
            done = True
        else:
            numbers[low_index], numbers[high_index] = numbers[high_index], numbers[low_index]
            swap_count += 1
            low_index += 1
            high_index -= 1
    return high_index, swap_count


def quicksort(numbers: list[int | float], low_index: int, high_index: int) -> int:
    """
    Sort a segment of the list using the quicksort algorithm and count the number of swaps.

    Parameters
    ----------
    numbers : list
        The list to be sorted (modified in-place)
    low_index : int
        The lower bound of the segment to be sorted
    high_index : int
        The upper bound of the segment to be sorted

    Returns
    -------
    int
        The total number of swaps made during the sorting process
    """
    if not numbers:
        ValueError("Invalid parameters.")
    # Our base case is where the partition size is 1 or zero elements
    if low_index >= high_index:
        return 0

    partition_index, swap_count_partition = partition(numbers, low_index, high_index)

    swap_count_left = quicksort(numbers, low_index, partition_index)
    swap_count_right = quicksort(numbers, partition_index + 1, high_index)
    return swap_count_partition + swap_count_left + swap_count_right


if __name__ == "__main__":
    test_one = [10, 2, 78, 4, 45, 32, 7, 11]
    quicksort(test_one, 0, len(test_one) - 1)
    assert test_one == [2, 4, 7, 10, 11, 32, 45, 78]