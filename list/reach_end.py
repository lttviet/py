from typing import List

def can_reach_end(lst: List[int]) -> bool:
    """Returns True if can reach end of list.

    lst[i]: num of steps from index i
    """
    i, max_reach, last_index = 0, 0, len(lst) - 1
    while i <= max_reach and max_reach < last_index:
        max_reach = max(max_reach, lst[i] + i)
        i += 1
    
    return max_reach >= last_index

if __name__ == '__main__':
    for lst in ([10,1,1,1], [3,3,1,0,2,0,1], [0,1], [1,1,1,1,1]):
        print(lst, can_reach_end(lst))