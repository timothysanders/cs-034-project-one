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