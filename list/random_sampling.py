import random
from typing import List

def random_sampling(lst: List[int], k: int) -> List[int]:
    """Returns a random subset of size k.
    """
    for i in range(k):
        r = random.randrange(i, len(lst))
        lst[i], lst[r] = lst[r], lst[i]

    return lst[:k]

def get_random_permutation(n: int) -> List[int]:
    permutation = list(range(n))
    random_sampling(permutation, n)
    return permutation

def online_sampling(n: int, k: int) -> List[int]:
    """Returns a random size-k subset of [0...n-1]
    """
    # to save space, don't create a list of n elements
    change = {}

    for i in range(k):
        random_idx = random.randrange(i, n)
        # may already been changed
        random_idx_mapped = change.get(random_idx, random_idx)
        idx_mapped = change.get(i, i)

        change[i] = random_idx_mapped
        change[random_idx] = idx_mapped

    return [change[i] for i in range(k)]

if __name__ == '__main__':
    for lst in ([1,2,3], [1,2,3,4], [1,2,3,4,5,6]):
        print(random_sampling(lst, 3))

    for n in (10, 20, 14):
        print(get_random_permutation(n))