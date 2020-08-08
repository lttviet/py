from typing import List

def delete_duplicates(lst: List[int]) -> List[int]:
    """Delete duplicate numbers from sorted array.
    """
    j = 1 # new value index

    # 0:j no duplicate sub array
    # i:len(lst) original sub array
    # sorted -> compare lst[j-1] and lst[i] to see if duplicate

    for i in range(1, len(lst)):
        if lst[j-1] != lst[i]:
            lst[j] = lst[i]
            j += 1

    return lst[0:j]

if __name__ == '__main__':
    for lst in ([1,1,1,1,1], [1,1,2,2,3,3,4], [1,2,3,4]):
        print(delete_duplicates(lst))