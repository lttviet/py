import random
from typing import List

def random_sampling(lst: List[int], k: int) -> List[int]:
    """Returns a random subset of size k.
    """
    for i in range(k):
        r = random.randrange(i, len(lst))
        lst[i], lst[r] = lst[r], lst[i]

    return lst[:k]

if __name__ == '__main__':
    for lst in ([1,2,3], [1,2,3,4], [1,2,3,4,5,6]):
        print(random_sampling(lst, 3))