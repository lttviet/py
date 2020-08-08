from typing import List

def len_longest_equal_sublist(lst: List[int]) -> int:
    """Finds the length of a longest sublist
    all of whose entries are equal.
    """
    cur_val, cur_val_length, longest_length = None, 0, 0

    for val in lst:
        if val == cur_val:
            cur_val_length += 1
            longest_length = max(longest_length, cur_val_length)
        else:
            cur_val = val
            cur_val_length = 1

    return longest_length

if __name__ == '__main__':
    for lst in ([1,1,1,2,1,1,1,1], [2,2,2,1], [1,1,2,2]):
        print(lst, len_longest_equal_sublist(lst))