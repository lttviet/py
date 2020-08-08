from typing import List

def reorder_false_true(lst: List[bool]) -> List[bool]:
    """Reorder a list of booleans to have false first.
    """
    # lst[:f] false
    # lst[f:t] unclassified
    # lst[t:] true
    f, t = 0, len(lst)
    while f < t:
        if not lst[f]:
            f += 1
        else:
            t -= 1
            lst[f], lst[t] = lst[t], lst[f]

    return lst

if __name__ == '__main__':
    lists = (
        [False, True, False, True],
        [False, False, True],
        [True]
    )

    for lst in lists:
        print(reorder_false_true(lst))