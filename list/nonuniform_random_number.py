import random
import itertools
import bisect
from typing import List

def random_num(val: List[int], p: List[int]) -> int:
    """Given a list of probabilities for some numbers
    Returns a number according to the probabilities.
    """
    cumulative_p = list(itertools.accumulate(p))
    random_idx = bisect.bisect_left(cumulative_p, random.random())

    return val[random_idx]

if __name__ == '__main__':
    print(random_num([1,2,3], [0.25, 0.5, 0.25]))