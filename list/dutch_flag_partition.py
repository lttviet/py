from typing import List

def dutch_flag_partition(lst: List[int], index: int) -> List[int]:
    """Reorder to less than lst[index], equal to lst[index] 
    and higher than lst[index]
    """
    if len(lst) < 2:
        return lst

    if index > len(lst):
        return None

    pivot = lst[index]
    # lst[:smaller] smaller than
    # lst[smaller:equal] equal to
    # lst[equal:higher] unclassified
    # lst[higher:] higher than
    smaller, equal, higher = 0, 0, len(lst)

    while equal < higher: # loop as long as there're unclassified
        # lst[equal] unclassified variable
        if lst[equal] < pivot:
            lst[equal], lst[smaller] = lst[smaller], lst[equal]
            smaller += 1
            equal += 1
        elif lst[equal] == pivot:
            equal += 1
        else:
            higher -= 1
            lst[equal], lst[higher] = lst[higher], lst[equal]

    return lst

if __name__ == '__main__':
    lists = ([1,2,2,4,5], [4,2,4,4,6,4], [2], [])
    for lst in lists:
        print(dutch_flag_partition(lst, 2))