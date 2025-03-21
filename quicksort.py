"""
Implementation of the quicksort algorithm.

The quicksort algorithm partitions a section of the unsorted list into a low partition and a high partition,
based on the pivot element within the list. After each partition has been created, each partition needs to be sorted.
Quicksort is then called recursively to sort the low and high partitions. This recursive sorting process continues
until a partition has one or zero elements, which will already be sorted.

The time complexity varies based on the given sequence, but the average runtime is O(NlogN).
"""


def partition(numbers: list[int | float], low_index: int, high_index: int) -> int:
    """
    Partition the array segment and return the partition index.

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
    int
        The index of the last element in the lower partition
    """
    # Identify the midpoint/pivot value using floor division
    midpoint = low_index + (high_index - low_index) // 2
    pivot = numbers[midpoint]
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
            low_index += 1
            high_index -= 1
    return high_index


def quicksort(numbers: list[int | float], low_index: int, high_index: int) -> None:
    """
    Sort a segment of the list using quicksort algorithm.

    Parameters
    ----------
    numbers : list
        The list to be sorted (modified in-place)
    low_index : int
        The lower bound of the segment to be sorted
    high_index : int
        The upper bound of the segment to be sorted
    """
    if not numbers:
        ValueError("Invalid parameters.")
    # Our base case is where the partition size is 1 or zero elements
    if low_index >= high_index:
        return

    partition_index = partition(numbers, low_index, high_index)

    quicksort(numbers, low_index, partition_index)
    quicksort(numbers, partition_index + 1, high_index)


if __name__ == "__main__":
    test_one = [10, 2, 78, 4, 45, 32, 7, 11]
    quicksort(test_one, 0, len(test_one) - 1)
    assert test_one == [2, 4, 7, 10, 11, 32, 45, 78]