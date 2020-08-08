from typing import List, Callable

def reorder_relative_order_true(lst: List[bool], fn: Callable) -> List[bool]:
    """ Reorder array to have false first then true.
    Keep the relative order of true.
    """
    # https://stackoverflow.com/questions/29723998
    # idea is to avoid swapping 2 true elements
    # loop from the end to beginning
    # lst[t:] true
    t = len(lst)
    for i in range(len(lst)-1, -1, -1):
        if fn(lst[i]):
            t -= 1
            lst[i], lst[t] = lst[t], lst[i]

    return lst

if __name__ == '__main__':
    lists = (
        [1,2,3,4,5],
        [2,4,6],
        [4,9,11,2,3,8]
    )

    for lst in lists:
        print(reorder_relative_order_true(lst, lambda x: x%2 == 0))