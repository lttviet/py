from typing import List

def interleave(lst: List[int]) -> List[int]:
    """Reorder a list so that
    A[0] <= A[1] >= A[2] <= A[3] ...
    """
    for i in range(len(lst)-1):
        if (
            (i % 2 == 0 and lst[i] > lst[i+1]) or 
            (i % 2 == 1 and lst[i] < lst[i+1])
        ):
            # swap if A[0] > A[1] or A[1] < A[2],... etc
            lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst


if __name__ == '__main__':
    for lst in ([10,9,8,20], [20,9,8,6], [10,20,10,30]):
        print(interleave(lst))