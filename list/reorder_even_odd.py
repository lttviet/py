from typing import List

def even_odd(lst: List[int]) -> List[int]:
    """Reorder list to have even numbers appear first.
    
    lst.sort(key=lambda x: x%2)
    """
    even, odd = 0, len(lst) - 1
    while even < odd:
        if lst[even] % 2 == 0:
            even += 1
        else:
            lst[even], lst[odd] = lst[odd], lst[even]
            odd -= 1

    return lst

if __name__ == '__main__':
    lists = ([1,2,3], [], [2], [3,3], [4,4], [1,2,3,4,5,6,7,8,9])
    for lst in lists:
        print(even_odd(lst))