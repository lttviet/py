from typing import List

def plus_one(lst: List[int]) -> List:
    """Take a list of integers, which represents a decimal number N.
    Returns the list that represents N+1
    """
    lst[-1] += 1
    
    for i in reversed(range(1, len(lst))):
        if lst[i] != 10:
            break
        lst[i] = 0
        lst[i-1] += 1

    if lst[0] == 10:
        lst[0] = 0
        lst.insert(0, 1)

    return lst

if __name__ == '__main__':
    for lst in ([1,2,3], [0], [9], [9,9], [1,0,0]):
        print(plus_one(lst))