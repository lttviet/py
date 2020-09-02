import random
from typing import List

def random_online_sampling(lst: List, k: int) -> List:
    # Assume lst has at least k elements
    sample = lst[:k]

    seen = k
    for ele in lst[k:]:
        seen += 1

        # get a random element [:seen] to be removed
        idx_to_replace = random.randrange(seen)
        # if < k, replace it with new element
        if idx_to_replace < k:
            sample[idx_to_replace] = ele

    return sample

if __name__ == '__main__':
    for lst in ([i for i in range(10)], [i for i in range(20)]):
        print(random_online_sampling(lst, 4))