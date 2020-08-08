from typing import List

def delete_key(lst: List[int], key: int) -> List[int]:
    """Delete keys from a list.
    [v for v in lst if v != key]
    """
    j = 0
    for i in range(len(lst)):
        if lst[i] != key:
            lst[j] = lst[i]
            j += 1

    return lst[:j]

if __name__ == '__main__':
    for lst in ([1,1,1,1,1,2], [1,1,2,2,3,3,4], [1,2,3,4], [2,3,4]):
        print(delete_key(lst, 1))