from typing import List

def update(lst: List[int], m: int) -> List[int]:
    """Given an ordered list, positive int m, update the list so
    if x appears m times in original list, x will show up min(2,m) in returned list
    
    ex. update([10,10,10], 2) -> [10,10]
        update([10,10,10], 1) -> [10]
        update([12,12,12], 3) -> [12, 12] 
    """
    exact = min(2, m)
    j = exact
    for i in range(exact, len(lst)):
        if (
            (exact == 1 and lst[i] != lst[j-1]) or 
            (
                exact == 2 and 
                (lst[j-1] != lst[j-2] or lst[j-1] != lst[i])
            )
        ):
            lst[j] = lst[i]
            j += 1           

    return lst[:j]

if __name__ == '__main__':
    for lst in ([1,2,3], [1,2,2,2,3], [1,2,2,3,3,3,4]):
        print(update(lst, 2))